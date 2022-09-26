import os, json

#printing the environment variables as plain text

#print("Content-type: text/plain")
#print()
#print(os.environ)

# printing the environment variables as json
#print("Content-type: application/json")
#print()
#print(json.dumps(dict(os.environ), indent=4))

#print query parameter data in html
print("Content-type: text/html")
print()
print(f"<p>QUERY_STRING={os.environ['HTTP_USER_AGENT']}</p>")
