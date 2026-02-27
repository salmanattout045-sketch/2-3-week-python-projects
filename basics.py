import json
import os


class APICache:
    def __init__(self, filename="cache.json"):
        self.filename = filename

    def save(self,data):
        with open(self.filename, "w") as f:
            json.dump(data,f,indent=4)

    def load(self):
        if self.exists():
            with open(self.filename, "r") as f:
                return json.load(f)
        else:
            print("cant load file")
            return None

    def exists(self):
        return os.path.exists(self.filename)

api_cache = APICache("cache.json")
content={"name":"Salman","age":16}
api_cache.save(content)

api_cache.exists()
loaded = api_cache.load()
print("here the data: ",loaded)

class Paper_Crypto:
    def __init__(self,coin="bitcoin"):
        self.coin = coin
        self.price_history=[]

    def add_history(self,price):

            self.price_history.append(price)
    def average_price(self):
        return sum(self.price_history)/len(self.price_history)

    def highest_price(self):
        return max(self.price_history)
    def lowest_price(self):
        return min(self.price_history)

paper_crypto = Paper_Crypto("bitcoin")
print(paper_crypto.add_history(15000))
print(paper_crypto.add_history(1000))
print(paper_crypto.add_history(35000))
print(paper_crypto.add_history(3000))
print(paper_crypto.add_history(20000))
print(paper_crypto.average_price())
print(paper_crypto.highest_price())
print(paper_crypto.lowest_price())



class DailyReport:
    def __init__(self):
        self.daily_report = {}

    def add_daily_report(self,name,value):
        self.daily_report[name]=value

    def dump_to_Json(self):
        with open("daily_report.json", "w") as f:
            json.dump(self.daily_report,f,indent=4)

    def load_to_Json(self):
        with open("daily_report.json", "r") as f:
            self.daily_report = json.load(f)

    def show_summary(self):
        revenue= self.daily_report.get("revenue",0)
        expense= self.daily_report.get("expense",0)
        profit= revenue - expense

        print("revenue:",revenue)
        print("expense:",expense)
        print("profit:",profit)

daily_report = DailyReport()
daily_report.add_daily_report("revenue",15000)
daily_report.add_daily_report("expense",10000)
daily_report.dump_to_Json()
daily_report.load_to_Json()
daily_report.show_summary()


