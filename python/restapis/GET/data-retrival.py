import requests

response = requests.get('https://jsonplaceholder.typicode.com/users/1')
response.raise_for_status()  # Raise an error for bad responses
# data = response.json()  # Parse the JSON response

if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    if data.get('username') == 'Bret':
        print("Username is Bret")

# print(data)  # Print the retrieved data