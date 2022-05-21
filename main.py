import datetime

import requests


#------Properties--------
TOKEN = "34sdfsdfskdjh834jnfjgnj"
USER_NAME = "teddev0422"
GRAPH_ID = "codinggraph1"
API = "https://pixe.la/v1/users"
GRAPH_API = f"{API}/{USER_NAME}/graphs"
GRAPH_ADD_API = f"{GRAPH_API}/{GRAPH_ID}"


# Get today date
now = datetime.datetime.today()
now = now.strftime("%Y%m%d")
# Graph header
headers = {
    "X-USER-TOKEN": TOKEN
}


# Step 1: Create a user
user_info = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
create_user = requests.post(url=API, json=user_info)


# Step 2: Create graph
graph_info = {
    "id": GRAPH_ID,
    "name": "coding-routine",
    "unit": "hours",
    "type": "float",
    "color": "sora"

}
create_graph = requests.post(url=GRAPH_API, json=graph_info, headers=headers)


#Step 3: post a variable in graph
updated_variables = {
    "date": now,
    "quantity": "10"
}

add_to_graph = requests.post(url=GRAPH_ADD_API, json=updated_variables, headers=headers)

#Step 4: update a pixel in graph
update_graph = requests.put(url=f"{GRAPH_ADD_API}/{now}", json=updated_variables, headers = headers)


# Step 5: delete the pixel
delete_pixel = requests.delete(url=f"{GRAPH_ADD_API}/{now}", headers= headers)


