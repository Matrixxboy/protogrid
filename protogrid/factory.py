from typing import Any, Optional, Union
from .models import APIResponse, ErrorDetail, MetaData, PaginationMeta
from .status import APIStatus


def create_response(
    status: Union[APIStatus, str, int] = APIStatus.OK,
    message: Optional[str] = None,
    payload: Optional[Any] = None,
    error_details: Optional[Any] = None,
    include_meta: bool = True,
    request_id: Optional[str] = None,
    # Pagination args
    page: Optional[int] = None,
    limit: Optional[int] = None,
    total_items: Optional[int] = None,
) -> APIResponse:
    """
    Creates a standardized API response.
    """
    # Resolve status
    api_status = APIStatus.from_value(status)
    
    is_success = api_status.http_status < 400
    
    # Handle Pagination
    pagination = None
    if page is not None and limit is not None:
        total = total_items if total_items is not None else 0
        total_pages = (total + limit - 1) // limit if limit > 0 else 0
        
        pagination = PaginationMeta(
            page=page,
            limit=limit,
            total_items=total,
            total_pages=total_pages,
            has_next=page < total_pages,
            has_prev=page > 1
        )
    
    meta = None
    if include_meta:
        meta = MetaData()
        if request_id:
            meta.request_id = request_id

    error = None
    if not is_success:
        error = ErrorDetail(
            type=api_status.code,
            details=error_details
        )
    
    # Determine default message if not provided
    if message is None:
        message = api_status.code.replace("_", " ").title()

    return APIResponse(
        success=is_success,
        message=message,
        http_code=api_status.http_status,
        payload=payload if is_success else None,
        pagination=pagination,
        error=error,
        meta=meta
    )

# Alias for ease of use
make_response = create_response
