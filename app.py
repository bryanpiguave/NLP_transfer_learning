from fastapi import FastAPI, Query
import numpy as np

app = FastAPI()

@app.get("/classify")
async def classify_prompt(prompt: str = Query(None)):
    # Your code to perform classification on the prompt
    classification = "Positive" if np.random.rand() > 0.5 else "Negative"
    return {"classification": classification}
