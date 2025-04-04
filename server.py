from flask import Flask
import logging

app = Flask(__name__)

# ✅ Logging Setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    return "Bot is alive!", 200

# ✅ Start Web Server Function
def start_server():
    logger.info("🌐 Starting Web Server on port 8080...")
    app.run(host="0.0.0.0", port=8080, threaded=True)

if __name__ == "__main__":
    start_server()
