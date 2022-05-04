import requests
import json

url = 'https://api.occe.io/public/orders/sugar_uah'


def get_min():
    price = []
    origin_data = requests.get(url=url)
    data = json.loads(origin_data.content)
    if 'result' not in data or data['result'] != 'success':
        return 'wrong'
    else:
        data = data['data']['buyOrders']
        for i in data:
            price.append(i['price'])
        price.sort(reverse=True)
        if len(price) == 0:
            return 'empty'
        else:
            return '%.8f' % price[0]


if __name__ == '__main__':
    print(get_min())
