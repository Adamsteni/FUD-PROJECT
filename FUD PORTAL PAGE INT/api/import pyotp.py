import requests

url = "https://textflow-sms-api.p.rapidapi.com/service/check"

payload = { "testing": "true" }
headers = {
	"x-rapidapi-key": "a27af25e0emshd0d0890478dda34p11a934jsn7bd408655921",
	"x-rapidapi-host": "textflow-sms-api.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())