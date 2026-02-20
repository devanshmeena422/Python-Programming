import requests

# r = requests("https://github.com/devanshmeena422/Python-Programming")
r = requests.get("https://api.github.com/users/codewithharry")

with open("devnsh.txt" , 'w') as f:
    f.write(r.text)