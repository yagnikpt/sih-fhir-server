import asyncio
import csv
import os
from dotenv import load_dotenv
from pymongo import AsyncMongoClient
from app.models.conceptmap import (
    CodeSystem,
    CodeSystemConcept,
    ConceptMap,
    ConceptMapGroup,
    ConceptMapElement,
)

_ = load_dotenv()


async def seed_data():
    client = AsyncMongoClient(os.getenv("DB_URL"))
    db = client["fhir_records"]
    codesystems = db["codesystems"]
    conceptmaps = db["conceptmaps"]

    # Clear existing data
    await codesystems.delete_many({})
    await conceptmaps.delete_many({})

    # Read CSV
    namaste_concepts = []
    icd11_concepts = []
    mappings = []

    with open("data/mappingcode.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            namaste_concepts.append(
                CodeSystemConcept(
                    code=row["namaste_code"],
                    display=row["namaste_display"],
                    definition=row.get("namaste_definition"),
                )
            )
            icd11_concepts.append(
                CodeSystemConcept(
                    code=row["icd11_code"],
                    display=row["icd11_display"],
                    definition=row.get("icd11_definition"),
                )
            )
            mappings.append(
                {
                    "source": row["namaste_code"],
                    "target": row["icd11_code"],
                    "equivalence": row["equivalence"],
                }
            )

    # Remove duplicates
    namaste_concepts = list({c.code: c for c in namaste_concepts}.values())
    icd11_concepts = list({c.code: c for c in icd11_concepts}.values())

    # Create CodeSystems
    namaste_cs = CodeSystem(
        id="namaste",
        url="https://namaste.codesystem",
        version="1.0",
        name="NAMASTE Code System",
        status="active",
        content="complete",
        concept=namaste_concepts,
        resourceType="CodeSystem",
    )

    icd11_cs = CodeSystem(
        id="icd11",
        url="https://icd11.codesystem",
        version="1.0",
        name="ICD-11 Code System",
        status="active",
        content="complete",
        concept=icd11_concepts,
        resourceType="CodeSystem",
    )

    await codesystems.insert_one(namaste_cs.model_dump())
    await codesystems.insert_one(icd11_cs.model_dump())

    # Create ConceptMap
    elements = []
    for mapping in mappings:
        elements.append(
            ConceptMapElement(
                code=mapping["source"],
                target=[
                    {"code": mapping["target"], "equivalence": mapping["equivalence"]}
                ],
                display=next(
                    (
                        c.display
                        for c in namaste_concepts
                        if c.code == mapping["source"]
                    ),
                    "",
                ),
            )
        )

    conceptmap = ConceptMap(
        id="namaste-to-icd11",
        url="https://namaste-to-icd11.conceptmap",
        version="1.0",
        name="NAMASTE to ICD-11 Mapping",
        status="active",
        group=[
            ConceptMapGroup(
                source="https://namaste.codesystem",
                target="https://icd11.codesystem",
                element=elements,
            )
        ],
        resourceType="ConceptMap",
    )

    await conceptmaps.insert_one(conceptmap.model_dump())

    print("Seeding completed.")
    await client.close()


if __name__ == "__main__":
    asyncio.run(seed_data())
