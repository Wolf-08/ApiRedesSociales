from typing import Optional
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = [
	"http://localhost",
	"http://localhost:4200",
]
app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

encuestas = []
class Result(BaseModel):
	email: str
	edad: str
	sexo: str
	redFavorita: str
	TiempoFacebook: int
	TiempoInstagram: int
	TiempoTikTok: int
	TiempoWhatsapp: int
	TiempoTwitter: int

@app.get("/")
def read_root():
	return {"Hello": "World Rasyue"}
@app.get("/test")
def test():
	return {"Hello": "World Test"}
@app.post('/form')
async def receive_data(result: Result):
	result_dict = result.dict()
	encuestas.append(result_dict)
	print(result_dict)
	return result

