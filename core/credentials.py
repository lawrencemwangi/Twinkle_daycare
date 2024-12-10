import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64
import os


class MpesaC2bCredential:
    consumer_key = os.getenv("MPESA_CONSUMER_KEY")
    consumer_secret = os.getenv("MPESA_CONSUMER_SECRET")
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    if not all([consumer_key, consumer_secret]):
        raise ValueError("MPESA credentials missing or not loaded correctly.")

    @staticmethod
    def get_mpesa_access_token():
        consumer_key = MpesaC2bCredential.consumer_key
        consumer_secret = MpesaC2bCredential.consumer_secret
        api_url = MpesaC2bCredential.api_url

        if not (consumer_key and consumer_secret and api_url):
            raise ValueError("Missing MPESA credentials or API URL in environment variables.")

        auth = HTTPBasicAuth(consumer_key, consumer_secret)

        try:
            response = requests.get(api_url, auth=auth)
            response.raise_for_status()  
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Failed to fetch MPESA access token: {e}")

        try:
            mpesa_access_token = response.json()
        except json.JSONDecodeError:
            raise ValueError("Failed to decode MPESA API response as JSON.")

        validated_mpesa_access_token = mpesa_access_token.get("access_token")
        if not validated_mpesa_access_token:
            raise ValueError("Access token not found in MPESA API response.")

        return validated_mpesa_access_token



class LipanaMpesaPpassword:
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    Business_short_code = "174379"
    OffSetValue = '0'
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'

    data_to_encode = Business_short_code + passkey + lipa_time

    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')
