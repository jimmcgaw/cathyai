from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse, FileResponse

from fastapi.staticfiles import StaticFiles
from authlib.integrations.starlette_client import OAuth
from starlette.config import Config
from datetime import datetime, timedelta
from jose import jwt

from pathlib import Path

config = Config(".env")

GOOGLE_CLIENT_ID = config("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = config("GOOGLE_CLIENT_SECRET")

APP_JWT_PRIVATE_KEY_PATH = config("APP_JWT_PRIVATE_KEY_PATH", default="/app/private_key.pem")
APP_JWT_ISSUER = config("APP_JWT_ISSUER", default="app-jwt-key")
APP_JWT_ALG = config("APP_JWT_ALG", default="RS256")
APP_JWT_EXP_HOURS = int(config("APP_JWT_EXP_HOURS", default=1))

# Load RSA private key
private_key_pem = Path(APP_JWT_PRIVATE_KEY_PATH).read_text(encoding="utf-8")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/root")
async def index():
    return FileResponse("static/index.html", media_type="text/html", status_code=200, headers={"Cache-Control": "no-cache"}, content_disposition_type="inline")

oauth = OAuth(config)
oauth.register(
    name="google",
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)


@app.get("/login/google")
async def login_via_google(request: Request):
    redirect_uri = request.url_for("auth_google_callback")
    return await oauth.google.authorize_redirect(request, redirect_uri)


@app.get("/auth/google/callback")
async def auth_google_callback(request: Request):
    token = await oauth.google.authorize_access_token(request)
    userinfo = token.get("userinfo")
    if not userinfo:
        raise HTTPException(status_code=400, detail="Failed to retrieve user info")

    now = datetime.now(datetime.timezone.utc)
    payload = {
        "iss": APP_JWT_ISSUER,  # must match Kong jwt_secret.key
        "sub": userinfo["email"],
        "name": userinfo.get("name"),
        "exp": now + timedelta(hours=APP_JWT_EXP_HOURS),
        "iat": now,
    }

    app_jwt = jwt.encode(
        payload,
        private_key_pem,
        algorithm=APP_JWT_ALG,  # "RS256"
    )

    # For demo, just return token
    return {"access_token": app_jwt, "token_type": "bearer"}


@app.get("/api/me")
async def read_me():
    # Kong has already validated JWT if you're here.
    return {"message": "Kong RS256-validated request reached FastAPI"}
