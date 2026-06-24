import requests
try:
    soc_l=[]# sum of contributions
    soc=0
    contributors_l=[]
    contributions_l=[]
    share_l=[]
    url=""
    bf=0
    ss=0

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
        
    for i in soc_l:
        soc+=int(i['contributions'])
    print("Total number of contributions: ", soc,end="\n\n")

    print("Contributors: ".ljust(20), "Contributions: ".ljust(10), "Share: ".rjust(10))
    print("-"*60)

    for i in soc_l:
        contributors_l.append(i['login'])
        contributions_l.append(i['contributions'])
        share_l.append(int(i['contributions'])/soc*100)
        print(f"{i['login']:20} {i['contributions']:<10} {int(i['contributions'])/soc*100:0.2f}% contributed")

    print()
    print(f"Top contributor Share: {share_l[0]:0.2f}%")
    print(f"Top 5 contributors Share: {sum(share_l[0:5]):0.2f}%\n")

    i=0
    while ss<80:
        ss+=float(share_l[i])
        bf+=1
        i+=1
    if bf == 1:
        risk = "Critical"
        message = "This project depends heavily on a single contributor. Losing that contributor could seriously impact development."
    elif bf <= 3:
        risk = "High"
        message = "A small number of contributors are responsible for most of the work. The project has a high dependency on key individuals."
    elif bf <= 7:
        risk = "Moderate"
        message = "Development is concentrated among a few contributors, but knowledge is reasonably distributed."
    elif bf <= 15:
        risk = "Healthy"
        message = "Work is spread across several contributors, reducing dependency on any single person."
    elif bf <= 30:
        risk = "Very Healthy"
        message = "The project benefits from strong contributor diversity and low concentration risk."
    else:
        risk = "Highly Distributed"
        message = "Contributions are widely distributed across the community, indicating excellent resilience and collaboration."
    print(f"Bus Factor: {bf}")
    print(f"Risk Level: {risk}")
    print(f"Insight: {message}")

except KeyError:
    print("Invalid repository name. Please check the repository name and try again.")