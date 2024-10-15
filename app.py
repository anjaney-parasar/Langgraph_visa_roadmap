
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from roadmap_generator import graph_app

app = FastAPI()
# Define Pydantic model for request body
class QuestionnaireRequest(BaseModel):
    questionnaire: str

# Define API endpoint
@app.post("/generate_roadmap")
async def generate_visa_roadmap(request: QuestionnaireRequest):
    try:
        result = graph_app.invoke({"questionnaire": request.questionnaire})
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,  port=8000)