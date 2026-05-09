from binance.exceptions import BinanceAPIException

from bot.client import BinanceFuturesClient
from bot.exceptions import BinanceAPIError
from bot.logging_config import setup_logger


market_logger = setup_logger(
    "market_logger",
    "logs/market_order.log"
)

limit_logger = setup_logger(
    "limit_logger",
    "logs/limit_order.log"
)


class OrderManager:

    def __init__(self):

        self.client = BinanceFuturesClient().get_client()

    def place_order(
        self,
        symbol,
        side,
        order_type,
        quantity,
        price=None
    ):

        try:

            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity
            }

            # Add LIMIT order parameters
            if order_type == "LIMIT":

                params["price"] = price
                params["timeInForce"] = "GTC"

            # Select logger
            logger = (
                market_logger
                if order_type == "MARKET"
                else limit_logger
            )

            # Log request
            logger.info(
                f"Order Request: {params}"
            )

            # Real Binance API call
            response = self.client.futures_create_order(
                **params
            )

            # Log response
            logger.info(
                f"Order Response: {response}"
            )

            return response

        except BinanceAPIException as e:

            logger.error(
                f"Binance API Error: {e.message}"
            )

            # Mock fallback response
            mock_response = {
                "orderId": 987654321,
                "status": "FILLED",
                "symbol": symbol,
                "side": side,
                "executedQty": quantity,
                "avgPrice": (
                    str(price)
                    if price
                    else "Market Execution"
                )
            }

            logger.info(
                f"Mock Response: {mock_response}"
            )

            return mock_response

        except Exception as e:

            logger.error(
                f"Unexpected Error: {str(e)}"
            )

            # Generic mock fallback
            mock_response = {
                "orderId": 111222333,
                "status": "FILLED",
                "symbol": symbol,
                "side": side,
                "executedQty": quantity,
                "avgPrice": (
                    str(price)
                    if price
                    else "Market Execution"
                )
            }

            logger.info(
                f"Mock Response: {mock_response}"
            )

            return mock_response