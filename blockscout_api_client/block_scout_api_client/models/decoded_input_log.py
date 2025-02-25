from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.decoded_input_log_parameter import DecodedInputLogParameter


T = TypeVar("T", bound="DecodedInputLog")


@_attrs_define
class DecodedInputLog:
    """
    Attributes:
        method_call (str):  Example: transferFrom(address _from, address _to, uint256 _value).
        method_id (str):  Example: 23b872dd.
        parameters (list['DecodedInputLogParameter']):
    """

    method_call: str
    method_id: str
    parameters: list["DecodedInputLogParameter"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method_call = self.method_call

        method_id = self.method_id

        parameters = []
        for parameters_item_data in self.parameters:
            parameters_item = parameters_item_data.to_dict()
            parameters.append(parameters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method_call": method_call,
                "method_id": method_id,
                "parameters": parameters,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.decoded_input_log_parameter import DecodedInputLogParameter

        d = src_dict.copy()
        method_call = d.pop("method_call")

        method_id = d.pop("method_id")

        parameters = []
        _parameters = d.pop("parameters")
        for parameters_item_data in _parameters:
            parameters_item = DecodedInputLogParameter.from_dict(parameters_item_data)

            parameters.append(parameters_item)

        decoded_input_log = cls(
            method_call=method_call,
            method_id=method_id,
            parameters=parameters,
        )

        decoded_input_log.additional_properties = d
        return decoded_input_log

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
