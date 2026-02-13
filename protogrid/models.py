from dataclasses import dataclass, field, asdict
from datetime import datetime
import uuid
from typing import Any, Optional, Generic, TypeVar, Dict

T = TypeVar("T")

@dataclass
class MetaData:
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    request_id: str = field(default_factory=lambda: f"req_{uuid.uuid4().hex[:12]}")

@dataclass
class ErrorDetail:
    type: str
    details: Optional[Any] = None

@dataclass
class PaginationMeta:
    page: int
    limit: int
    total_items: int
    total_pages: int
    has_next: bool
    has_prev: bool

@dataclass
class APIResponse(Generic[T]):
    success: bool
    message: str
    http_code: int
    payload: Optional[T] = None
    pagination: Optional[PaginationMeta] = None
    error: Optional[ErrorDetail] = None
    meta: Optional[MetaData] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert the response to a dictionary, removing None values for cleaner output."""
        return {k: v for k, v in asdict(self).items() if v is not None}
