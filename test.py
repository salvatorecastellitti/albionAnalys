import json

data = """
[{"UnitPriceSilver": "5320000", "Amount": "100", "AuctionType": "request", "ItemTypeId": "T5_CLOTH"}, {"UnitPriceSilver": "5310000", "Amount": "849", "AuctionType": "request", "ItemTypeId": "T5_CLOTH"}]
"""

data = json.loads(data)

for item in data:
    print('\n\n', item)
    for x,y in item.items():
        print(x, y)
