import requests

soc_l=[]# sum of contributions
soc=0
contributors_l=[]
contributions_l=[]
share_l=[]
url=""

repo=input("Enter repo name: ")
url=f"https://api.github.com/repos/{repo}"
response = requests.get(url)
token = response.json()

print("Repository Name: ", token['name'])
print("Repository Owner: ", token['owner']['login'])
print("Repository Description: ", token['description'])
print("Repository Language: ", token['language'])
print("Created At: ", token['created_at'])
print("Updated At: ", token['updated_at'],end="\n\n")

j=1
while j!=0:
    s=f"{url}/contributors?page={j}"
    contributors=requests.get(s).json()
    if len(contributors)==0:
        break
    for i in contributors:
        soc_l.append(i)
    j+=1
    
print("Contributors: ".ljust(20), "Contributions: ".ljust(10), "Share: ".rjust(10))
print("-"*60)

for i in soc_l:
    soc+=int(i['contributions'])
print("Total number of contributions: ", soc,end="\n\n")

for i in soc_l:
    contributors_l.append(i['login'])
    contributions_l.append(i['contributions'])
    share_l.append(int(i['contributions'])/soc*100)
    print(f"{i['login']:20} {i['contributions']:<10} {int(i['contributions'])/soc*100:0.2f}% contributed")

print(f"Top contributor Share: {share_l[0]:0.2f}%")

print(f"Top 5 contributors Share: {sum(share_l[0:5]):0.2f}%")
