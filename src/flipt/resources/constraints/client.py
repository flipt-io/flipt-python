# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from .types.constraint import Constraint
from .types.constraint_create_request import ConstraintCreateRequest
from .types.constraint_update_request import ConstraintUpdateRequest

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ConstraintsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(self, namespace_key: str, segment_key: str, *, request: ConstraintCreateRequest) -> Constraint:
        """
        Parameters:
            - namespace_key: str.

            - segment_key: str.

            - request: ConstraintCreateRequest.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/v1/namespaces/{namespace_key}/segments/{segment_key}/constraints",
            ),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
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
        """
        Parameters:
            - namespace_key: str.

            - segment_key: str.

            - id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/v1/namespaces/{namespace_key}/segments/{segment_key}/constraints/{id}",
            ),
            headers=self._client_wrapper.get_headers(),
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
        """
        Parameters:
            - namespace_key: str.

            - segment_key: str.

            - id: str.

            - request: ConstraintUpdateRequest.
        """
        _response = self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/v1/namespaces/{namespace_key}/segments/{segment_key}/constraints/{id}",
            ),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
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
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(self, namespace_key: str, segment_key: str, *, request: ConstraintCreateRequest) -> Constraint:
        """
        Parameters:
            - namespace_key: str.

            - segment_key: str.

            - request: ConstraintCreateRequest.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/v1/namespaces/{namespace_key}/segments/{segment_key}/constraints",
            ),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
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
        """
        Parameters:
            - namespace_key: str.

            - segment_key: str.

            - id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/v1/namespaces/{namespace_key}/segments/{segment_key}/constraints/{id}",
            ),
            headers=self._client_wrapper.get_headers(),
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
        """
        Parameters:
            - namespace_key: str.

            - segment_key: str.

            - id: str.

            - request: ConstraintUpdateRequest.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/v1/namespaces/{namespace_key}/segments/{segment_key}/constraints/{id}",
            ),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
