from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Atendimento(BaseModel):
    nome: str
    mensagem: str

@app.get("/")
def raiz():
    return {"mensagem": "Secretária Inteligente pronta para atender!"}

@app.post("/atendimento")
def responder(atendimento: Atendimento):
    nome = atendimento.nome
    mensagem = atendimento.mensagem.lower()

    if "consulta" in mensagem:
        return {"resposta": f"Olá {nome}, podemos agendar sua consulta. Qual seria o melhor dia para você?"}
    elif "cancelar" in mensagem:
        return {"resposta": f"{nome}, sua consulta será cancelada. Deseja remarcar?"}
    elif "horário" in mensagem:
        return {"resposta": f"{nome}, temos horários disponíveis pela manhã e tarde. Qual prefere?"}
    elif "obrigado" in mensagem or "valeu" in mensagem:
        return {"resposta": f"Disponha, {nome}! 😊"}
    else:
        return {"resposta": f"{nome}, não entendi bem sua mensagem. Pode repetir com mais detalhes?"}
