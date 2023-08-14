# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class FlagType(str, enum.Enum):
    VARIANT_FLAG_TYPE = "VARIANT_FLAG_TYPE"
    BOOLEAN_FLAG_TYPE = "BOOLEAN_FLAG_TYPE"

    def visit(
        self, variant_flag_type: typing.Callable[[], T_Result], boolean_flag_type: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is FlagType.VARIANT_FLAG_TYPE:
            return variant_flag_type()
        if self is FlagType.BOOLEAN_FLAG_TYPE:
            return boolean_flag_type()