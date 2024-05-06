SERVER_URL = "https://flask-production-81a2.up.railway.app";

function handleLogin(response) {
    console.log("response from login:", response);
    localStorage.setItem("token", response.credential);
}

function onLinkAdsAcount() {
    //token = localStorage.getItem("token")
    //window.location.href = `${SERVER_URL}/authorize?token=${token}`;

    const token = localStorage.getItem("token");
    if (token) {
        window.location.href = `${SERVER_URL}/authorize?token=${encodeURIComponent(token)}`;
    } else {
        console.error("Token not found in localStorage.");
    }
}