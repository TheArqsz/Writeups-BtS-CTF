import requests
url = "http://127.0.0.1:2638/"
data = {"next_button": 1}

flag_dict = {}
flag = ''
response = {}
for i in range(0,1):
    response = requests.post(url, data)
    flag_dict[response.headers['x-sequence-number']] = response.headers['x-flag-letter']

for i in range(0,len(flag_dict)):
    flag += flag_dict[str(i)]
print flag
