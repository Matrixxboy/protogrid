from typing import Any, Optional
from ..factory import create_response, APIStatus

try:
    from fastapi.responses import JSONResponse
except ImportError:
    JSONResponse = None

def make_response(
    status: APIStatus = APIStatus.OK,
    message: Optional[str] = None,
    data: Optional[Any] = None,
    error_details: Optional[Any] = None,
    include_meta: bool = True,
    request_id: Optional[str] = None,
    headers: Optional[dict] = None
):
    """Returns a FastAPI/Starlette JSONResponse."""
    if JSONResponse is None:
        raise ImportError("fastapi is not istalled. Use 'pip install fastapi' to use this integration.")
    
    response_obj = create_response(
        status=status,
        message=message,
        data=data,
        error_details=error_details,
        include_meta=include_meta,
        request_id=request_id
    )
    
    return JSONResponse(
        status_code=response_obj.http_code,
        content=response_obj.to_dict(),
        headers=headers
    )
