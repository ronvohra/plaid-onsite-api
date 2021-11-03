import uvicorn
from app.core.application import create_api

api = create_api()


if __name__ == "__main__":
    uvicorn.run(api, host="0.0.0.0", port=8000)
