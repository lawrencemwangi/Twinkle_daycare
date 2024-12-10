from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from . credentials import MpesaC2bCredential, LipanaMpesaPpassword
import os

# Create your views here.

def Home(request):
    return render(request, 'home.html')


def About(request):
    return render(request, 'about.html')


def Service(request):
    return render(request, 'service.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact_page')
        else:
            messages.error(request, "All fields are required.")

    return render(request, 'contact.html')



def token(request):
    consumer_key = os.getenv("MPESA_CONSUMER_KEY")
    consumer_secret = os.getenv("MPESA_CONSUMER_SECRET")
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials" 

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})


def pay(request):
    if request.method == "POST":
        number = request.POST['number'] 
        amount = request.POST['amount']
        access_token = MpesaC2bCredential.get_mpesa_access_token()
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": f"Bearer {access_token}"}
        
        payment_data = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": number,  
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": number, 
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Twinkle Daycare",
            "TransactionDesc": "Fees Charges"
        }

        try:
            response = requests.post(api_url, json=payment_data, headers=headers)

            if response.status_code == 200:
                return HttpResponse("Payment success")
            else:
                return HttpResponse(f"Payment failed with status code {response.status_code}", status=500)
        
        except requests.RequestException as e:
            return HttpResponse(f"Error occurred while making payment request: {str(e)}", status=500)

    return HttpResponse("Invalid request method. Please use POST.", status=400)


def stk(request):
    return render(request, 'pay.html', {'navbar':'stk'})
