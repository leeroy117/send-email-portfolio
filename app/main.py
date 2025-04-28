import email
from typing import List, Optional, Union

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import BaseModel, EmailStr

app = FastAPI()

class EmailSchema(BaseModel):
    name: str
    email: Optional[str]
    phone: Optional[str]
    message: str

conf = ConnectionConfig(
    MAIL_USERNAME ="sukaritas19@gmail.com",
    MAIL_PASSWORD = "ypglzvhepdwrrjxp",
    MAIL_FROM = "sukaritas19@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

# html = """
# <h3>Nombre: ${name}</h3>
# <h3>Email: ${email}</h3>
# <br/>
# <p>Correo electronico: ${message}</p>
# """

@app.get("/")
async def read_root():
    return JSONResponse(status_code=200, content={"message": "ON :D"})

@app.post("/send-email")
async def send_email(emailBody: EmailSchema) -> JSONResponse:
    print("emial???????????????",emailBody.email)
    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=["leeroy.uziel.gg@outlook.es"],
        body=f"""<h2>Email: {emailBody.email}</h1>
                <h2>Name: {emailBody.name} </h2>
                <h2>Phone: {emailBody.phone} </h2>
                <p>Message: {emailBody.message} </p>
        """,
        subtype=MessageType.html)
    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"}) 

