from twilio.rest import Client

#--------------------------------------------------------
# change values of account_sid, auth_token, to and from - all from twilio account
#-------------------------------------------------------

class Send:

    def send_msg(self,value,classes):
    #     # Your Account SID from twilio.com/console
        account_sid = "***************************************"
    #     # Your Auth Token from twilio.com/console
        auth_token  = "***************************************"
    #
        client = Client(account_sid, auth_token)
    #
        message = client.messages.create(
            to="*****************",
            from_="**************",
            body=f"Message from suraj \n Diabetic Retinopathy Detection System Report! severity level is {value}:  and class is {classes}")
    #
        print('Message sent Succesfully !')
        print(message.sid)

