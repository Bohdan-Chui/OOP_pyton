from Order import Order
from Customer import Customer
from Store import Store

if __name__ == '__main__':
    try:
        order = Order(Customer('Bohdan', 'Chuy', 'Serhiyouvich', '+380(97)-126-62-62'),Store(12.3,"Phone", 12),
                      Store(12.3,"Phone", 12), Store(12.3,"Phone", 12))
        print(order.total_order_value())
    except Exception as ve:
         print(ve)