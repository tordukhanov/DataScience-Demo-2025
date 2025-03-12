import click


def greedy_coin(change):
    """Retuerns a dictionary with coin types as a key and number as the value"""
    conins = [0.25, 0.10, 0.50, 0.01]
    coins_loop = {0.25: "quarter", 0.10: "dime", 0.50:"nickle", 0.01:"penny"}
    coin_dict = {}
    for coin in coins:
        coin_dict[coin] = 0
    for coin in coins:
            