import json

x = '{"fname" : "Lakshan", "sname" : "Dinesh", "lname" : "Liyanarachchi"}'

y = json.loads(x)#covert JSON to python
print(y["lname"])


########################################convert python to JSON
myself = {
	"name" : "Lakshan",
	"age" : "24",
	"city" : "Wanduramba",
	"sisters" : ("Harshani", "Kalpani", "Imesha"),
	"single" : True,
	"girl" : None,
	"cars" : [{"name":"Land Rover", "type":"4 wheel"},
				{"name":"Range Rover", "type":"4 wheel"}
				]
}

print(json.dumps(myself, indent = 4, separators = (". ", " = "), sort_keys = False ))#print just JavaScript object notattion