from bot.validators import validate_side


def test_validate_side():

    assert validate_side("buy") == "BUY"
    assert validate_side("sell") == "SELL"