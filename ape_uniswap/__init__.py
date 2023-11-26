from .router_codec import RouterCodec

from .managers import UniswapManager as _UniswapManager

uniswap = _UniswapManager()

__all__ = [
    "RouterCodec",
    "uniswap"
]
