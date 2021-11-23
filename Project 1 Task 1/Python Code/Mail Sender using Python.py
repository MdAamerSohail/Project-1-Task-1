import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

# Type Your Gmail Id and Password
s.login("#Your Gmail Id", "#password")
  
# Type Your Subject and Body
subject = "#Type Your Subject Here"
body= "#Type Your Body Text Here"

message = "Subject:{}\n\n{}".format(subject,body)

# Type Emails where to send
SendTo = ["type email id", "type email id"]

# sending the mail
s.sendmail("Your Gmail Id", SendTo, message)
  
s.quit()
