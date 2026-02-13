from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
import logging
import traceback

from api_response.integrations.response import make_response

# ---------------- Logging ----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

app = FastAPI()

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ======================================================
# ✅ HEALTH CHECK API (to check if server is running)
# ======================================================
@app.get("/health")
def health_check():
    return make_response(
        status=200,
        message="Server is running",
        data={"status": "OK"},
        include_meta=True
    )

# ======================================================
# ✅ TEST SUCCESS API
# ======================================================
@app.get("/success")
def success_api():
    return make_response(
        status=200,
        message="Success API working",
        data={"data": 123},
        include_meta=False
    )

# ======================================================
# ✅ TEST ERROR API (manual error trigger)
# ======================================================
@app.get("/error")
def error_api():
    raise HTTPException(status_code=400, detail="Manual Bad Request")

# ======================================================
# ✅ 404 NOT FOUND HANDLER
# ======================================================
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    logging.error(f"HTTP Error: {exc.detail}")

    return JSONResponse(
        status_code=exc.status_code,
        content=make_response(
            status=exc.status_code,
            message="HTTP Error",
            data=exc.detail,
            include_meta=False
        )
    )

# ======================================================
# ✅ VALIDATION ERROR HANDLER (422)
# ======================================================
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logging.error(f"Validation Error: {exc.errors()}")

    return JSONResponse(
        status_code=422,
        content=make_response(
            status=422,
            message="Validation Error",
            data=exc.errors(),
            include_meta=False
        )
    )

# ======================================================
# ✅ GLOBAL ERROR HANDLER (500)
# ======================================================
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logging.error(f"Unhandled Error: {str(exc)}")
    logging.error(traceback.format_exc())

    return JSONResponse(
        status_code=500,
        content=make_response(
            status=500,
            message="Internal Server Error",
            data=str(exc),
            include_meta=False
        )
    )
