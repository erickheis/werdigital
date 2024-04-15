from flask import Flask
from auth.auth import authorize

_CLIENT_URL = "https://werdigital-production.up.railway.app/"

app = Flask(__name__)
app.secret_key = ""

@app.route("/authorize")
def authorize_endpoint():
    auth_info = authorize()
    passthrough_val = auth_info["passthorugh_val"]
    session["passthrough_val"] = passthrough_val
    url = auth_info["authorization_url"]
    return redirect(url)

@app.route("/oauth2callback")
def oauth2callback_endpoint():
    passthrough_val = session["passthorugh_val"]
    state = request.args.get("state")
    code = request.args.get("code")
    oauth2callback(passthrough_val, state, code)
    return redirect(_CLIENT_URL)
    
