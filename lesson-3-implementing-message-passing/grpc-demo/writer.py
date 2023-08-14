import grpc
import item_pb2
import item_pb2_grpc

import order_pb2
import order_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
# stub = item_pb2_grpc.ItemServiceStub(channel)
stub2 = order_pb2_grpc.OrderServiceStub(channel)

# Update this with desired payload
# item = item_pb2.ItemMessage(
#     name="Non-Stick Frying Pan",
#     brand_name="Chef Dreams",
#     id=4,
#     weight=4.5
# )

# create random OrderMessage
order = order_pb2.OrderMessage(
    id="1",
    created_by="user1",
    status=order_pb2.OrderMessage.Status.QUEUED,
    created_at="2020-01-01",
    equipment=[order_pb2.OrderMessage.Equipment.KEYBOARD, order_pb2.OrderMessage.Equipment.MOUSE]
)

# response = stub.Create(item)
# print(response)

response2 = stub2.Create(order)
print(response2)

response3 = stub2.Get(order_pb2.Empty())
print(response3)
