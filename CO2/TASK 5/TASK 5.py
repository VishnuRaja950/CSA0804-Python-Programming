def add_item_buggy(item, order=[]):
    order.append(item)
    return order

def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order

print(add_item_buggy("Tea"), add_item_buggy("Vada"))
print(add_item("Tea"), add_item("Vada"))
print("defaults:", add_item_buggy.__defaults__)

def make_bill(items, gst_rate=0.05):
    subtotal = sum(items)
    gst = subtotal * gst_rate
    return subtotal, gst, subtotal + gst

print("bill:", make_bill([40, 20]))

# local, global and nonlocal examples
total_orders = 0
def record_order():
    global total_orders
    total_orders += 1

def counter():
    count = 0
    def increase():
        nonlocal count
        count += 1
        return count
    return increase

record_order()
next_count = counter()
print("global:", total_orders, "nonlocal:", next_count(), next_count())
