from fastapi import FastAPI

app = FastAPI(title="Erebus API")

@app.get("/")
def root():
    return {"status": "ok"}
