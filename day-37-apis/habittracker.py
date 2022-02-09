"""
Creating a github-like habit tracker using pixela's API.
"""

#Imports
import requests
from datetime import datetime

#Endpoint parameters
USERNAME = 'habittrackr' #Your pixela username
TOKEN = '3qracests5vtdtdf' #Your pixela token
GRAPH_ID = 'habit1' #Your pixela graph id
today = datetime.today() #Get today's date to be able to update the graph without having to change the date in the code


pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username':USERNAME,
    'agreeTermsOfService':'yes',
    'notMinor':'yes'
}

#CREATE PIXELA USER, COMMENT OUT AFTER THE FIRST RUN
create_user = requests.post(url=pixela_endpoint, json=user_params)
print(create_user.text)

#CREATING THE GRAPH
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_params = {
                'id': GRAPH_ID,
                'name':'Reading Tracker', #Name of the graph
                'unit':'Pages', #Unit of the graph
                'type':'int', #Type of the data that will be stored in the graph
                'color':'momiji', #Color palette of the squares
}

header = {
    'X-USER-TOKEN': TOKEN
}

#CREATING THE GRAPH WITH THE POST REQUEST
post_graph = requests.post(url=graph_endpoint, json=graph_params, headers=header)
print(post_graph.text)

#ENDPOINT THAT WILL LET US UPDATE THE GRAPH
post_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

pixel_params = {
                'date':today.strftime("%Y%m%d"),
                'quantity':'20',
                'optionalData':"{\"Book\":\"The Outsider\"}"
}

#UPDATE THE GRAPH WITH THE POST REQUEST
post_pixel = requests.post(url=post_pixel_endpoint, json=pixel_params, headers=header)
print(post_pixel.text)
