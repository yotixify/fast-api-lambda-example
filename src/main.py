from fastapi import Depends, FastAPI, Response, status  # 👈 new imports
from fastapi.security import HTTPBearer
 
from .utils import VerifyToken 

from mangum import Mangum

app = FastAPI()

token_auth_scheme = HTTPBearer()

@app.get("/public")
async def root():
    return {"message": "This is a public route with no authenticatio needed."}


@app.get("/api/private")
def private(response: Response, token: str = Depends(token_auth_scheme)):  # 👈 updated code
    """A valid access token is required to access this route"""
 
    result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # 👇 new code
    if result.get("status"):
       response.status_code = status.HTTP_400_BAD_REQUEST
       return result
    # 👆 new code
 
    return result

handler = Mangum(app)