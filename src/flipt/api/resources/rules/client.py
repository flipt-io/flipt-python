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
from .types.rule import rule
from .types.rule_list import ruleList


class RulesClient:
    def __init__(self, *, environment: FliptApiEnvironment, token: typing.Optional[str] = None):
        self._environment = environment
        self._token = token

    def list(
        self,
        flag_key: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
    ) -> ruleList:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment}/", f"api/v1/flags/{flag_key}/rules"),
            params={"limit": limit, "offset": offset, "pageToken": page_token},
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ruleList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(self, flag_key: str, *, segment_key: str, rank: int) -> rule:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment}/", f"api/v1/flags/{flag_key}/rules"),
            json=jsonable_encoder({"segmentKey": segment_key, "rank": rank}),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(rule, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def order(self, flag_key: str, *, rule_ids: typing.List[str]) -> None:
        _response = httpx.request(
            "PUT",
            urllib.parse.urljoin(f"{self._environment}/", f"api/v1/flags/{flag_key}/rules/order"),
            json=jsonable_encoder({"ruleIds": rule_ids}),
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

    def get(self, flag_key: str, id: str) -> rule:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment}/", f"api/v1/flags/{flag_key}/rules/{id}"),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(rule, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, flag_key: str, id: str) -> None:
        _response = httpx.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._environment}/", f"api/v1/flags/{flag_key}/rules/{id}"),
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

    def update(self, flag_key: str, id: str, *, segment_key: str) -> None:
        _response = httpx.request(
            "PUT",
            urllib.parse.urljoin(f"{self._environment}/", f"api/v1/flags/{flag_key}/rules/{id}"),
            json=jsonable_encoder({"segmentKey": segment_key}),
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
