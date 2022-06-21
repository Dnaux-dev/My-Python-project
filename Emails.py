from curses.ascii import EM
import smtplib
import os

from string import Template

from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage

username = os.environ.get('email')
password = os.environ.get('psw')


MY_ADDRESS = 'ajiloredaniel33@gmail.com'
PASSWORD = 'aizzapbocyqbauzt'


def get_contacts(my_contacts):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """

    names = []
    emails = []
    with open(my_contacts, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails


def read_template(message):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """

    with open(message, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def main():
    names, emails = get_contacts('my_contacts.txt')  # read contacts
    message_template = read_template('message.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=465)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):      # create a message
        em = EmailMessage
        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        em ['From'] = MY_ADDRESS
        em ['To'] = email
        em ['Subject'] = "This is TEST"

        # add in the message body
            # send the message via the server set up earlier.
        s.send_message(msg)
        del msg

    # Terminate the SMTP session and close the connection
    s.quit()


if __name__ == '__main__':
    main()
