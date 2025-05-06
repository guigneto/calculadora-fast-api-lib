# 🧮 Calculadora FastAPI

Este projeto é uma API simples de calculadora, construída com FastAPI, utilizando o padrão arquitetural **MVC (Model-View-Controller)**. A lógica das operações foi separada em uma biblioteca interna para manter o código limpo e reutilizável.

---

## 📂 Estrutura do Projeto

```
calculadora-fastapi/
├── app/
│   ├── main.py                  # Inicialização da aplicação FastAPI
│   ├── controllers/
│   │   └── calculator_controller.py  # Controladores que executam a lógica
│   ├── models/
│   │   └── calculator_models.py      # Modelos Pydantic para entrada de dados
│   └── views/
│       └── routes.py                # Definição das rotas/endpoints
├── calculadora_lib/
│   └── operations.py           # Biblioteca com a lógica matemática
├── tests/
   └── test_main.py          # Arquivo para execução de testes automatizados
```
## 🚀 Tecnologias

- Python 3.10+
- FastAPI
- Uvicorn
- Pytest

---

## 🔥 Como rodar

1. Instale as dependências:

```bash
pip install fastapi uvicorn
```

2. Execute o servidor:

```bash
uvicorn app.main:app --reload
```

3. Acesse a documentação interativa:
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## ✅ Endpoints disponíveis

| Método | Rota               | Descrição                |
|--------|--------------------|--------------------------|
| POST   | `/soma`            | Soma dois números        |
| POST   | `/subtracao`       | Subtrai dois números     |
| POST   | `/multiplicacao`   | Multiplica dois números  |
| POST   | `/divisao`         | Divide dois números      |
| POST   | `/exponenciacao`   | Exponencia dois números  |

### 📤 Corpo da requisição (JSON):

```json
{
  "a": 10,
  "b": 2
}
```
## 🧪 Rodando os testes

Os testes automatizados estão na pasta `tests/`.

Execute com:

```bash
pytest tests/
```
---

## 📌 Licença

Este projeto é livre para uso educacional e pessoal.
