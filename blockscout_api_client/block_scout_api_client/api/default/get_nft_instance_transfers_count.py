from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_nft_instance_transfers_count_response_200 import GetNftInstanceTransfersCountResponse200
from ...types import Response


def _get_kwargs(
    address_hash: str,
    id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/tokens/{address_hash}/instances/{id}/transfers-count",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetNftInstanceTransfersCountResponse200]]:
    if response.status_code == 200:
        response_200 = GetNftInstanceTransfersCountResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetNftInstanceTransfersCountResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    address_hash: str,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, GetNftInstanceTransfersCountResponse200]]:
    """get transfers count of NFT instance

    Args:
        address_hash (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetNftInstanceTransfersCountResponse200]]
    """

    kwargs = _get_kwargs(
        address_hash=address_hash,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    address_hash: str,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, GetNftInstanceTransfersCountResponse200]]:
    """get transfers count of NFT instance

    Args:
        address_hash (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetNftInstanceTransfersCountResponse200]
    """

    return sync_detailed(
        address_hash=address_hash,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    address_hash: str,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, GetNftInstanceTransfersCountResponse200]]:
    """get transfers count of NFT instance

    Args:
        address_hash (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetNftInstanceTransfersCountResponse200]]
    """

    kwargs = _get_kwargs(
        address_hash=address_hash,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    address_hash: str,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, GetNftInstanceTransfersCountResponse200]]:
    """get transfers count of NFT instance

    Args:
        address_hash (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetNftInstanceTransfersCountResponse200]
    """

    return (
        await asyncio_detailed(
            address_hash=address_hash,
            id=id,
            client=client,
        )
    ).parsed
