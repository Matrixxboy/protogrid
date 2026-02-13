from typing import Any, Optional
from .factory import create_response, APIStatus

def make_response(
    status: APIStatus = APIStatus.OK,
    message: Optional[str] = None,
    data: Optional[Any] = None,
    error_details: Optional[Any] = None,
    include_meta: bool = True,
    request_id: Optional[str] = None,
    headers: Optional[dict] = None
):
    
    response_obj = create_response(
        status=status,
        message=message,
        data=data,
        error_details=error_details,
        include_meta=include_meta,
        request_id=request_id
    )
    pure_res = response_obj.to_dict()
    return pure_res
