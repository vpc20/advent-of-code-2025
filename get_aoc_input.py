import requests

# Paste your copied session cookie value here
SESSION_ID = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

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
