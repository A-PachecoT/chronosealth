from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import uvicorn
import threading

app = FastAPI()


@app.get("/health")
async def health_check():
    # Implement your health check logic here
    # For example:
    return JSONResponse(content={"status": "healthy"}, status_code=200)


def run_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)


def start_health_check_server():
    thread = threading.Thread(target=run_server)
    thread.start()


# Start the FastAPI server in a separate thread
start_health_check_server()
