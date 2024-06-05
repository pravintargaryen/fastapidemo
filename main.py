from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Read the JSON file once at startup
with open('fcc_data.json', 'r') as json_file:
    combined_dict = json.load(json_file)

@app.get("/data", response_class=JSONResponse)
async def get_data():
    return combined_dict

# For individual record access
@app.get("/data/{record_id}", response_class=JSONResponse)
async def get_record(record_id: int):
    record = combined_dict.get(str(record_id))
    if record:
        return record
    return JSONResponse(status_code=404, content={"message": "Record not found"})

