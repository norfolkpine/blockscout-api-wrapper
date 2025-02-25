from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExtendedRevertReasonAsMap")


@_attrs_define
class ExtendedRevertReasonAsMap:
    """
    Attributes:
        raw (str):  Example: 4b415032303a207472616e7366657220616d6f756e74206578636565647320616c6c6f77616e6365.
        code (int):
        message (str):  Example: Reverted.
    """

    raw: str
    code: int
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        raw = self.raw

        code = self.code

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "raw": raw,
                "code": code,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        raw = d.pop("raw")

        code = d.pop("code")

        message = d.pop("message")

        extended_revert_reason_as_map = cls(
            raw=raw,
            code=code,
            message=message,
        )

        extended_revert_reason_as_map.additional_properties = d
        return extended_revert_reason_as_map

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
