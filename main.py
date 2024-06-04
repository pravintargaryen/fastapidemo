from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json

app = FastAPI()

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
