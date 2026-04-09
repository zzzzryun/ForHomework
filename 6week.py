order_detail = []

def make_order(name,qty,qul):
    order_detail.insert(qul-1, {"이름":name, "수량":qty})

print(order_detail)
make_order("아메리카노",2,3)
print(order_detail)
make_order("자바칩프라푸치노",1,1)
print(order_detail)
make_order("라떼",1,2)
print(order_detail)