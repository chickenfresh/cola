# cola.py
def get_min_price(price=7, k=3):
    today_money = price
    for i in range(4):
        bottles = (today_money - price + 1) // k
        if (today_money - price + 1) % k != 0:
            bottles += 1
        c = today_money - bottles * k
        today_money = bottles * price + c
    return today_money


print(get_min_price())
