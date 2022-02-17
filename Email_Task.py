# --------------- Email Task ---------------#

email1 = input("From (Enter Your Email ID) : ")  # Email ID of the Sender
email2 = input("To (Enter Recipient's Email ID) : ")  # Email ID of Receiver
subject = input("Subject : ")  # Subject Of an Email
content = input("Start Writing From Here : ")  # Content Of an Email
completed = " "
while True:
    completed = input("Do You Want to Send the Email (yes/no) : ").lower()  # Approval
    if completed == 'yes':
        print("Email Sent Successfully! ")
        break
    elif completed == 'no':
        print("Message Saved as Draft.")
        break
    else:
        print("I didn't Understand That ")
