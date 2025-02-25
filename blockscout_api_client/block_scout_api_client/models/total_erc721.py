from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nft_instance import NFTInstance


T = TypeVar("T", bound="TotalERC721")


@_attrs_define
class TotalERC721:
    """
    Attributes:
        token_id (str):  Example: 1.
        token_instance (Union[Unset, NFTInstance]):
    """

    token_id: str
    token_instance: Union[Unset, "NFTInstance"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token_id = self.token_id

        token_instance: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.token_instance, Unset):
            token_instance = self.token_instance.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token_id": token_id,
            }
        )
        if token_instance is not UNSET:
            field_dict["token_instance"] = token_instance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.nft_instance import NFTInstance

        d = src_dict.copy()
        token_id = d.pop("token_id")

        _token_instance = d.pop("token_instance", UNSET)
        token_instance: Union[Unset, NFTInstance]
        if isinstance(_token_instance, Unset):
            token_instance = UNSET
        else:
            token_instance = NFTInstance.from_dict(_token_instance)

        total_erc721 = cls(
            token_id=token_id,
            token_instance=token_instance,
        )

        total_erc721.additional_properties = d
        return total_erc721

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
