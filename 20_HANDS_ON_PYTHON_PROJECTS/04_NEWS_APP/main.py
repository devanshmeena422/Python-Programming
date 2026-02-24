import requests
query = input("What type of news are you intrested in today? : ")
api = "7faf84a57d054e83aae1589265013312"
url = f"https://newsapi.org/v2/everything?q={query}&from=2026-01-12&sortBy=publishedAt&apiKey={api}"
print(url)
r = requests.get(url)
data = r.json()
articles = data["articles"]

for index , article in enumerate (articles):
    print(index + 1 ,article["title"] , article["url"])
    print("\n ************************************ \n")