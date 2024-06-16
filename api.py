# import requests

# url = "https://microsoft-translator-text.p.rapidapi.com/languages"

# querystring = {"api-version":"3.0"}

# headers = {
# 	"x-rapidapi-key": "703c09c28dmshfae0db001cbbb13p1d23f7jsn1b51b53328f3",
# 	"x-rapidapi-host": "microsoft-translator-text.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)
# if response.headers['Content-Type'] == 'application/json':
#     try:
#         data = response
#         print(data.json())
#     except requests.exceptions.JSONDecodeError as e:
#         print("Error decoding JSON:", e)
#         # Handle the error gracefully (e.g., retry, log error, use default values)
# else:
#     # Handle non-JSON content
#     print(f"Warning: Unexpected content type: {response.headers['Content-Type']}")
#     # You might need to parse HTML, plain text, or another format here (if applicable)

