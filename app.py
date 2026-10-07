from fastapi import FastAPI
import uvicorn
from laya import Router 
import os
import time

os.environ["HF_HOME"] = os.path.expanduser("~/.cache/huggingface")
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# 1. Initialize and preload the model weights
router = Router()
router.preload() 

app = FastAPI(title='Laya Slop Detector')

# 2. Accept a structured JSON schema that matches our prediction keys
@app.post('/predict')
async def analyze(payload: dict):
    # Grab the text block passed from the Streamlit frontend
    state = payload.get("state", "")
    
    questions = {
        'isslop': {
            "type": 'noul',
            "instructions": "Is this text a generic, cliché AI-generated LinkedIn post?",  
        }
    }

    t0 = time.perf_counter()
    prediction = router.predict(state, questions)
    latency_ms = round((time.perf_counter() - t0),3)
    answer = prediction["answers"]["isslop"]

    p = answer["noul"]
    verdict = "🚨 AI SLOP" if p >= 0.5 else "🟢 HUMAN SIGNAL"
    confidence = answer["confidence"]

    # Return keys that map precisely to what your Streamlit UI expects
    return {
        'confidence': f"{round(confidence * 100, 1)}%",
        'slop_probability': f"{round(p * 100, 1)}%",
        'verdict': verdict,
        'latency':latency_ms
        #would be better to test latency if the model works on gpu currently its on cpu
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
