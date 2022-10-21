import requests

# r = requests.get("https://api.github.com/repos/dward2/BME547/branches")
# print(r)
# print(type(r))
# print(r.text)
# if r.status_code == 200:
#    answer = r.json()
#    print(type(answer))
#    for branch in answer:
#        print(branch["name"])
# else:
#    print("Bad Connection:".foramt(r))

# output_info = {"name": "Konrad Slaman",
#                "net_id": "kjs74",
#                "e-mail": "konrad.slaman@duke.edu"}
# r = requests.post("http://vcm-21170.vm.duke.edu:5000/student",
#                   json=output_info)
output_info = {"user": "konrad", "message": "I hate UNC"}
r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message",
                  json=output_info)
m = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/mimi")
print(m.text)