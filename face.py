import requests
import json
import io
from PIL import Image
import base64

subscription_key = ""
#subscription_key = ""
#################################################
#face-detect 1
#################################################
face_api_url = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect"
headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/octet-stream'
}
parameters = {
    'returnFaceId':'true',
    'returnFaceLandmarks':'false'
}
image_data = open('bean.jpg','rb').read()
response = requests.post(face_api_url, headers=headers, params=parameters, data=image_data)
#print(response.json())
print(response.json()[0]['faceId'])
id1 = response.json()[0]['faceId']
#################################################
#face-detect 2
#################################################
image_data = open('bean1.jpg','rb').read()
response = requests.post(face_api_url, headers=headers, params=parameters, data=image_data)
id2 = response.json()[0]['faceId']
print(id2)
#################################################
#face-verify 1&2
#################################################
face_api_url_verify = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/verify"
body = {
    'faceId1': id1,
    'faceid2': id2
}
parameters = {
}
headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/json'
}
response = requests.post(face_api_url_verify, headers=headers, params=parameters, json=body)
print(response.json())
#################################################
#PersonGroups Create
#################################################
headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/json'
}
body = {
    'name':'group1',
    'userdata':'Whitelisted users',
}
face_api_person_group_url = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/persongroups/pone"
#response = requests.put(face_api_person_group_url, headers=headers, json=body)
#print(response.json())
#################################################
#PersonGroups Person Create
#################################################
face_api_person_group_create_url = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/persongroups/pone/persons"
headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/json'
}
body = {
    'name':'Person1',
    'userData':'user provided data',
}
parameters = {'personGroupId':'pone'}
response = requests.post(face_api_person_group_create_url, headers=headers,params=parameters, json=body)
print(response.json())
pid = response.json()['personId']
#################################################
#PersonGroups Train
#################################################
face_api_url_person_group_train= "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/persongroups/pone/train"
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
parameters={'personGroupId':'pone'}
body = {}
response = requests.post(face_api_url_person_group_train, headers=headers)
print(response)
#################################################
#PersonGroups Person AddFace
#################################################
parameters = {
    'personId': pid,
}
headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/octet-stream'
}
image_data = open('bean.jpg','rb').read()
#image_data = str(image_data)
b_data_string = base64.b64encode(image_data)
body = "{b_data_string}"
#body = str({[image_data]})
#body = str(body)
face_api_person_group_create_url = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/persongroups/pone/persons/"
response = requests.post(face_api_person_group_create_url, headers=headers,params=parameters,data=body)
print(response.json())
