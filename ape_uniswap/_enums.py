"""
Enums used by the Uniswap Universal Router Codec

* Author: Elnaril (https://www.fiverr.com/elnaril, https://github.com/Elnaril).
* License: MIT.
* Doc: https://github.com/Elnaril/uniswap-universal-router-decoder
"""


from enum import Enum

from eth_utils import to_checksum_address


class _RouterFunction(Enum):
    # https://docs.uniswap.org/contracts/universal-router/technical-reference#command
    V3_SWAP_EXACT_IN = 0
    V3_SWAP_EXACT_OUT = 1
    SWEEP = 4
    PAY_PORTION = 6
    V2_SWAP_EXACT_IN = 8
    V2_SWAP_EXACT_OUT = 9
    PERMIT2_PERMIT = 10
    WRAP_ETH = 11
    UNWRAP_WETH = 12


class FunctionRecipient(Enum):
    """
    SENDER: When the function recipient is the sender

    ROUTER: When the function recipient is the router

    CUSTOM: When the function recipient is neither the trx sender nor the router
    """
    SENDER = "recipient is transaction sender"
    ROUTER = "recipient is universal router"
    CUSTOM = "recipient is custom"


class _RouterConstant(Enum):
    # https://github.com/Uniswap/universal-router/blob/main/contracts/libraries/Constants.sol
    MSG_SENDER = to_checksum_address("0x0000000000000000000000000000000000000001")
    ADDRESS_THIS = to_checksum_address("0x0000000000000000000000000000000000000002")
    ROUTER_BALANCE = 2**255
