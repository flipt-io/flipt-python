# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from .types.rule import Rule
from .types.rule_create_request import RuleCreateRequest
from .types.rule_list import RuleList
from .types.rule_order_request import RuleOrderRequest
from .types.rule_update_request import RuleUpdateRequest

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RulesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        namespace_key: str,
        flag_key: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
    ) -> RuleList:
        """
        Parameters:
            - namespace_key: str.

            - flag_key: str.

            - limit: typing.Optional[int].

            - offset: typing.Optional[int].

            - page_token: typing.Optional[str].
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/v1/namespaces/{namespace_key}/flags/{flag_key}/rules"
            ),
            params=remove_none_from_dict({"limit": limit, "offset": offset, "pageToken": page_token}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(RuleList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(self, namespace_key: str, flag_key: str, *, request: RuleCreateRequest) -> Rule:
        """
        Parameters:
            - namespace_key: str.

            - flag_key: str.

            - request: RuleCreateRequest.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/v1/namespaces/{namespace_key}/flags/{flag_key}/rules"
            ),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Rule, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def order(self, namespace_key: str, flag_key: str, *, request: RuleOrderRequest) -> None:
        """
        Parameters:
            - namespace_key: str.

            - flag_key: str.

            - request: RuleOrderRequest.
        """
        _response = self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/v1/namespaces/{namespace_key}/flags/{flag_key}/rules/order",
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

    def get(self, namespace_key: str, flag_key: str, id: str) -> Rule:
        """
        Parameters:
            - namespace_key: str.

            - flag_key: str.

            - id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/v1/namespaces/{namespace_key}/flags/{flag_key}/rules/{id}",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Rule, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, namespace_key: str, flag_key: str, id: str) -> None:
        """
        Parameters:
            - namespace_key: str.

            - flag_key: str.

            - id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/v1/namespaces/{namespace_key}/flags/{flag_key}/rules/{id}",
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

    def update(self, namespace_key: str, flag_key: str, id: str, *, request: RuleUpdateRequest) -> None:
        """
        Parameters:
            - namespace_key: str.

            - flag_key: str.

            - id: str.

            - request: RuleUpdateRequest.
        """
        _response = self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/v1/namespaces/{namespace_key}/flags/{flag_key}/rules/{id}",
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


class AsyncRulesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        namespace_key: str,
        flag_key: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
    ) -> RuleList:
        """
        Parameters:
            - namespace_key: str.

            - flag_key: str.

            - limit: typing.Optional[int].

            - offset: typing.Optional[int].

            - page_token: typing.Optional[str].
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/v1/namespaces/{namespace_key}/flags/{flag_key}/rules"
            ),
            params=remove_none_from_dict({"limit": limit, "offset": offset, "pageToken": page_token}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(RuleList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(self, namespace_key: str, flag_key: str, *, request: RuleCreateRequest) -> Rule:
        """
        Parameters:
            - namespace_key: str.

            - flag_key: str.

            - request: RuleCreateRequest.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/v1/namespaces/{namespace_key}/flags/{flag_key}/rules"
            ),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Rule, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def order(self, namespace_key: str, flag_key: str, *, request: RuleOrderRequest) -> None:
        """
        Parameters:
            - namespace_key: str.

            - flag_key: str.

            - request: RuleOrderRequest.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/v1/namespaces/{namespace_key}/flags/{flag_key}/rules/order",
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

    async def get(self, namespace_key: str, flag_key: str, id: str) -> Rule:
        """
        Parameters:
            - namespace_key: str.

            - flag_key: str.

            - id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/v1/namespaces/{namespace_key}/flags/{flag_key}/rules/{id}",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Rule, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, namespace_key: str, flag_key: str, id: str) -> None:
        """
        Parameters:
            - namespace_key: str.

            - flag_key: str.

            - id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/v1/namespaces/{namespace_key}/flags/{flag_key}/rules/{id}",
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

    async def update(self, namespace_key: str, flag_key: str, id: str, *, request: RuleUpdateRequest) -> None:
        """
        Parameters:
            - namespace_key: str.

            - flag_key: str.

            - id: str.

            - request: RuleUpdateRequest.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/v1/namespaces/{namespace_key}/flags/{flag_key}/rules/{id}",
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
