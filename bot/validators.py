from bot.exceptions import ValidationError


VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]


def validate_symbol(symbol):

    if not symbol.endswith("USDT"):
        raise ValidationError(
            "Symbol must end with USDT"
        )

    return symbol.upper()


def validate_side(side):

    side = side.upper()

    if side not in VALID_SIDES:
        raise ValidationError(
            "Side must be BUY or SELL"
        )

    return side


def validate_order_type(order_type):

    order_type = order_type.upper()

    if order_type not in VALID_ORDER_TYPES:
        raise ValidationError(
            "Order type must be MARKET or LIMIT"
        )

    return order_type


def validate_quantity(quantity):

    if quantity <= 0:
        raise ValidationError(
            "Quantity must be greater than 0"
        )

    return quantity


def validate_price(price, order_type):

    if order_type == "LIMIT":

        if price is None:
            raise ValidationError(
                "LIMIT order requires price"
            )

        if price <= 0:
            raise ValidationError(
                "Price must be greater than 0"
            )

    return price