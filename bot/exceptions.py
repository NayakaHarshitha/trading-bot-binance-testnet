class ValidationError(Exception):
    """Raised when user input validation fails."""
    pass


class BinanceAPIError(Exception):
    """Raised when Binance API request fails."""
    pass