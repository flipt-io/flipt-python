# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class RolloutSegmentOperator(str, enum.Enum):
    OR_SEGMENT_OPERATOR = "OR_SEGMENT_OPERATOR"
    AND_SEGMENT_OPERATOR = "AND_SEGMENT_OPERATOR"

    def visit(
        self, or_segment_operator: typing.Callable[[], T_Result], and_segment_operator: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is RolloutSegmentOperator.OR_SEGMENT_OPERATOR:
            return or_segment_operator()
        if self is RolloutSegmentOperator.AND_SEGMENT_OPERATOR:
            return and_segment_operator()
