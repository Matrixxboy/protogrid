from enum import Enum
from http import HTTPStatus
from typing import Union

class APIStatus(Enum):
    # 1xx Informational
    CONTINUE = ("continue", HTTPStatus.CONTINUE)
    SWITCHING_PROTOCOLS = ("switching_protocols", HTTPStatus.SWITCHING_PROTOCOLS)
    PROCESSING = ("processing", HTTPStatus.PROCESSING)
    EARLY_HINTS = ("early_hints", HTTPStatus.EARLY_HINTS)
    
    # 2xx Success
    OK = ("ok", HTTPStatus.OK)
    CREATED = ("created", HTTPStatus.CREATED)
    ACCEPTED = ("accepted", HTTPStatus.ACCEPTED)
    NON_AUTHORITATIVE_INFORMATION = ("non_authoritative_information", HTTPStatus.NON_AUTHORITATIVE_INFORMATION)
    NO_CONTENT = ("no_content", HTTPStatus.NO_CONTENT)
    RESET_CONTENT = ("reset_content", HTTPStatus.RESET_CONTENT)
    PARTIAL_CONTENT = ("partial_content", HTTPStatus.PARTIAL_CONTENT)
    MULTI_STATUS = ("multi_status", HTTPStatus.MULTI_STATUS)
    ALREADY_REPORTED = ("already_reported", HTTPStatus.ALREADY_REPORTED)
    IM_USED = ("im_used", HTTPStatus.IM_USED)
    
    # 3xx Redirection
    MULTIPLE_CHOICES = ("multiple_choices", HTTPStatus.MULTIPLE_CHOICES)
    MOVED_PERMANENTLY = ("moved_permanently", HTTPStatus.MOVED_PERMANENTLY)
    FOUND = ("found", HTTPStatus.FOUND)
    SEE_OTHER = ("see_other", HTTPStatus.SEE_OTHER)
    NOT_MODIFIED = ("not_modified", HTTPStatus.NOT_MODIFIED)
    USE_PROXY = ("use_proxy", HTTPStatus.USE_PROXY)
    TEMPORARY_REDIRECT = ("temporary_redirect", HTTPStatus.TEMPORARY_REDIRECT)
    PERMANENT_REDIRECT = ("permanent_redirect", HTTPStatus.PERMANENT_REDIRECT)
    
    # 4xx Client Error
    BAD_REQUEST = ("bad_request", HTTPStatus.BAD_REQUEST)
    UNAUTHORIZED = ("unauthorized", HTTPStatus.UNAUTHORIZED)
    PAYMENT_REQUIRED = ("payment_required", HTTPStatus.PAYMENT_REQUIRED)
    FORBIDDEN = ("forbidden", HTTPStatus.FORBIDDEN)
    NOT_FOUND = ("not_found", HTTPStatus.NOT_FOUND)
    METHOD_NOT_ALLOWED = ("method_not_allowed", HTTPStatus.METHOD_NOT_ALLOWED)
    NOT_ACCEPTABLE = ("not_acceptable", HTTPStatus.NOT_ACCEPTABLE)
    PROXY_AUTHENTICATION_REQUIRED = ("proxy_authentication_required", HTTPStatus.PROXY_AUTHENTICATION_REQUIRED)
    REQUEST_TIMEOUT = ("request_timeout", HTTPStatus.REQUEST_TIMEOUT)
    CONFLICT = ("conflict", HTTPStatus.CONFLICT)
    GONE = ("gone", HTTPStatus.GONE)
    LENGTH_REQUIRED = ("length_required", HTTPStatus.LENGTH_REQUIRED)
    PRECONDITION_FAILED = ("precondition_failed", HTTPStatus.PRECONDITION_FAILED)
    PAYLOAD_TOO_LARGE = ("payload_too_large", HTTPStatus.PAYLOAD_TOO_LARGE)
    URI_TOO_LONG = ("uri_too_long", HTTPStatus.URI_TOO_LONG)
    UNSUPPORTED_MEDIA_TYPE = ("unsupported_media_type", HTTPStatus.UNSUPPORTED_MEDIA_TYPE)
    RANGE_NOT_SATISFIABLE = ("range_not_satisfiable", HTTPStatus.RANGE_NOT_SATISFIABLE)
    EXPECTATION_FAILED = ("expectation_failed", HTTPStatus.EXPECTATION_FAILED)
    IM_A_TEAPOT = ("im_a_teapot", HTTPStatus.IM_A_TEAPOT)
    MISDIRECTED_REQUEST = ("misdirected_request", HTTPStatus.MISDIRECTED_REQUEST)
    UNPROCESSABLE_ENTITY = ("unprocessable_entity", HTTPStatus.UNPROCESSABLE_ENTITY)
    LOCKED = ("locked", HTTPStatus.LOCKED)
    FAILED_DEPENDENCY = ("failed_dependency", HTTPStatus.FAILED_DEPENDENCY)
    TOO_EARLY = ("too_early", HTTPStatus.TOO_EARLY)
    UPGRADE_REQUIRED = ("upgrade_required", HTTPStatus.UPGRADE_REQUIRED)
    PRECONDITION_REQUIRED = ("precondition_required", HTTPStatus.PRECONDITION_REQUIRED)
    TOO_MANY_REQUESTS = ("too_many_requests", HTTPStatus.TOO_MANY_REQUESTS)
    REQUEST_HEADER_FIELDS_TOO_LARGE = ("request_header_fields_too_large", HTTPStatus.REQUEST_HEADER_FIELDS_TOO_LARGE)
    UNAVAILABLE_FOR_LEGAL_REASONS = ("unavailable_for_legal_reasons", HTTPStatus.UNAVAILABLE_FOR_LEGAL_REASONS)
    
    # 5xx Server Error
    INTERNAL_SERVER_ERROR = ("internal_server_error", HTTPStatus.INTERNAL_SERVER_ERROR)
    NOT_IMPLEMENTED = ("not_implemented", HTTPStatus.NOT_IMPLEMENTED)
    BAD_GATEWAY = ("bad_gateway", HTTPStatus.BAD_GATEWAY)
    SERVICE_UNAVAILABLE = ("service_unavailable", HTTPStatus.SERVICE_UNAVAILABLE)
    GATEWAY_TIMEOUT = ("gateway_timeout", HTTPStatus.GATEWAY_TIMEOUT)
    HTTP_VERSION_NOT_SUPPORTED = ("http_version_not_supported", HTTPStatus.HTTP_VERSION_NOT_SUPPORTED)
    VARIANT_ALSO_NEGOTIATES = ("variant_also_negotiates", HTTPStatus.VARIANT_ALSO_NEGOTIATES)
    INSUFFICIENT_STORAGE = ("insufficient_storage", HTTPStatus.INSUFFICIENT_STORAGE)
    LOOP_DETECTED = ("loop_detected", HTTPStatus.LOOP_DETECTED)
    NOT_EXTENDED = ("not_extended", HTTPStatus.NOT_EXTENDED)
    NETWORK_AUTHENTICATION_REQUIRED = ("network_authentication_required", HTTPStatus.NETWORK_AUTHENTICATION_REQUIRED)
    
    

    @property
    def code(self) -> str:
        return self.value[0]

    @property
    def http_status(self) -> int:
        return self.value[1].value

    @classmethod
    def from_value(cls, value: Union[str, int, 'APIStatus']) -> 'APIStatus':
        if isinstance(value, cls):
            return value
        
        if isinstance(value, int):
            # Try to match by HTTP status code
            for status in cls:
                if status.http_status == value:
                    return status
            # Fallback for unknown int codes (default to INTERNAL_SERVER_ERROR or custom handling could be added)
            # For now, if we can't map it, we might return a generic error or raise.
            # Let's default to OK if 200-299, else Error.
            if 200 <= value < 300:
                return cls.OK
            return cls.INTERNAL_SERVER_ERROR

        if isinstance(value, str):
            value_lower = value.lower()
            # Try to match by code string ("ok", "not_found")
            for status in cls:
                if status.code == value_lower:
                    return status
            # Try to match by Enum name ("OK", "NOT_FOUND")
            try:
                return cls[value.upper()]
            except KeyError:
                pass
            
            # Try to match if user passed string number "200"
            if value.isdigit():
                return cls.from_value(int(value))

        # Default fallback
        return cls.INTERNAL_SERVER_ERROR
