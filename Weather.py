import requests

url = "https://api.weatherbit.io/v2.0/current"
params = {
    "key": "0249bb0f331f4fcc851919a5d3deef78",
    "lang": "en",  # Optional
    "units": "M",   # Optional
    "city": "Bhopal",
    "country": "IN"
}

response = requests.get(url, params=params)
data = response.json()

# Now you can use the 'data' variable to access the weather information
print(data)