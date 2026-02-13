from typing import Any, Optional
from ..factory import create_response, APIStatus

def make_response(
    status: APIStatus = APIStatus.OK,
    message: Optional[str] = None,
    data: Optional[Any] = None,
    error_details: Optional[Any] = None,
    include_meta: bool = True,
    request_id: Optional[str] = None,
    headers: Optional[dict] = None,
    # Pagination args
    page: Optional[int] = None,
    limit: Optional[int] = None,
    total_items: Optional[int] = None,
):
    response_obj = create_response(
        status=status,
        message=message,
        data=data,
        error_details=error_details,
        include_meta=include_meta,
        request_id=request_id,
        page=page,
        limit=limit,
        total_items=total_items
    )
    
    return response_obj.to_dict()
