SERVER_URL = "https://flask-production-81a2.up.railway.app";

function handleLogin(response) {
    localStorage.setItem("token", response.credential);
}

function onLinkAdsAcount() {
    token = localStorage.getItem("token")
    window.location.href = `${SERVER_URL}/authorize?token=${token}`;
}