"""
import soundcloud

client = soundcloud.Client(
    client_id="4BHhtKR78O7UYNyiwKbKTPQ1gmDGKOLj",
    client_secret="CrSEBf6SL2KFMohbQwhf7x6cb6h2gIrR",
    redirect_uri="http://localhost/callback",
)
auth_url = client.authorize_url()
print("Authorization URL:", auth_url)

token = client.exchange_token(auth_url)
print("Access Token:", token.access_token)
"""