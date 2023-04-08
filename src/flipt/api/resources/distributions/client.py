# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ....environment import FliptApiEnvironment
from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_headers import remove_none_from_headers
from .types.distribution import distribution


class DistributionsClient:
    def __init__(
        self, *, environment: FliptApiEnvironment = FliptApiEnvironment.PRODUCTION, token: typing.Optional[str] = None
    ):
        self._environment = environment
        self._token = token

    def create(self, flag_key: str, rule_id: str, *, variant_id: str, rollout: float) -> distribution:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._environment.value}/", f"api/v1/flags/{flag_key}/rules/{rule_id}/distributions"
            ),
            json=jsonable_encoder({"variantId": variant_id, "rollout": rollout}),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(distribution, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, flag_key: str, rule_id: str, id: str, *, variant_id: str) -> None:
        _response = httpx.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._environment.value}/", f"api/v1/flags/{flag_key}/rules/{rule_id}/distributions/{id}"
            ),
            params={"variantId": variant_id},
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(self, flag_key: str, rule_id: str, id: str, *, variant_id: str, rollout: float) -> distribution:
        _response = httpx.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._environment.value}/", f"api/v1/flags/{flag_key}/rules/{rule_id}/distributions/{id}"
            ),
            json=jsonable_encoder({"variantId": variant_id, "rollout": rollout}),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(distribution, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncDistributionsClient:
    def __init__(
        self, *, environment: FliptApiEnvironment = FliptApiEnvironment.PRODUCTION, token: typing.Optional[str] = None
    ):
        self._environment = environment
        self._token = token

    async def create(self, flag_key: str, rule_id: str, *, variant_id: str, rollout: float) -> distribution:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(
                    f"{self._environment.value}/", f"api/v1/flags/{flag_key}/rules/{rule_id}/distributions"
                ),
                json=jsonable_encoder({"variantId": variant_id, "rollout": rollout}),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(distribution, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, flag_key: str, rule_id: str, id: str, *, variant_id: str) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "DELETE",
                urllib.parse.urljoin(
                    f"{self._environment.value}/", f"api/v1/flags/{flag_key}/rules/{rule_id}/distributions/{id}"
                ),
                params={"variantId": variant_id},
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
            )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(self, flag_key: str, rule_id: str, id: str, *, variant_id: str, rollout: float) -> distribution:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "PUT",
                urllib.parse.urljoin(
                    f"{self._environment.value}/", f"api/v1/flags/{flag_key}/rules/{rule_id}/distributions/{id}"
                ),
                json=jsonable_encoder({"variantId": variant_id, "rollout": rollout}),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(distribution, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
