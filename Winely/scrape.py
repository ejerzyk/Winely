import json, urllib2, sqlite3

database_name = 'db.sqlite3'
num_wines = 100
offset = 72800
print "[STATUS] Connecting to database"
conn = sqlite3.connect(database_name)
print "[STATUS] Connected to database"
c = conn.cursor()
print "[STATUS] Created cursor"

# print "[STATUS] Creating wines table"
# c.execute('''CREATE TABLE wines (id, name, url, region, varietal, wine_type, food_type, vineyard, vintage, price, style, rating)''')
# print "[STATUS] Created wines table"

while (num_wines == 100) or (offset < 81526):
	api = "http://services.wine.com/api/beta2/service.svc/JSON/catalog?filter=categories(490)&offset=" + str(offset) + "&size=100&apikey=12f62e4289aaac88de6323f7878656d6"
	obj = json.load(urllib2.urlopen(api))
	wines = obj['Products']['List']
	num_wines = len(wines)
	for wine in wines:
		Id = wine['Id']
		name = wine['Name']
		url = wine['Url']
		region = wine['Appellation']['Region']['Name']
		varietal = wine['Varietal']['Name']
		wine_type = wine['Varietal']['WineType']['Name']
		food_type = ""
		vineyard = wine['Vineyard']['Name']
		vintage = wine['Vintage']
		price = wine['PriceRetail']
		style = wine['ProductAttributes'][len(wine['ProductAttributes']) - 1]['Name'] if len(wine['ProductAttributes']) > 0 else ""
		rating = wine['Ratings']['HighestScore']
		to_insert = [Id, name, url, region, varietal, wine_type, food_type, vineyard, vintage, price, style, rating]
		c.execute("INSERT INTO wines VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", to_insert)
	offset = offset + num_wines
	conn.commit()
	print "[STATUS] Committed " + str(offset) + " wines"

print "[STATUS] Closing connection"
conn.close()
print "[STATUS] Closed connection"

print  "[STATUS] Scraped " + str(offset) + " wines successfully!"