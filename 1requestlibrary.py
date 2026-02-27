import requests

url = "https://cdn-0001.qstv.on.epicgames.com/PIEdEgHqduVxJVmCxL/image/landscape_comp.jpeg"

response = requests.get(url)

with open("funny.jpeg", "wb") as f:
    f.write(response.content)
print(response.status_code)  # when you get 200 no errors perfect
                             #if 300 its rederict
                             #if its 400 its client errors
                             #if its 500 its server errors
print(response.ok)#now that gives anything below 400 asuming there is no problem
print(response.headers) # that basically gives info


payload={'user_name': "salman",'password': "testing"}
r= requests.post('https://httpbin.org/post',data=payload)
r_dict = r.json()
print(r_dict['form'])

#now heres how to authenticate:


r= requests.get('https://httpbin.org//basic-auth/salman/testing', auth=('salman','testing'))
print(r.text)

#exersice 1


data_lumina=" https://python.datalumina.com/"
entering=requests.get(data_lumina)
print(entering.content)

#exersice 2


url = "https://i.ytimg.com/vi/JDx9cGhV0rc/maxresdefault.jpg"
response = requests.get(url)

with open("funny_dog.jpg", "wb") as f:
    f.write(response.content)


url = "https://th.bing.com/th/id/R.d059c6fb97ad0bac4070b71e01e2c4ad?rik=Slqo0ops6Uh8vg&riu=http%3a%2f%2fimages7.memedroid.com%2fimages%2fUPLOADED338%2f6363612892aef.jpeg&ehk=gSxxcXt6XtFHdqA%2f3MXKJd2YeQACgy3WDiFOReYEhp4%3d&risl=&pid=ImgRaw&r=0"
response = requests.get(url)
with open("funny_rock.jpg", "wb") as f:
    f.write(response.content)

url="https://www.bing.com/search?q=liverpool+fc&form=ANNNB1&refig=6956ac9595a74ad1ad135b5537d88d9d&pc=U531&pq=liverpool&pqlth=9&assgl=12&sgcn=liverpool+fc&qs=HS&sgtpv=HS&smvpcn=0&swbcn=10&sctcn=0&sc=10-9&sp=1&ghc=0&cvid=6956ac9595a74ad1ad135b5537d88d9d&clckatsg=1&hsmssg=0"
response = requests.get(url)
print(response.text)

# ex.5

info = {
    "name": "salman",
    "age": 15,
    "hobbie": "fifa",
    "2hobie": "python",
    "date of birth": "6/4/2011",
    "fav_food": "chicken"
}

response = requests.post("https://httpbin.org/post", data=info)
print(response.text)





#1.
url= "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
print("Status code: ", response.status_code)
print("Content Type" , response.headers.get('Content-Type'))
data=response.json()
print("Post title :", data["title"])

#2. error handling

try:
    response = requests.get("https://httpbin.org/delay/3", timeout=1)
except requests.exceptions.Timeout:
    print(" time ran out")
except requests.exceptions.RequestException as e:
    print("request failed",e)

#3. authorization



