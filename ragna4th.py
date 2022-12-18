import json
import requests


class Ragna4th:
    def __init__(self):
        self.url = "https://api.ragna4th.com/db/market"
        self.auth = "Bearer MTQ4Nzky.fpBp5q5EbHvkAMB28YByxatO8SlOSYGN9gf0T4YGu591R6K9Ytw_InVgt7J6"

    # noinspection PyMethodMayBeStatic
    def get_item_name(self, item_id):
        url = f"https://roleta.ragna4th.com/db/i/q/in/{item_id}"
        response = requests.request("GET", url, data='')

        return json.loads(response.text)[0]['name']

    # noinspection PyMethodMayBeStatic
    def search_prices(self, item_id):
        payload = {
            "search": f'{item_id}',
            "limit": 100,
            "filters": [
                {
                    "field": "nameid",
                    "operator": "in",
                    "value": f'[{item_id}]'
                }
            ],
            "order":
                {
                    "by": "price",
                    "direction": "asc"
                }
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.auth
        }

        response = requests.request("POST", url=self.url, json=payload, headers=headers)
        return json.loads(response.text), self.get_item_name(item_id)

    def show_item_prices(self, item_id):
        data, item_name = self.search_prices(item_id)
        price_check = {}

        for item in data['result']['items']:
            if item['price'] in price_check:
                price_check[str(item['price'])] += item['amount']
            else:
                price_check[str(item['price'])] = item['amount']

        message = f"{'=' * int((60-len(item_name))/2)}{item_name}{'=' * int((60-len(item_name))/2)}\n"

        for price, quantity in price_check.items():
            message += f" Preço: {'{:,}'.format(int(price)) + 'ƶ': <24}{'Quantidade: ': >24}{quantity}\n"

        return message


# ragna4th = Ragna4th()
# print(ragna4th.show_item_prices("8030"))