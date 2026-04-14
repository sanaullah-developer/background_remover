from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from PIL import Image
import base64
import io
import time

from inference import remove_background

app = FastAPI()

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Serve UI
@app.get("/")
async def serve_ui():
    return FileResponse("index.html")

# ✅ API
@app.post("/remove-background")
async def remove_bg(file: UploadFile = File(...)):
    start = time.time()

    # Load image
    image = Image.open(file.file).convert("RGB")

    # 🔥 RESIZE (BIG SPEED BOOST)
    max_size = 640
    image.thumbnail((max_size, max_size))

    # Run inference
    output = remove_background(image)

    # Convert to base64
    buffer = io.BytesIO()
    output.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode()

    width, height = output.size

    return {
        "image_base64": f"data:image/png;base64,{img_str}",
        "width": width,
        "height": height,
        "time": round(time.time() - start, 2)
    }