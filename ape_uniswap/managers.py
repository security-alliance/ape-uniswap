from ape.utils import ManagerAccessMixin
from ape import Contract
from .router_codec import RouterCodec
from eth_typing import AnyAddress
from ._enums import (
    FunctionRecipient,
)
from ._constants import (
    _router_abi,
)
from ape.api import AccountAPI, ReceiptAPI
from eth_utils import to_checksum_address

from typing import (
    Optional,
    Sequence,
)
UNI_V2_ROUTER = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"
UNI_V3_ROUTER = "0xE592427A0AEce92De3Edee1F18E0157C05861564"


class UniswapManager(ManagerAccessMixin):
    def __init__(self) -> None:
        self.router_codec = RouterCodec()

    def __repr__(self) -> str:
        return "<ape_uniswap.UniswapManager>"

    def execute_v3_swap_exact_in_simple(
            self,
            amount_in: int,
            amount_out_min: int,
            token_in: AnyAddress,
            token_out: AnyAddress,
            fee: int,
            sender: Optional[AccountAPI] = None,
    ) -> ReceiptAPI:
        print(f"Executing swap exact in: {amount_in} {token_in} for {token_out}")
        if (self.network_manager.network.chain_id != 1):
            raise ValueError("Uniswap V3 is only supported on Ethereum Mainnet for now")
            
        print(f"Chain ID is 1")

        builder = self.router_codec.encode.chain()
        print(f"Builder initiated")
        builder = builder.v3_swap_exact_in(
            self,
            function_recipient=FunctionRecipient.SENDER,
            amount_in=amount_in,
            amount_out_min=amount_out_min,
            path=[to_checksum_address(token_in), fee, to_checksum_address(token_out)])
            
        print(f"Swap added to chain")

        encoded_data = builder.build()
        print(f"Encoded data: {encoded_data}")
        router_contract = Contract(UNI_V3_ROUTER, abi=_router_abi)
        print(f"Calling router contract: {router_contract.address}")

        return router_contract.__call__(data=encoded_data, sender=sender)
