# Protogrid
![PyPI](https://img.shields.io/pypi/v/protogrid)
![Python](https://img.shields.io/pypi/pyversions/protogrid)
![License](https://img.shields.io/pypi/l/protogrid)
![Status](https://img.shields.io/pypi/status/protogrid)

**The Standardized API Response Library for Python.**

Protogrid is a lightweight, zero-dependency library designed to standardize API responses across your Python web services. Whether you use **FastAPI**, **Flask**, or raw Python scripts, Protogrid ensures your API responses are consistent, predictable, and professional.

## 🚀 Features

- **Standardized JSON Structure**: Every response follows a strict schema: `success`, `message`, `data`, `pagination`, `error`, `meta`.
- **Automatic Pagination**: Pass `page`, `limit`, and `total_items`, and Protogrid handles the metadata calculation for you.
- **Zero Dependencies**: Built purely on the Python standard library (`dataclasses`, `enum`, `http`).
- **Framework Agnostic**: Works out-of-the-box with any Python web framework.
- **Type-Safe**: Fully typed for modern Python development.

## 📦 Installation

```bash
pip install protogrid
```

## 🛠 Usage

### 1. Basic Success Response

```python
from protogrid import make_response

# Simple data return
response = make_response(
    payload={"user_id": 123, "name": "Alice"},
    message="User retrieved successfully"
)

# Output:
# {
#   "success": true,
#   "message": "User retrieved successfully",
#   "http_code": 200,
#   "payload": {"user_id": 123, "name": "Alice"},
#   "pagination": null,
#   "error": null,
#   "meta": { ... }
# }
```

### 2. Automatic Pagination

Stop calculating `total_pages` manually. Just feed Protogrid your data and counts.

```python
users_list = [...] # Your logic to get data
total_count = 100

return make_response(
    payload=users_list,
    page=1,
    limit=10,
    total_items=total_count
)
```

**Output:**

```json
{
  "success": true,
  "payload": [ ... ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total_items": 100,
    "total_pages": 10,
    "has_next": true,
    "has_prev": false
  }
}
```

### 3. Error Handling

Protogrid makes error responses consistent.

```python
# specific status code
return make_response(
    status=404,
    message="User not found",
    error_details={"id": "123 is invalid"}
)
```

## 📚 API Reference

### `make_response(...)`

| Argument        | Type                          | Default | Description                                                         |
| :-------------- | :---------------------------- | :------ | :------------------------------------------------------------------ |
| `status`        | `int` \| `str` \| `APIStatus` | `200`   | HTTP status code (e.g., `200`, `404`, `"ok"`, `"bad_request"`).     |
| `message`       | `str`                         | `None`  | Custom message. Defaults to the status code description if omitted. |
| `payload`       | `Any`                         | `None`  | The main data content of your response.                             |
| `error_details` | `Any`                         | `None`  | Detailed error info (e.g., validation errors, stake trace).         |
| `page`          | `int`                         | `None`  | Current page number (for pagination).                               |
| `limit`         | `int`                         | `None`  | Items per page (for pagination).                                    |
| `total_items`   | `int`                         | `None`  | Total number of items in the database (for pagination).             |
| `include_meta`  | `bool`                        | `True`  | Whether to include metadata like timestamps.                        |
| `request_id`    | `str`                         | `None`  | A unique request ID for tracing.                                    |


# ALL API Status Codes

### 1. 1xx Informational

| Status Code |Status as string| Status Name | Description |
| :--- | :--- | :--- | :--- |
| 100 | "continue" | Continue | The server has received the request headers and the client should proceed to send the request body. |
| 101 | "switching_protocols" | Switching Protocols | The server understands and is willing to comply with the client's request, for example, as a result of an Upgrade header. |
| 102 | "processing" | Processing | The server has received and is processing the request, but no response is available yet. |
| 103 | "early_hints" | Early Hints | The server is sending early hints to the client, such as link headers, to improve the loading performance of the page. |

## 2. 2xx Success

| Status Code |Status as string| Status Name | Description |
| :--- | :--- | :--- | :--- |
| 200 | "ok" | OK | The request has succeeded. |
| 201 | "created" | Created | The request has been fulfilled and resulted in a new resource being created. |
| 202 | "accepted" | Accepted | The request has been accepted for processing, but the processing has not been completed. |
| 204 | "no_content" | No Content | The server successfully processed the request and is not returning any content. |
| 205 | "reset_content" | Reset Content | The server successfully processed the request, but is not returning any content. |
| 206 | "partial_content" | Partial Content | The server successfully processed the request and is returning a partial response. |
| 207 | "multi_status" | Multi-Status | The server has received and is processing multiple requests, but no response is available yet. |
| 208 | "already_reported" | Already Reported | The server has received and is processing multiple requests, but no response is available yet. |
| 226 | "im_used" | IM Used | The server has received and is processing multiple requests, but no response is available yet. |


### 3. 3xx Redirection

| Status Code |Status as string| Status Name | Description |
| :--- | :--- | :--- | :--- |
| 300 | "multiple_choices" | Multiple Choices | The server is temporarily redirecting the client to a different URL. |
| 301 | "moved_permanently" | Moved Permanently | The requested resource has been permanently moved to a new URL. |
| 302 | "found" | Found | The requested resource has been temporarily moved to a new URL. |
| 304 | "not_modified" | Not Modified | The client can continue using the cached version of the resource. |
| 307 | "temporary_redirect" | Temporary Redirect | The server is temporarily redirecting the client to a different URL. |
| 308 | "permanent_redirect" | Permanent Redirect | The server is permanently redirecting the client to a different URL. |

### 4. 4xx Client Error

| Status Code |Status as string| Status Name | Description |
| :--- | :--- | :---| :--- |
| 400 | "bad_request" | Bad Request | The request could not be understood or was invalid. |
| 401 | "unauthorized" | Unauthorized | The request has not been applied because it lacks valid authentication credentials for the target resource. |
| 403 | "forbidden" | Forbidden | The server understood the request but refuses to authorize it. |
| 404 | "not_found" | Not Found | The server cannot find the requested resource. |
| 405 | "method_not_allowed" | Method Not Allowed | The request method is known by the server but has been intentionally disabled. |
| 409 | "conflict" | Conflict | The request could not be completed due to a conflict with the current state of the target resource. |
| 410 | "gone" | Gone | The requested resource is no longer available and will not be available again. |
| 411 | "length_required" | Length Required | The server refuses to accept the request without a defined Content-Length. |
| 412 | "precondition_failed" | Precondition Failed | The server does not meet one of the preconditions that the requester put on the later request. |
| 413 | "payload_too_large" | Payload Too Large | The server refuses to process a request because its payload is too large. |
| 414 | "uri_too_long" | URI Too Long | The server refuses to process a request because its URI is too long. |
| 415 | "unsupported_media_type" | Unsupported Media Type | The server refuses to process a request because its media type is not supported. |
| 416 | "range_not_satisfiable" | Range Not Satisfiable | The server refuses to process a request because its range is not satisfiable. |
| 417 | "expectation_failed" | Expectation Failed | The server does not meet one of the expectations that the requester put on the later request. |
| 418 | "im_a_teapot" | I'm a teapot | The server refuses to process a request because it is a teapot. |
| 421 | "misdirected_request" | Misdirected Request | The server cannot produce a response that matches the set of values of the request's content negotiation headers. |
| 422 | "unprocessable_entity" | Unprocessable Entity | The server understands the content type of the request entity, and the syntax of the request entity is correct, but it was unable to process the contained instructions. |
| 423 | "locked" | Locked | The resource that is being accessed is locked. |
| 424 | "failed_dependency" | Failed Dependency | The request failed because it depended on another request that failed. |
| 425 | "too_early" | Too Early | The server refuses to process a request because it is too early. |
| 426 | "upgrade_required" | Upgrade Required | The server refuses to process a request because it is too early. |
| 428 | "precondition_required" | Precondition Required | The server requires the request to have a precondition that the requester has not provided. |
| 429 | "too_many_requests" | Too Many Requests | The user has sent too many requests in a given amount of time. |
| 431 | "request_header_fields_too_large" | Request Header Fields Too Large | The server refuses to process a request because its header fields are too large. |
| 451 | "unavailable_for_legal_reasons" | Unavailable For Legal Reasons | The server refuses to process a request because it is legally required to do so. |

### 5. 5xx Server Error

| Status Code | Status as string| Status Name | Description |
| :--- | :--- | :--- | :--- |
| 500 | "internal_server_error" | Internal Server Error | The server encountered an unexpected condition that prevented it from fulfilling the request. |
| 501 | "not_implemented" | Not Implemented | The server does not support the functionality required to fulfill the request. |
| 502 | "bad_gateway" | Bad Gateway | The server, while acting as a gateway or proxy, received an invalid response from an upstream server. |
| 503 | "service_unavailable" | Service Unavailable | The server is not ready to handle the request. |
| 504 | "gateway_timeout" | Gateway Timeout | The server, while acting as a gateway or proxy, did not receive a timely response from an upstream server. |
| 505 | "http_version_not_supported" | HTTP Version Not Supported | The server does not support the HTTP protocol version used in the request. |
| 506 | "variant_also_negotiates" | Variant Also Negotiates | The server has an internal configuration error. |
| 507 | "insufficient_storage" | Insufficient Storage | The server is unable to store the representation of the resource. |
| 508 | "loop_detected" | Loop Detected | The server detected an infinite loop while processing the request. |
| 510 | "not_extended" | Not Extended | The server requires additional extensions to the request to fulfill it. |
| 511 | "network_authentication_required" | Network Authentication Required | The client needs to authenticate to gain network access. |




## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## 📄 License

MIT License.
