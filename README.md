# Paginate the eCX API

**Version 1.0.0**

A simple Python example using the Requests module to interact with the eCX API to query for the latest phish data.  Because the eCX API uses the HAL+JSON spec in the output users are able to iterate through pages of results matching their query parameters. 

**CSV Output**

By default eCX outputs all data in JSON using the HAL+JSON spec, which allows consumers of the data to control all pagination thoughout the result set.

  However, the eCX API fully supports CSV output using the `container` parameter set to `csv`.  
  
  Example:   
  
  `https://api.ecrimex.net/phish?container=csv`  
  
  Note that the default JSON object contains nested key value pairs that will not flatten into CSV, so the only values returned when CSV is desired are: id, brand, date_discovered, URL, confidence_level, and modified.
  
 This example goes a little further with CSV output, and does not use the `container=cvs` parameter, instead it demonstrates how to use Python to convert the output to csv on the fly.

**Developed By...**

Alan Fajardo for the APWG, alan.fajardo916@gmail.com
