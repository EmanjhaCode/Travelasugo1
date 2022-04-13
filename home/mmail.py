# mail approved by gmail
 # link : https://www.digitalocean.com/community/questions/unable-to-send-mail-through-smtp-gmail-com
# 1 Go to admin.google.com
# 2 From the admin console, select “Security”
# 3 Select “Basic settings”
# 4 Scroll down to “Less secure apps”
# 5 Go to settings for less secure apps ››
# 6 Check the radio button “Allow users to manage their access to less secure apps”
# 7 Save the changes
# 8 Open this link being sign in as the super administrator https://www.google.com/settings/security/lesssecureapps
# 9 Check the radio button Turn On the access for less secure apps
# 10 Unlock Captcha using this link https://accounts.google.com/DisplayUnlockCaptcha
# end

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def tabmail(receiverid,otp):
    sender_email = "punjabinawab0651@gmail.com"
    receiver_email = receiverid
    password = "Punjabi@0651"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Emanjha LLC | OTP"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""
    html = f"""\
    <html>
      <body>
        <h2>Welcome to Emanjha LLC</h2>
           <h3>
           Your  OTP is {otp}
          </h3>

      </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
# em = input('write your email : ')
# y = tabmail(em)
