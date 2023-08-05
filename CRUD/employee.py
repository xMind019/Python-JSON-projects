import json

def add_data():
	no = input("Enter your employee number: ")
	name = input("Enter your name: ")
	position = input("Enter your job position: ")

	dic = {
		"Employee Number: " : no,
		"Name: " : name,
		"Job Position: " : position 
	}

	with open("employee.json", "r") as getdata:
		data = json.load(getdata) # convert json to python

		data[no] = dic

		with open("employee.json", "w") as save:
			json.dump(data,save)  # convert python to json

add_data()
