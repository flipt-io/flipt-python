# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class SegmentMatchType(str, enum.Enum):
    ALL_MATCH_TYPE = "ALL_MATCH_TYPE"
    ANY_MATCH_TYPE = "ANY_MATCH_TYPE"

    def visit(
        self, all_match_type: typing.Callable[[], T_Result], any_match_type: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is SegmentMatchType.ALL_MATCH_TYPE:
            return all_match_type()
        if self is SegmentMatchType.ANY_MATCH_TYPE:
            return any_match_type()