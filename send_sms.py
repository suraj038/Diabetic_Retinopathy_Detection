from twilio.rest import Client

#--------------------------------------------------------
# change values of account_sid, auth_token, to and from - all from twilio account
#-------------------------------------------------------

class Send:

    def send_msg(self,value,classes):
    #     # Your Account SID from twilio.com/console
        account_sid = "AC2c3f836befda3c8529953adee0af569b"
    #     # Your Auth Token from twilio.com/console
        auth_token  = "69327eb4a4b72a5121e10f9a65fb4d0a"
    #
        client = Client(account_sid, auth_token)
    #
        message = client.messages.create(
            to="+91 63607 59972",
            from_="+15109441462",
            body=f"Message from suraj \n Diabetic Retinopathy Detection System Report! severity level is {value}:  and class is {classes}")
    #
        print('Message sent Succesfully !')
        print(message.sid)

