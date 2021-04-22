from concurrent import futures
import random
import pymongo
from google.protobuf.json_format import MessageToJson
import grpc

from studentCart_pb2 import (
    classRequest,
    classResponse,
)
import studentCart_pb2_grpc

client = pymongo.MongoClient("classlist_db",27017)
client_2 = pymongo.MongoClient("cart_db",27017)
db = client.classlist
db_2 = client_2.cart
class cartService(
    studentCart_pb2_grpc.cartServicer
):
    def addClass(self, request, context):
        size = db.classInfo.find_one({"course_code":request.courseCode})["size"]
        if ( size == 0 ): # class is full
            return classResponse(success=False)
        db.classInfo.update_one( {"course_code":request.courseCode}, {"$inc" :{"size":-1} } ) # decrement size of the class
        title = db.classInfo.find_one({"course_code":request.courseCode})["titles"]
        credit = db.classInfo.find_one({"course_code":request.courseCode})["credit"]
        course_info = db.classInfo.find_one({"course_code":request.courseCode},{"course_info":1})["course_info"]
        for course in course_info:
            if course["section"] == request.section:
                print(course)
                request_1 = {"title":title,"section":request.section,"classNumber":course["class_numbers"],"days":course["days"],"time":course["times"], "instructor":course["instructors"],"credit":credit}
                cart = db_2.cart.find_one({"username":request.userName})["cart"]
                cart.append(request_1)
                db_2.cart.update_one({"username":request.userName}, {"$set" : {"cart" : cart}}) # updating the cart of the user after adding the new class
                print(db_2.cart.find_one({"username":request.userName}))
                return classResponse(success=True)

    def dropClass(self, request, context):
        db.classInfo.update_one( {"course_code":request.courseCode}, {"$inc" :{"size":1} } ) # increment size of the class
        cart = db_2.cart.find_one({"userName":"ta326"})["cart"]
        i = 0 # used to find the position of the class in the cart which will be removed
        print(cart)
        for Class in cart:
            if Class["section"] == request.section:
                cart.pop(i)
                print(cart)
                db_2.cart.update_one({"userName":request.userName}, {"$set" : {"cart" : cart}})
                print(db_2.cart.find_one({"userName":request.userName}))
                return classResponse(success=True)
            else:
                i+=1
        return classResponse(success=False)
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))
    studentCart_pb2_grpc. add_cartServicer_to_server(
        cartService(), server
    )
    server.add_insecure_port("0.0.0.0:5003")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()