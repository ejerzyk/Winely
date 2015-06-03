import json, urllib2, sqlite3

database_name = 'db.sqlite3'

num_wines = 100
offset = 0
print "[STATUS] Connecting to database"
conn = sqlite3.connect(database_name)
print "[STATUS] Connected to database"
c = conn.cursor()
print "[STATUS] Created cursor"

def get_food_type(food_id, food_type):
	print "[STATUS] Getting " + food_type + " wines"
	while (num_wines == 100) or (offset < 81513):
		api = "http://services.wine.com/api/beta2/service.svc/JSON/catalog?filter=categories(490" + str(food_id) + ")&offset=" + str(offset) + "&size=100&apikey=12f62e4289aaac88de6323f7878656d6"
		obj = json.load(urllib2.urlopen(api))
		wines = obj['Products']['List']
		num_wines = len(wines)
		for wine in wines:
			Id = wine['Id']
			c.execute("UPDATE wines SET food_type = ? WHERE id = ?", food_type, Id)
		offset = offset + num_wines
		conn.commit()
		print "[STATUS] Commited " + str(offset) + " " + food_type + " wines"
	print "[STATUS] Got " + food_type + " wines"

get_food_type(3008, "Meat")
get_food_type(3009, "Cheese")
get_food_type(3010, "Dessert")
get_food_type(3012, "Pasta & Grains")
get_food_type(3013, "Poultry")
get_food_type(3014, "Seafood")

print "[STATUS] Closing connection"
conn.close()
print "[STATUS] Closed connection"

print "[STATUS] DONE"