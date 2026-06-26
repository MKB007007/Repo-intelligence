import requests
from datetime import datetime as dt, date
from dotenv import load_dotenv
import os

load_dotenv()
git_token=os.getenv("GITHUB_TOKEN")
print(git_token)

try:
    soc_l=[]# sum of contributions
    soc=0
    contributors_l=[]
    contributions_l=[]
    share_l=[]
    url=""
    bf=0
    ss=0
    commit=""
    no_of_commits_30=0
    no_of_commits_90=0
    activity_ratio=0

    headers = {
    "Authorization": f"Bearer {git_token}"
   }
    repo=input("Enter repo name: ")
    url=f"https://api.github.com/repos/{repo}"
    response = requests.get(url,headers=headers)
    token = response.json()

    print('='*60)
    print("GITHUB INTELLIGENCE ANALYSER".center(60))
    print('='*60,'\n')
    print("Repository Information")
    print("-"*60)
    print("Repository Name: ", token['name'])
    print("Repository Owner: ", token['owner']['login'])
    print("Repository Description: ", token['description'])
    print("Repository Language: ", token['language'])
    print("Created At: ", token['created_at'])
    print("Updated At: ", token['updated_at'],end="\n\n")

    j=1
    while j!=0:
        s=f"{url}/contributors?page={j}"
        contributors=requests.get(s, headers=headers).json()
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
    print("\nBus Factor Analysis")
    print("-" * 60)
    print(f"Bus Factor: {bf}")
    print(f"Risk Level: {risk}")
    print(f"Insight: {message}")

    commit_url=f"{url}/commits"
    commit_request=requests.get(commit_url, headers=headers).json()
    latest_commit=commit_request[0]['commit']['committer']["date"]
    latest_commit_author=commit_request[0]['commit']['author']["name"]
    latest_commit=latest_commit[0:latest_commit.find('T')]
    
    d1 = dt.strptime(date.today().strftime("%Y-%m-%d"), "%Y-%m-%d").date()
    d2 = dt.strptime(latest_commit, "%Y-%m-%d").date()

    j=1
    while (d1-d2).days <120 and j!=0:
        commit_url=f"{url}/commits?page={j}"
        commit_request=requests.get(commit_url, headers=headers).json()
        if len(commit_request)==0:
            break
        for i in range(0, len(commit_request)):
            commit=commit_request[i]['commit']['committer']["date"]
            commit=commit[0:commit.find('T')]
            d2 = dt.strptime(commit, "%Y-%m-%d").date()
            if (d1-d2).days <30:
                no_of_commits_30+=1
            elif (d1-d2).days >=30 and (d1-d2).days <120:
                no_of_commits_90+=1
            else:
                j=-1
                break
        j+=1
    ratio_30=no_of_commits_30/30
    ratio_90=no_of_commits_90/90

    print("\nActivity Analysis")
    print("-" * 60)
    print(f"Latest Commit Date      : {latest_commit}")
    print(f"Latest Commit Author    : {latest_commit_author}")
    print()
    print(f"Commits (Last 30 Days)  : {no_of_commits_30}")
    print(f"Commits (Prev. 90 Days) : {no_of_commits_90}")
    print(f"Recent Activity Rate    : {ratio_30:.2f} commits/day")
    print(f"Previous Activity Rate  : {ratio_90:.2f} commits/day")
    print()

    if ratio_90 == 0:
        if ratio_30 == 0:
            trend = "Dormant"
            insight = "No development activity was detected in the last 120 days."
        else:
            trend = "Revived"
            insight = "The repository has resumed development after a period of inactivity."
    else:
        activity_ratio = ratio_30 / ratio_90
        if activity_ratio > 1.3:
            trend = "Accelerating"
            insight = "Development activity has increased significantly compared to the previous three months."
        elif activity_ratio >= 0.7:
            trend = "Stable"
            insight = "Development activity has remained consistent over the past four months."
        else:
            trend = "Declining"
            insight = "Development activity has slowed compared to the previous three months."

    print(f"Activity Trend       : {trend}")
    print(f"Insight              : {insight}")



except Exception as e:
    print(type(e))
    print(e)