from django.shortcuts import render

import requests
import json
import base64
from PIL import Image

# Create your views here.

def img_data(request):
    print("function calllll.................................")
    datas =""
    if request.method == "POST":
        print(request.POST,">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(request.FILES,">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        fname = request.POST.get('name')
        uploaded_image = request.FILES['img']

        encoded_image = base64.b64encode(uploaded_image.read()).decode('utf-8')
        print(encoded_image,"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        url = "https://vision.googleapis.com/v1/images:annotate"

        key = "#" #mention your api key

        data = {'key': key}

        payload = json.dumps({
        "requests": [
            {
            "image": {
                "content" :encoded_image # base64 encoded image format
            },
            "features": [
                {
                "type": "DOCUMENT_TEXT_DETECTION"
                }
            ]
            }
        ]
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload, params=data)

        # print(response.text)
        dict_data  = json.loads(response.text) #convert json data to dictionary data
   
        datas = dict_data['responses'][0]["fullTextAnnotation"]['text']

    return render(request,'index.html',{'data':str(datas)})
