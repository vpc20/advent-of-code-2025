import requests

# Paste your copied session cookie value here
SESSION_ID = "53616c7465645f5fc77d1a4cc725ba225838170f9e4002a01ce9236b7907ee0ce133815136c542d5a3e96901d69b222dcffb698afc6379f67e37d79ba0503f12"

# change the url to get the input for each day
url = "https://adventofcode.com/2019/day/3/input"
cookies = {"session": SESSION_ID}

response = requests.get(url, cookies=cookies)

if response.status_code == 200:  # successful get
    data = response.text
    # print(data[:100])  # Print the first 100 characters of your input
    day = url.split('/')[5].zfill(2)
    filename = f"aoc_{day}_data1.txt"
    with open(filename, "w") as f:
        f.write(data)
else:
    print(f"Error {response.status_code}: {response.text}")