from fastapi import APIRouter, HTTPException
from app.controllers import calculator_controller as controller
from app.models.calculator_models import Operacao

router = APIRouter()

@router.post("/soma")
def soma(op: Operacao):
    return {"resultado": controller.soma(op.a, op.b)}

@router.post("/subtracao")
def subtracao(op: Operacao):
    return {"resultado": controller.subtracao(op.a, op.b)}

@router.post("/multiplicacao")
def multiplicacao(op: Operacao):
    return {"resultado": controller.multiplicacao(op.a, op.b)}

@router.post("/divisao")
def divisao(op: Operacao):
    try:
        return {"resultado": controller.divisao(op.a, op.b)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/exponenciacao")
def exponenciacao(op: Operacao):
    return {"resultado": controller.exponenciacao(op.a, op.b)}