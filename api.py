from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Привет, это менеджер задач"}


@app.get("/health")
def health():
    return {"status": "ok"}
