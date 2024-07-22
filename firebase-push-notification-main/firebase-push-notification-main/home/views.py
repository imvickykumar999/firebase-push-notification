from django.http.request import HttpHeaders
from django.shortcuts import render

from django.http import HttpResponse
import requests
import json



def send_notification(registration_ids , message_title , message_desc):
    fcm_api = ""
    url = "https://fcm.googleapis.com/fcm/send"
    
    headers = {
    "Content-Type":"application/json",
    "Authorization": 'key='+fcm_api}

    payload = {
        "registration_ids" :registration_ids,
        "priority" : "high",
        "notification" : {
            "body" : message_desc,
            "title" : message_title,
            "image" : "https://i.ytimg.com/vi/m5WUPHRgdOA/hqdefault.jpg?sqp=-oaymwEXCOADEI4CSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDwz-yjKEdwxvKjwMANGk5BedCOXQ",
            "icon": "https://yt3.ggpht.com/ytc/AKedOLSMvoy4DeAVkMSAuiuaBdIGKC7a5Ib75bKzKO3jHg=s900-c-k-c0x00ffffff-no-rj",
            
        }
    }

    result = requests.post(url,  data=json.dumps(payload), headers=headers )
    print(result.json())





def index(request):
    return render(request , 'index.html')

def send(request):
    resgistration  = ["dJfCbgEvjZXcRxV-PqqHyJ:APA91bE024ZTyYzloqGspO7NToG0sqzHG5ZMaoMV7c36Z3XWt15yelFPh5q6GAyYO4mc9S2b8BlNysb56YpRfEsh5LepDJ2wSm8xeebz_yzuLnGVCpQh-vZVmCT8YwMWpZs0hEahaUC4", ]
    send_notification(resgistration , 'Code Keen added a new video' , 'Code Keen new video alert')
    return HttpResponse("sent")


def showFirebaseJS(request):
    data='importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-app.js");' \
         'importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-messaging.js"); ' \
         'var firebaseConfig = {' \
         '        apiKey: "AIzaSyDEffV60DqptX5isXVzlhYp1JMKf7t2wlA",' \
         '        authDomain: "fir-push-notification-85613.firebaseapp.com",' \
         '        projectId: "fir-push-notification-85613",' \
         '        storageBucket: "fir-push-notification-85613.appspot.com",' \
         '        messagingSenderId: "279392742552",' \
         '        appId: "1:279392742552:web:df183eb0e8c256fb7174ed",' \
         '        measurementId: "G-TZVKHMQSRE"' \
         ' };' \
         'firebase.initializeApp(firebaseConfig);' \
         'const messaging=firebase.messaging();' \
         'messaging.setBackgroundMessageHandler(function (payload) {' \
         '    console.log(payload);' \
         '    const notification=JSON.parse(payload);' \
         '    const notificationOption={' \
         '        body:notification.body,' \
         '        icon:notification.icon' \
         '    };' \
         '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
         '});'

    return HttpResponse(data,content_type="text/javascript")
