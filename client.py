import requests


r = requests.get("http://127.0.0.1:5000/time")
print(r.status_code)
print(r.text)

r = requests.get("http://127.0.0.1:5000/date")
print(r.status_code)
print(r.text)

out_data = {'date': "10/21/2002",
            'units': "year"}
r2 = requests.post("http://127.0.0.1:5000/age", json=out_data)
print(r2.status_code)
print(r2.text)

r = requests.get("http://127.0.0.1:5000/breakfast")
print(r.status_code)
print(r.text)

r = requests.get("http://127.0.0.1:5000/lunch")
print(r.status_code)
print(r.text)

r = requests.get("http://127.0.0.1:5000/dinner")
print(r.status_code)
print(r.text)

# out_data2 = {"a": 50, "b": 11}
# r3 = requests.post("http://127.0.0.1:5000/add_numbers", json=out_data2)
# print(r3.status_code)
# print(r3.text)