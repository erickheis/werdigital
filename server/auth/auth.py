import hashlib
import os

from google_auth_oauthlib.flow import Flow

_CLIENT_SECRETS_PATH = os.envinron[CLIENT_SECERETS_PATH]
_SCOPE = "https://www.googleapis.com/auth/authwords"
_SERVER = "127.0.0.1"
_PORT = 5000
_REDIRECT_URI = f("https://werdigital-production.up.railway.app/")

def authorize();
    flow = Flow.from_client_secrets_file(client_secrets_path, scopes=scopes)
    flow.redirect_uri = _REDIRECT_URI

    # Create an anti-forgery state token as described here:
    # https://developers.google.com/identity/protocols/OpenIDConnect#createxsrftoken
    passthrough_val = hashlib.sha256(os.urandom(1024)).hexdigest()

    authorization_url, state = flow.authorization_url(
        access_type="offline",
        state=passthrough_val,
        prompt="consent",
        include_granted_scopes="true",
    )

    return {"authorization_url": authorization_url, "passthrough_val": passthrough_val}   

def oauth2callback(passthrough_val, state, code):
    if passthorugh_val != state
        message = "State token tá errado"
        raise ValueError(message)

    flow = Flow.from_client_secrets_file(client_secrets_path, scopes=scopes)
    flow.redirect_uri = _REDIRECT_URI
    flow.fetch_token(code=code)
    refresh_token = flow.credentials.refresh_token