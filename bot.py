from flask import Flask, request, jsonify
import json
import requests
import os

app = Flask(name)

# --- CONFIG ---
BOT_TOKEN = "8315094748:AAGMHP53CqdDipmFFZmfzGfDhvx1YcBWl78"
CHAT_ID = "5745825285"  # admin group or personal ID
USERS_FILE = "users.json"

# --- Load Users Data ---
def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# --- Save Users Data ---
def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

# --- Verify VIP Key ---
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    vip_key = data.get("vip_key", "").strip()
    user_id = data.get("user_id", "").strip()

    users = load_users()
    for user in users:
        if user["vip_key"] == vip_key:
            return jsonify({"status": "ok", "message": "Login successful"})
    
    return jsonify({"status": "error", "message": "Invalid VIP Key"}), 401

# --- Send Command to Telegram ---
@app.route("/send", methods=["POST"])
def send_command():
    data = request.get_json()
    command = data.get("command", "").strip()

    if not command:
        return jsonify({"status": "error", "message": "No command provided"}), 400

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": command
    }
    r = requests.post(url, json=payload)

    if r.status_code == 200:
        return jsonify({"status": "ok", "message": "Command sent successfully"})
    else:
        return jsonify({"status": "error", "message": "Failed to send command"}), 500

# --- Add new user (optional admin endpoint) ---
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    vip_key = data.get("vip_key", "").strip()
    user_id = data.get("user_id", "").strip()

    if not vip_key or not user_id:
        return jsonify({"status": "error", "message": "Missing vip_key or user_id"}), 400

    users = load_users()
    users.append({"vip_key": vip_key, "user_id": user_id})
    save_users(users)

    return jsonify({"status": "ok", "message": "User added"})

if name == "main":
    app.run(host="0.0.0.0", port=5000)