from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHttpException
from .endpoints import auth

# OpenAPI Labels
ALPHA = '&nbsp;&nbsp;<font color=\'red\'><strong>&lt;ALPHA/DO-NOT-USE&gt;</strong></font>'
BETA = '&nbsp;&nbsp;<font color=\'orange\'><strong>&lt;BETA&gt;</strong></font>'
STABLE = '&nbsp;&nbsp;<font color=\'green\'><strong>&lt;STABLE&gt;</strong></font>'
DOCS_TAG_METADATA = [{
    'name': 'auth',
    'description': 'User Authorization' + STABLE
}]

# Set basic information for api node
app = FastAPI(
    title='FastAPI Start Template',
    description='write your api docs description here',
    version='0.0.1',
    openapi_tags=DOCS_TAG_METADATA,
    openapi_url='/docs/openapi.json',
    docs_url='/docs/swagger',  # swagger is available on http://hostname:port/api/v1/docs/swagger
    redoc_url='/docs/redoc'  # redoc is available on http://hostname:port/api/v1/docs/swagger
)

# Assign routing to each api
# The 'tags' here refer to the value defined in 'DOCS_TAG_METADATA' above
app.include_router(auth.router, prefix='/auth', tags=['auth'])


# Override HTTP Exception Handler
@app.exception_handler(StarletteHttpException)
def override_http_exception(request, exc: StarletteHttpException):
    # The 'request' parameter cannot be omitted
    return JSONResponse(
        content={
            'status': exc.status_code,
            'msg': exc.detail
        },
        status_code=exc.status_code
    )


# Override Validation Error Exception Handler
@app.exception_handler(RequestValidationError)
def override_validation_error(request, exc: RequestValidationError):
    # The 'request' parameter cannot be omitted
    return JSONResponse(
        content={
            'status': 422,
            'msg': 'Incorrect data format!',
            'data': exc.errors()
        },
        status_code=422
    )
