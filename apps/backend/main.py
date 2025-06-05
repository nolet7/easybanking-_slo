from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Easy Banking API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/balance")
def get_balance():
    return {"balance": 1000.00}

@app.post("/transfer")
def transfer(to: str, amount: float):
    return {"to": to, "amount": amount, "status": "success"}

Instrumentator().instrument(app).expose(app)
