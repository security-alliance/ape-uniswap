from ape.contracts import ContractInstance
from ape.types import ContractType
from ape.utils import ManagerAccessMixin, cached_property
from eth_utils import to_checksum_address
from ape import chain, project, networks, accounts, Contract
from tokenlists import TokenListManager
from .router_codec import RouterCodec
from eth_typing import AnyAddress
from ._enums import (
    _RouterConstant,
    _RouterFunction,
    FunctionRecipient,
)
from ._constants import (
    _execution_function_input_types,
    _execution_function_selector,
    _router_abi,
)
from ape.api import AccountAPI, Address, ReceiptAPI, TransactionAPI

from typing import (
    Any,
    cast,
    Dict,
    List,
    Optional,
    Sequence,
    Tuple,
    Union,
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
        if (self.network_manager.network.chain_id != 1):
            raise ValueError("Uniswap V3 is only supported on Ethereum Mainnet for now")

        builder = self.router_codec.encode.chain()
        builder = builder.v3_swap_exact_in(
            self,
            FunctionRecipient.SENDER,
            amount_in,
            amount_out_min,
            Sequence[token_in, fee, token_out])

        encoded_data = builder.build()
        router_contract = Contract(UNI_V3_ROUTER, abi=_router_abi)

        return router_contract.__call__(data=encoded_data, sender=sender)
