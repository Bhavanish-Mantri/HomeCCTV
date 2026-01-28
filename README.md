# HomeCCTV — Intrusion Detection System

**HomeCCTV** is a Python-based Intrusion Detection System that uses computer vision to monitor video feeds, detect motion, capture evidence, and alert you via Telegram. Built using OpenCV, Flask, and Telegram Bot API, it’s ideal for learning real-time video processing, web integration, and alert automation. :contentReference[oaicite:1]{index=1}

---

## 🚀 Features

✔ Real-time motion detection using OpenCV  
✔ Records and saves snapshots/clips when motion is detected  
✔ Telegram notification alerts with images/videos  
✔ Flask-based web dashboard for monitoring  
✔ Supports IP camera / mobile webcam feeds  
✔ Modular structure for customization

---

## 🛠 Technologies Used

- **Python** – core application logic  
- **OpenCV** – video capture and motion detection  
- **Flask** – lightweight web dashboard  
- **Telegram Bot API** – remote alerts  
- **ffmpeg** – video handling utilities

---

## 📁 Project Structure
```
HomeCCTV/
├── app.py ← Main application
├── static/ ← CSS, JS, assets
├── templates/ ← HTML interface pages
├── intrusions/ ← Saved motion clips & logs
├── .gitignore
└── README.md
```

---

## 📌 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Bhavanish-Mantri/HomeCCTV.git
   cd HomeCCTV
   
2. **Set Up Virtual Environment**

Create and activate a virtual environment to keep dependencies isolated.

```bash
python3 -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

3. **Install Dependencies**

Install all required Python packages:
```
pip install -r requirements.txt
```
---

## ⚙ Configuration

### Telegram Bot Setup

1. Create a Telegram bot using **BotFather**
2. Copy and save your **Bot Token**
3. Get your **Chat ID** (user or group where alerts will be sent)

### Update `app.py`

Add your Telegram credentials:

```python
TELEGRAM_BOT_TOKEN = "<your-bot-token>"
CHAT_ID = "<your-chat-id>"
```

---

## ▶ Run the System

Start the HomeCCTV application:
```
python app.py
```

---

## 🕹 Usage

| Action | Description |
|------|------------|
| Access Web UI | http://localhost:5000 |
| Start Monitoring | Run `app.py` |
| View Intrusion Logs | Check `intrusions/` directory |

---

## 📸 How It Works

- The system continuously captures frames from a webcam or IP camera.
- Motion detection is performed by comparing frame differences using OpenCV.
- When motion is detected:
  - A snapshot or video clip is saved locally.
  - A Telegram alert is sent with the captured evidence.
- Live feed and intrusion logs can be viewed via the Flask web dashboard.

---

## 🧠 Ethical Use

This project is intended **strictly for educational and ethical purposes**.  
Do not use it for unauthorized surveillance or privacy invasion.  
Always comply with local laws and regulations when deploying monitoring systems.

---

## 🧩 Contributing

Contributions are welcome 🎉  
If you discover bugs, have feature ideas, or want to improve documentation:

- Open an issue  
- Submit a pull request  

---

## 📜 License

MIT License © 2026

