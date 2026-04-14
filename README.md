---

title: CutOut — AI Background Remover
emoji: ✂️
colorFrom: indigo
colorTo: purple
sdk: docker
pinned: true
short_description: Remove image backgrounds instantly using AI
license: apache-2.0
-------------------

# ✂️ CutOut — AI Background Remover

A fast, modern web application that removes image backgrounds using a custom-trained YOLO segmentation model. Upload an image with a person and instantly get a clean cutout with a transparent background.

---

## 🚀 Live Demo

👉 https://huggingface.co/spaces/sanaullahafd07/bg_remover

---

## ✨ Features

* 🧠 Accurate person segmentation using YOLO
* ⚡ Optimized for fast CPU inference
* 🎨 Clean and modern user interface
* 🖼️ Transparent PNG output
* 📥 One-click download

---

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **Model:** YOLO (Ultralytics)
* **Image Processing:** OpenCV, PIL
* **Frontend:** HTML, CSS, JavaScript
* **Deployment:** Docker on Hugging Face Spaces

---

## 📂 Project Structure

```
.
├── app.py
├── inference.py
├── index.html
├── Dockerfile
├── requirements.txt
└── model/
    └── best.pt
```

---

## ⚙️ How It Works

1. Upload an image
2. Image is resized for faster processing
3. YOLO model detects and segments the person
4. Mask is converted into an alpha channel
5. Output image is returned with a transparent background

---

## 🧪 Run Locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

---

## ⚡ Performance

* Optimized for CPU environments
* Typical processing time: **2–4 seconds per image**

---

## 🌐 Deployment

This project is deployed using Docker on Hugging Face Spaces.

---

## 👨‍💻 Author

**Sanaullah Afridi**
| AI Developer| Computer Vision Enthusiast
---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ or sharing it.

---
