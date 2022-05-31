from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHttpException

# Import api node
from app.api import api_v1
from app.core.database import engine, Base

# Database auto initialize
Base.metadata.create_all(bind=engine)

# Set basic information and disable docs for root node
server = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)


# Override HTTP Exception Handler
@server.exception_handler(StarletteHttpException)
def override_http_exception(request, exc: StarletteHttpException):
    # The 'request' parameter cannot be omitted
    return JSONResponse(
        content={
            "status": exc.status_code,
            "msg": exc.detail
        },
        status_code=exc.status_code
    )


# CORS Configuration *Uncomment when needed*
# origins = [
#     "*"
# ]
#
# server.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )

# Assign routing to each api node
server.mount("/api/v1", api_v1.app)
