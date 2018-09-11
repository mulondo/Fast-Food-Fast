class Customer_Orders:
    def __init__(self):
        self.orders=[]

     def make_order(self,username,phone_number,myitems=list()):
        my_order=[]
        my_order=myitems
        order_id=len(self.orders)+1
        order={
            "username":username,
            "order_id":order_id,
            "phone_number":phone_number,
            "order_items":my_order,
            "status":"None"
        }
        return self.orders.append(order)