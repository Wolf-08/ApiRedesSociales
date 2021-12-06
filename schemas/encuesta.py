from pydantic import BaseModel

class Encuesta(BaseModel):
	id: int
	email: str
	edad: str
	sexo: str
	redFavorita: str
	TiempoFacebook: int
	TiempoInstagram: int
	TiempoTikTok: int
	TiempoWhatsapp: int
	TiempoTwitter: int