# Protogrid

**Standardized, Type-Safe API Responses for Python.**

Protogrid is a lightweight library that enforces a consistent JSON structure for your API responses. It handles pagination math, error formatting, and metadata automatically.

## Quick Start

```python
from protogrid import make_response

# youre response data/payload
items_list = {
    "user_id": 123,
    "name": "Alice"
}

# Standard Response
return make_response(
    status=200, #or "ok" or APIStatus.OK 
    message="Manual Bad Request", #or None
    payload=items_list, #or None
    
    #only if you need pagination 
    page=1, #or None
    limit=10, #or None
    total_items=10, #or None
    include_meta=True, #or False (default: True) include request_id and timestamp
    error_details="Manual Bad Request" #default: None , used 
)
```

## Response Structure

```json
{
  "success": true,
  "message": "Manual Bad Request",
  "http_code": 200,
  "payload": {
    "user_id": 123,
    "name": "Alice"
  },
  "pagination": {
    "page": 1,
    "limit": 10,
    "total_items": 100,
    "total_pages": 10,
    "has_next": true,
    "has_prev": false
  },
  "error": null,
  "meta": {
    "timestamp": "2026-02-13T15:58:20.000Z",
    "request_id": "req_123e4567-e89b-12d3-a456-426614174000"
  }
}
```

## Why use Protogrid?

- ✅ **Consistent**: Always return the same JSON structure.
- ✅ **Lazy**: Don't manually calculate `total_pages` or `has_next` ever again.
- ✅ **Universal**: Works with FastAPI, Flask, Django, or scripts.

👉 **[Full Documentation & Source Code on GitHub](https://github.com/Matrixxboy/protogrid)**
