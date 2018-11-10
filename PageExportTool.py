# import the following Python modules for needed functionality
import requests
import json
import csv

# set the base URL to the eCX API, and the endpoint
base_url = "https://api.sandbox.ecrimex.net"
phish_endpoint = "/phish"
query_params = ""

# the request will need to have headers set, the Authorization value should be set to your eCX API token key which 
# you can find in your eCX profile at https://ecrimex.net/users/update
headers = {
    'Authorization': "",
    'Content-Type': "application/json"
    }

# function to call the eCX API
def extractPhishData(endpoint):
    url = base_url + endpoint
    # add the query_params variable to the request if you want to filter your data or set the output format
    response = requests.request("GET", url, headers=headers)
    data = json.dumps(response.json())
    api_data = json.loads(data)
    links = api_data['_links']
    api_phish = api_data['_embedded']['phish']
    return_data = {'phish': api_phish, 'links': links}
    return return_data

# our array to hold the output data
output_data = []

#call our function to GET the data
temp_data = extractPhishData(phish_endpoint)

# in the results of the output is a _links JSON array, save the array into links
links = temp_data['links']

output_data.extend(temp_data['phish'])

# iterate the results as long as links has a `next` key in the array
while 'next' in links:
    next_url = links['next']['href']
    new_phish_data = extractPhishData(next_url)
    links = new_phish_data['links']
    output_data.extend(new_phish_data['phish'])

# manually convert the data and output it into a CSV file.
# alternately you could add 'container=csv' to query_params and include it in the request above
with open('Output_Phish_Data.csv', 'w',newline='') as new_csv_file:
    fieldnames = ['_links','id','url','brand','confidence_level','date_discovered','modified','asn','ip','domain','metadata','status']
    csv_writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames, delimiter= ',')
    csv_writer.writeheader()

    for line in output_data:
        csv_writer.writerow(line)




