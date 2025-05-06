from fastapi import FastAPI, HTTPException
from app.models import Operacao
from calculadora_lib import soma, subtracao, multiplicacao, divisao, exponenciacao

app = FastAPI()

@app.post("/soma")
def rota_soma(valores: Operacao):
    resultado = soma(valores.a, valores.b)
    return {"resultado": resultado}

@app.post("/subtracao")
def rota_subtracao(valores: Operacao):
    resultado = subtracao(valores.a, valores.b)
    return {"resultado": resultado}

@app.post("/multiplicacao")
def rota_multiplicacao(valores: Operacao):
    resultado = multiplicacao(valores.a, valores.b)
    return {"resultado": resultado}

@app.post("/divisao")
def rota_divisao(valores: Operacao):
    try:
        resultado = divisao(valores.a, valores.b)
        return {"resultado": resultado}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.post("/exponenciacao")
def rota_exponenciacao(valores: Operacao):
    resultado = exponenciacao(valores.a, valores.b)
    return {"resultado": resultado}