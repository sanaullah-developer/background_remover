from ultralytics import YOLO
import numpy as np
import cv2
from PIL import Image

# ✅ Load model ONCE
model = YOLO("model/best.pt")
model.to("cpu")

def remove_background(image):
    img = np.array(image)

    # 🔥 Faster inference (important)
    results = model(img, imgsz=640)[0]

    # If no person detected
    if results.masks is None or len(results.masks.data) == 0:
        return image

    masks = results.masks.data.cpu().numpy()

    # 🔥 Combine all masks efficiently
    combined_mask = np.max(masks, axis=0)

    # Resize mask to original image size
    combined_mask = cv2.resize(
        combined_mask,
        (img.shape[1], img.shape[0]),
        interpolation=cv2.INTER_NEAREST
    )

    # Convert to binary mask
    combined_mask = (combined_mask > 0.5).astype(np.uint8) * 255

    # Add alpha channel
    rgba = np.dstack((img, combined_mask))

    return Image.fromarray(rgba)