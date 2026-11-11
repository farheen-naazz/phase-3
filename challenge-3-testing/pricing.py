def calculate_final_price(amount: float, discount_percent: float) -> float:
    """Calculate an order total after applying a percentage discount."""

    if amount < 0:
        raise ValueError("Amount cannot be negative")

    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")

    discount_amount = amount * discount_percent / 100

    return round(amount - discount_amount, 2)