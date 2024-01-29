from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import spacy

# Carregando o modelo Spacy
nlp = spacy.load("pt_core_news_sm") # Altere conforme o modelo desejado

app = FastAPI()

class RequestBody(BaseModel):
    texto: str
    labels: list[str]

@app.post("/extrair-entidades/")
def extrair_entidades(request_body: RequestBody):
    texto = request_body.texto
    labels_desejados = request_body.labels
    doc = nlp(texto)

    entidades = {label: [] for label in labels_desejados}

    for ent in doc.ents:
        if ent.label_ in labels_desejados:
            entidades[ent.label_].append(ent.text)

    return entidades
