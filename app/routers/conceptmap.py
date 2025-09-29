from fastapi import APIRouter, Depends, HTTPException, Header
from pymongo.asynchronous.collection import AsyncCollection
from internal.database import (
    get_db,
    get_codesystem_collection,
    get_conceptmap_collection,
)
from app.models.conceptmap import CodeSystem, ConceptMap

router = APIRouter()


def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != "secret-key":  # For MVP, simple check
        raise HTTPException(status_code=401, detail="Invalid API Key")


@router.get(
    "/codesystem/{id}",
    response_model=CodeSystem,
    dependencies=[Depends(verify_api_key)],
)
async def get_codesystem(id: str, db=Depends(get_db)):
    collection = await get_codesystem_collection(db)
    cs = await collection.find_one({"id": id})
    if not cs:
        raise HTTPException(status_code=404, detail="CodeSystem not found")
    cs.pop("_id", None)  # Remove MongoDB _id
    return CodeSystem(**cs)


@router.get(
    "/conceptmap/{id}",
    response_model=ConceptMap,
    dependencies=[Depends(verify_api_key)],
)
async def get_conceptmap(id: str, db=Depends(get_db)):
    collection = await get_conceptmap_collection(db)
    cm = await collection.find_one({"id": id})
    if not cm:
        raise HTTPException(status_code=404, detail="ConceptMap not found")
    cm.pop("_id", None)  # Remove MongoDB _id
    return ConceptMap(**cm)


@router.get("/lookup", dependencies=[Depends(verify_api_key)])
async def lookup(q: str, db=Depends(get_db)):
    collection = await get_codesystem_collection(db)
    cs = await collection.find_one({"id": "namaste"})
    if not cs:
        raise HTTPException(status_code=404, detail="NAMASTE CodeSystem not found")
    results = [
        c
        for c in cs["concept"]
        if q.lower() in c["code"].lower()
        or (c.get("display") and q.lower() in c["display"].lower())
    ]
    return {"results": results[:10]}  # Limit to 10


@router.get("/translate", dependencies=[Depends(verify_api_key)])
async def translate(
    code: str, source: str = "namaste", target: str = "icd11", db=Depends(get_db)
):
    collection = await get_conceptmap_collection(db)
    cm = await collection.find_one({"id": f"{source}-to-{target}"})
    if not cm:
        raise HTTPException(status_code=404, detail="ConceptMap not found")
    for group in cm["group"]:
        for element in group["element"]:
            if element["code"] == code:
                return {"mappings": element["target"]}
    return {"mappings": []}


@router.post("/upload", dependencies=[Depends(verify_api_key)])
async def upload_bundle(bundle: dict, db=Depends(get_db)):
    # For MVP, just acknowledge receipt. In real, validate and store.
    return {"status": "Bundle received", "id": "some-id"}
