import re
import requests
from datetime import datetime as dt


def currency_rates(*val):
    for cur_val in val:
        date_var = dt.strptime(re.findall(r'(\d+.\d+.\d+)', xml_currency[2])[0], "%d.%m.%Y")
        if len(cur_val) == 3:
            for string in range(0, len(xml_currency)-1):
                match = re.search(cur_val, xml_currency[string])
                if match:
                    xml_to_list = xml_currency[string+6].split('>')[1].split(',')
                    value = float(xml_to_list[0]) + (float(xml_to_list[1]) * (pow(10, -len(xml_to_list[1]))))
                    break
            else:
                value = 'No such currency'
        else:
            value = 'currency has to be 3 digits'
        return [date_var.date(), value, cur_val]


xml_currency = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text.split('<')

