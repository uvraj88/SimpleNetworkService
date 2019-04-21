# SimpleNetworkService
Simple Network Service which resolves lat and long to a address.

# Usage
Check Connection:
-use ping endpoint to check server connection:
-form url in below format.
-{http localhost}:{port}/ping
-port is usually '5000'
Eg: http://0.0.0.0:5000/ping


Query for an address:
-use resolve endpoint to get address:
-form url in below format.
-{http localhost}:{port}/resolve?params
-port is usually '5000'
-params should be in format 'lat={value}&long={value}'
-default value is set for lat and long to see a sample response.
Eg: http://0.0.0.0:5000/resolve?lat=49.78&long=-123.11
default values Eg: http://0.0.0.0:5000/resolve

#Start server
Goto inside src folder and run __main__.py file
Sample Eg: python __main__.py

#Run Tests
Goto inside tst folder and run 'pytest' command.
