import requests

url = 'http://127.0.0.1:8000/api/calculate/'
payload = {
    'num1': 10,
    'num2': 5,
    'operation': 'add'  # try 'subtract', 'mul', or 'div' as well
}

response = requests.post(url, json=payload)
print(response.json())