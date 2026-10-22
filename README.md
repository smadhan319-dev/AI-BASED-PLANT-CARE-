# AI PLANT CARE

## Option 1 — Free local plant disease classification (no API key)

This project includes a local FastAPI backend using the open-source Hugging Face model `neghani/plantvillage-mobilenetv2`. Local inference has no per-request API fee and does not require an OrcaRouter key. It is limited by your computer/server hardware and by the categories represented in the model; it is not guaranteed to identify every disease or give treatment advice.

### Requirements
- Python 3.10 or newer
- Internet on first run to download Python packages and model weights
- Enough RAM/CPU (PyTorch model loading may take several minutes; a GPU is optional)

### Start the local model server
1. Unzip the project.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment (recommended):
   - Windows: `py -m venv .venv` then `.venv\\Scripts\\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
4. Install dependencies: `python -m pip install -r requirements-local-ai.txt`
5. Start the server: `python -m uvicorn local_ai:app --host 127.0.0.1 --port 8000`
6. Keep the terminal open. The first start downloads the model.
7. Open `index.html` in a browser. In Settings, leave the OrcaRouter API key blank and set Local AI server URL to `http://127.0.0.1:8000`, then Save settings.
8. Go to Diagnose, choose a leaf image, and tap Diagnose now.

If the browser blocks local requests when opening `index.html` as a file, serve the static files from another terminal in the project folder with `python -m http.server 8080`, then open `http://localhost:8080`. Keep the AI server running on port 8000 too.

### Limitations
- The local classifier reports the top three class labels and model scores. A score is not a calibrated guarantee of diagnostic accuracy.
- PlantVillage-style models may perform poorly on field images, mixed symptoms, unusual crops, or diseases outside their training classes.
- Local inference has no API request quota, but your hardware has finite speed and memory. Cloud hosting may impose its own limits and costs.
- The local classifier does not generate treatment recommendations. Verify any diagnosis with a local agricultural extension service before applying pesticides.
- The CORS configuration is for local development. Restrict allowed origins before exposing this server to the public internet.

## Option 2 — Existing cloud AI

You can still enter an OrcaRouter API key in Settings. When a key is saved, photo diagnosis uses the cloud AI as before. Ask AI and Community expert answers continue to require a cloud API key.

Features: photo diagnosis, My crops tracker, Weather and spray advice, Disease library, Community Q&A, Ask AI, fertiliser and spray calculators, and 8 answer languages.
