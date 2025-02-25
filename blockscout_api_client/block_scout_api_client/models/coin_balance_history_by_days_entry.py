from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CoinBalanceHistoryByDaysEntry")


@_attrs_define
class CoinBalanceHistoryByDaysEntry:
    """
    Attributes:
        date (str):  Example: 2022-08-02.
        value (float):  Example: 100232323.
    """

    date: str
    value: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        date = d.pop("date")

        value = d.pop("value")

        coin_balance_history_by_days_entry = cls(
            date=date,
            value=value,
        )

        coin_balance_history_by_days_entry.additional_properties = d
        return coin_balance_history_by_days_entry

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
