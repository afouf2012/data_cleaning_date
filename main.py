# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pymongo
from faker import Faker

fake = Faker()
client = pymongo.MongoClient("mongodb://aml_user:o0Eucdnbqf1rfidhj@vps-55aa3b4a.vps.ovh.net:19191/sanctions_db")
db = client["sanctions_db"]
collection = db["transactions"]
for trans in collection.find():
    print("begin")
    fakeDate = fake.date_time_between(start_date='-1y', end_date='now')
    collection.update_one({"_id": trans["_id"]}, {"$set": {"date": fakeDate}})

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
