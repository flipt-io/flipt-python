# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_headers import remove_none_from_headers
from ...environment import FliptApiEnvironment
from .types.constraint import Constraint
from .types.constraint_create_request import ConstraintCreateRequest
from .types.constraint_update_request import ConstraintUpdateRequest


class ConstraintsClient:
    def __init__(
        self, *, environment: FliptApiEnvironment = FliptApiEnvironment.PRODUCTION, token: typing.Optional[str] = None
    ):
        self._environment = environment
        self._token = token

    def create(self, namespace_key: str, segment_key: str, *, request: ConstraintCreateRequest) -> Constraint:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._environment.value}/", f"api/v1/namespaces/{namespace_key}/segments/{segment_key}/constraints"
            ),
            json=jsonable_encoder(request),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Constraint, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, namespace_key: str, segment_key: str, id: str) -> None:
        _response = httpx.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._environment.value}/",
                f"api/v1/namespaces/{namespace_key}/segments/{segment_key}/constraints/{id}",
            ),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(self, namespace_key: str, segment_key: str, id: str, *, request: ConstraintUpdateRequest) -> None:
        _response = httpx.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._environment.value}/",
                f"api/v1/namespaces/{namespace_key}/segments/{segment_key}/constraints/{id}",
            ),
            json=jsonable_encoder(request),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncConstraintsClient:
    def __init__(
        self, *, environment: FliptApiEnvironment = FliptApiEnvironment.PRODUCTION, token: typing.Optional[str] = None
    ):
        self._environment = environment
        self._token = token

    async def create(self, namespace_key: str, segment_key: str, *, request: ConstraintCreateRequest) -> Constraint:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(
                    f"{self._environment.value}/",
                    f"api/v1/namespaces/{namespace_key}/segments/{segment_key}/constraints",
                ),
                json=jsonable_encoder(request),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Constraint, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, namespace_key: str, segment_key: str, id: str) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "DELETE",
                urllib.parse.urljoin(
                    f"{self._environment.value}/",
                    f"api/v1/namespaces/{namespace_key}/segments/{segment_key}/constraints/{id}",
                ),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(self, namespace_key: str, segment_key: str, id: str, *, request: ConstraintUpdateRequest) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "PUT",
                urllib.parse.urljoin(
                    f"{self._environment.value}/",
                    f"api/v1/namespaces/{namespace_key}/segments/{segment_key}/constraints/{id}",
                ),
                json=jsonable_encoder(request),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
