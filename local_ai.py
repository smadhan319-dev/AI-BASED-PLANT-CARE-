"""Local PlantVillage image-classification API for AI PLANT CARE.
Run: uvicorn local_ai:app --host 127.0.0.1 --port 8000
"""
from io import BytesIO
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image, UnidentifiedImageError
from transformers import pipeline

MODEL_ID = "neghani/plantvillage-mobilenetv2"
app = FastAPI(title="AI Plant Care - Local Disease Classifier")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Local development only; restrict this for public deployments.
    allow_credentials=False,
    allow_methods=["POST", "GET", "OPTIONS"],
    allow_headers=["*"],
)
classifier = None

@app.on_event("startup")
def load_model():
    global classifier
    classifier = pipeline("image-classification", model=MODEL_ID)

@app.get("/")
def health():
    return {"status": "ok", "model": MODEL_ID}

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=415, detail="Upload a JPG, PNG, or other image file.")
    raw = await file.read()
    if not raw or len(raw) > 10 * 1024 * 1024:
        raise HTTPException(status_code=413, detail="Image is empty or larger than 10 MB.")
    try:
        image = Image.open(BytesIO(raw)).convert("RGB")
    except (UnidentifiedImageError, OSError):
        raise HTTPException(status_code=400, detail="Could not read the image. Try a JPG or PNG.")
    try:
        predictions = classifier(image, top_k=3)
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Model prediction failed. Check server logs.") from exc
    return {"model": MODEL_ID, "predictions": predictions}
