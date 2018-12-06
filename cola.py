# cola.py
def calc_bottles(budg, price) -> (None, int):
    result = budg // price
    return None if result == 0 else result


def get_min_price(budget=0, price=7, k=3) -> int:
    starting_budget = budget
    for i in range(4):
        bottles = calc_bottles(budget, price)
        if not bottles:
            return get_min_price(starting_budget + 1, price, k)
        budget = budget % price + bottles * k
    bottles = calc_bottles(budget, price)
    if not bottles:
        return get_min_price(starting_budget + 1, price, k)
    budget = budget % price
    return starting_budget if budget == 0 and bottles == 1 else get_min_price(starting_budget + 1, price, k)


print(get_min_price())
