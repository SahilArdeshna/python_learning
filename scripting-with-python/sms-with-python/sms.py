from twilio.rest import Client

account_sid = "AC47e60a08383ee9ffb5c9fca8362f0ed3"
auth_token = "f343316c0dd313a88f11fc092f82a648"
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_="+15736725681", to="+918511802410", body="Lunch time!"
)

print(message.sid)
