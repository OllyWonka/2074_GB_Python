import requests
    def currency_rates(code: str) -> float:
        response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        currency_dict = {}
        currency_list = response.text.split('ID=')
        del currency_list[0]
        for i in currency_list:
            exchange_rate = i[(i.find('<Value>') + 7): i.find('</Value>')]
            exchange_rate = float(exchange_rate.replace(',', '.')
            difference = int(i[(i.find('<Nominal>') + 9): i.find('</Nominal>')
    currency_dict[(i[(i.find('<CharCode>') + 10): i.find('</CharCode>')])] = exchange_rate/difference
    result_value = currency_dict.get(code.upper(), None)
    return result_value

print(currency_rates("USD"))
