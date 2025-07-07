from flask import Flask, render_template
import requests, datetime, os, threading, time

app = Flask(__name__)

# === CONFIGURATION ===
BOT_TOKEN = '7208069689:AAHVdxh9AUu9QJnfJkXI-wo_fP5iPUrovuo'
CHAT_ID = '931091155'
PHOTO_PATH = 'static/captured.jpg'
IP_WEBCAM_URL = 'http://192.168.1.11:5000/shot.jpg'  

# === Globals to show on dashboard ===
last_time = "N/A"
last_ip = "N/A"
last_location = "N/A"

# === Capture Photo from Mobile IP Camera ===
def capture_photo():
    try:
        r = requests.get(IP_WEBCAM_URL, timeout=5)
        if r.status_code == 200:
            with open(PHOTO_PATH, 'wb') as f:
                f.write(r.content)
        else:
            print("[❌] Failed to fetch image from IP cam.")
    except Exception as e:
        print("[ERROR] Capture failed:", e)

# === Get Public IP and Location ===
def get_ip_and_location():
    try:
        ip = requests.get("https://api.ipify.org").text
        geo = requests.get(f"https://ipinfo.io/{ip}/json").json()
        city = geo.get("city", "Unknown")
        country = geo.get("country", "Unknown")
        return ip, f"{city}, {country}"
    except:
        return "Unavailable", "Unknown"

# === Send to Telegram ===
def send_to_telegram(photo_path, message):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
        with open(photo_path, 'rb') as f:
            requests.post(url, files={'photo': f}, data={'chat_id': CHAT_ID, 'caption': message})
    except Exception as e:
        print("[ERROR] Telegram send failed:", e)

#Background Task: Capture Every 5 Seconds
def background_capture():
    global last_time, last_ip, last_location
    while True:
        try:
            capture_photo()
            ip, location = get_ip_and_location()
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            last_time = now
            last_ip = ip
            last_location = location

            msg = f"🔐 Auto-Capture Alert\n📅 {now}\n🌍 Location: {location}\n💻 IP: {ip}"
            send_to_telegram(PHOTO_PATH, msg)

            print(f"[✅] Captured & sent at {now}")
        except Exception as e:
            print("[⚠️] Error in background capture:", e)

        time.sleep(5) 

@app.route('/')
def home():
    return render_template('index.html', date=last_time, ip=last_ip, location=last_location)

# === Start Everything ===
if __name__ == '__main__':
    # Start capture thread
    threading.Thread(target=background_capture, daemon=True).start()
    
    # Run web server
    app.run(host='0.0.0.0', port=5000)
