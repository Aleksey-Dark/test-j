import sys
import requests

# response = requests.post('http://127.0.0.1:5000/', json={'start_date': '01-10-2022', 'end_date': '31.10.2022'})
response = requests.post('http://178.154.192.50:5000/', data={'start_date': '01-10-2022', 'end_date': '1.10.2022'})
# response = requests.post(f'{sys.argv[1]}', data={'start_date': f'{sys.argv[2]}', 'end_date': f'{sys.argv[3]}'})
print(response.text)
# input('Press "Enter" to exit.')
