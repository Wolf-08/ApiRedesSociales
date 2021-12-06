from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from numpy import float64
from models.forms import Forms
from schemas.encuesta import Encuesta
from config.db import SessionLocal
from sqlalchemy.orm import Session
import pandas as pd
from sqlalchemy.sql import func

app = FastAPI(
		title = "API Encuestas",
    description = "Save data and stats",
    version = "1.0",
)
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

def get_database_session():
  try:
    db = SessionLocal()
    yield db
  finally:
    db.close()

@app.get("/")
def read_root():
	return {"Hello": "World "}

@app.get("/stats")
async def test(db: Session = Depends(get_database_session)):
	return db.query(Forms).count()

@app.get("/tiempoPromedio")
async def tiempoPromedio(db: Session = Depends(get_database_session)):
  tiempoPromedioRedSocial = []
  tiempoPromedio = db.query(
    Forms.TiempoFacebook,Forms.TiempoInstagram,
    Forms.TiempoTikTok,Forms.TiempoWhatsapp,Forms.TiempoTwitter)
  df = pd.DataFrame(tiempoPromedio)
  df.columns = [
    'TiempoFacebook','TiempoInstagram',
    'TiempoTikTok','TiempoWhatsapp','TiempoTwitter']
  for column in df.columns:
    tiempoPromedioRedSocial.append(df[column].mean())
  return tiempoPromedioRedSocial

@app.get("/redFavorita")
async def redFavorita(db: Session = Depends(get_database_session)):
  redSocialFavorita = ''
  redSocialMenosFavorita = ''
  red = db.query(Forms.redFavorita)
  df = pd.DataFrame(red)
  df.columns = ['redFavorita']
  redFavorita = df['redFavorita'].value_counts()
  redSocialFavorita = redFavorita.index[0]
  redSocialMenosFavorita = redFavorita.index[-1]
  return {'redSocialFavorita': redSocialFavorita,'redSocialMenosFavorita': redSocialMenosFavorita}

@app.get("/redMasUsada-edad")
async def redMasUsada(db: Session = Depends(get_database_session)):
  edades = ['1','2','3','4']
  df = pd.DataFrame()
  for edad in edades:
    tiempoEdad = db.query(
    func.sum(Forms.TiempoFacebook),
    func.sum(Forms.TiempoInstagram),
    func.sum(Forms.TiempoTikTok),
    func.sum(Forms.TiempoWhatsapp),
    func.sum(Forms.TiempoTwitter)).filter_by(edad = edad)
    timeEdad = pd.DataFrame(tiempoEdad)
    df = df.append(timeEdad,ignore_index=True)
  df.columns = [
    'TiempoFacebook','TiempoInstagram',
    'TiempoTikTok','TiempoWhatsapp','TiempoTwitter']
  tiempoRed = df.astype(float64).idxmax(axis=1)
  return {
    'rango1':tiempoRed[0],
    'rango2':tiempoRed[1],
    'rango3':tiempoRed[2],
    'rango4':tiempoRed[3]}

@app.post('/form')
async def receive_data(result: Encuesta,db: Session = Depends(get_database_session)):
	result_dict = result.dict()
	encuesta = Forms(id=result_dict['id'],email = result_dict['email'],edad = result_dict['edad'],sexo = result_dict['sexo'],redFavorita = result_dict['redFavorita'],TiempoFacebook = result_dict['TiempoFacebook'],TiempoInstagram = result_dict['TiempoInstagram'],TiempoTikTok = result_dict['TiempoTikTok'],TiempoWhatsapp = result_dict['TiempoWhatsapp'],TiempoTwitter = result_dict['TiempoTwitter'])
	db.add(encuesta)
	db.commit()
	db.refresh(encuesta)
	return result

