from pydantic import BaseModel, Field


class CodeSystemConcept(BaseModel):
    code: str = Field(..., description="The code value.")
    display: str | None = Field(
        None, description="Human-readable display for the code."
    )
    definition: str | None = Field(None, description="Formal definition of the code.")


class CodeSystem(BaseModel):
    resourceType: str = Field("CodeSystem")
    id: str | None = Field(None, description="Logical id of this artifact.")
    url: str = Field(..., description="Canonical identifier for this code system.")
    version: str | None = Field(None, description="Version identifier.")
    name: str | None = Field(None, description="Name for this code system.")
    status: str = Field(..., description="Status (e.g., 'active').")
    content: str = Field(..., description="Content mode (e.g., 'complete').")
    concept: list[CodeSystemConcept] = Field(
        ..., description="List of concepts (codes) in the system."
    )


class ConceptMapElement(BaseModel):
    code: str = Field(..., description="Identifies the source concept being mapped.")
    display: str | None = Field(None, description="Display for the source concept.")
    target: list[dict] = Field(..., description="Mappings for this concept.")


class ConceptMapGroup(BaseModel):
    source: str = Field(..., description="Source system URL.")
    target: str = Field(..., description="Target system URL.")
    element: list[ConceptMapElement] = Field(..., description="Mappings in this group.")


class ConceptMap(BaseModel):
    resourceType: str = Field("ConceptMap")
    id: str | None = Field(None, description="Logical id of this artifact.")
    url: str = Field(..., description="Canonical identifier for this concept map.")
    version: str | None = Field(None, description="Version identifier.")
    name: str | None = Field(None, description="Name for this concept map.")
    status: str = Field(..., description="Status (e.g., 'active').")
    group: list[ConceptMapGroup] = Field(..., description="Groups of mappings.")
