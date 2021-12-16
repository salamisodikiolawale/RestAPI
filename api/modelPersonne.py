from typing import Optional
from pydantic import BaseModel

class modelPersonne(BaseModel):
    nom: str
    prenom:str
    ssn: str


