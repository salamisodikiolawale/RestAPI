from modelPersonne import modelPersonne
from fastapi import FastAPI
from pymongo import MongoClient
import json

app = FastAPI()

def database():
    host = 'mongodb'
    client = MongoClient(host=f'{host}')
    return client

@app.get("/personnes")
def fetch_personnes():

    db = database()
    results = db.registre.personnes.find()
    personnes = []
    for result in results:
        p = {"nom": result["nom"], "prenom": result["prenom"],
             "ssn": result["ssn"]}
        personnes.append(p)
    return personnes
    
@app.post("/personnes", response_model=modelPersonne)
def insert_personne(dataPersonne):
    db = database()
    # data_perso_dico = dataPersonne.dict()
    # db.registre.personnes.insert_one(data_perso_dico)
    return dataPersonne
