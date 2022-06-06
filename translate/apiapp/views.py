from django.shortcuts import render
import http.client
import json


# BELOW GOOGLE TRANSLATOR API USED IN THE POST REQUEST FROM THE USER

# Create your views here.
def home(request):
    if request.method == 'POST':
        if request.POST['input1'] == "null" and request.POST['lan1'] == "null" and request.POST['lan2'] == "null":
            return render(request, 'home.html', {'validation_msg': "please the valid fields"})
        else:
            conn = http.client.HTTPSConnection("google-translate1.p.rapidapi.com")
            text_user = request.POST['input1']
            out_lang = request.POST['lan2']
            in_lang = request.POST['lan1']
            payload = "q=" + text_user + "&target=" + out_lang + "&source=" + in_lang

            headers = {
                'content-type': "application/x-www-form-urlencoded",
                'accept-encoding': "application/gzip",
                'x-rapidapi-host': "google-translate1.p.rapidapi.com",
                'x-rapidapi-key': "enterapikey"
            }

            conn.request("POST", "/language/translate/v2", payload, headers)

            res = conn.getresponse()
            data = res.read()

            mydata = json.loads(data.decode("utf-8"))
            result_lang = mydata["data"]["translations"][0]['translatedText']
            return render(request, 'home.html', {'Message': result_lang})

    else:
        return render(request, 'home.html')
