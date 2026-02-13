from typing import Any, Optional, Union
from .models import APIResponse, ErrorDetail, MetaData
from .status import APIStatus


def create_response(
    status: Union[APIStatus, str, int] = APIStatus.OK,
    message: Optional[str] = None,
    data: Optional[Any] = None,
    error_details: Optional[Any] = None,
    include_meta: bool = True,
    request_id: Optional[str] = None
) -> APIResponse:
    """
    Creates a standardized API response.
    
    Args:
        status: The APIStatus enum value, or a string ("ok", "200"), or int (200).
        message: Optional custom message. Defaults to status code name.
        data: The payload to return for success responses.
        error_details: Additional error information for failure responses.
        include_meta: Whether to include metadata (timestamp, request_id).
        request_id: Optional custom request ID.
        
    Returns:
        An APIResponse object.
    """
    # Resolve status
    api_status = APIStatus.from_value(status)
    
    is_success = api_status.http_status < 400
    
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
        data=data if is_success else None,
        error=error,
        meta=meta
    )

# Alias for ease of use
make_response = create_response
