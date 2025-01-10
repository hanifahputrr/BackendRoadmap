#conditionally operation

def forward_order_status(order):
    if order["status"] == "ORDER_MASUK":
        order["status"] = "DIKEMAS"
    elif order["status"] == "DIKEMAS":
        order["status"] = "DIKIRIM"
    else:
        order["status"] = "SELESAI"
    return order 

print(forward_order_status({"status": "ORDER_MASUK"}))  # {"status": "ORDER_MASUK"}
print(forward_order_status({"status": "DIKEMAS"}))  # {"status": "DIKIRIM"}
print(forward_order_status({"status": "DIKIRIM"}))  # {"status": "SELESAI"}