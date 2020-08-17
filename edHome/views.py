from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from ussd.core import UssdView, UssdRequest
@csrf_exempt
class Doctor(UssdView):
    def get(self, req):
        return UssdRequest(
        phone_number=req.data['phoneNumber'].strip('+'),
        session_id=req.data['sessionId'],
        #ussd_input=text,
        service_code=req.data['serviceCode'],
        language=req.data.get('language', 'en')
    )
    def ussd_response_handler(self, ussd_response):
        if ussd_response.status:
            res = 'CON' + ' ' + str(ussd_response)
            response = HttpResponse(res)
        else:
            res = 'END' + ' ' + str(ussd_response)
        response = HttpResponse(res)
        return response

