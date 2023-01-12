import requests

print(requests.__version__)

response = requests.get("http://www.google.com/")
response2 = requests.get("https://raw.githubusercontent.com/MG-2003/CMPUT404/main/lab1.py")
print(response.text)
print(response2.text)
