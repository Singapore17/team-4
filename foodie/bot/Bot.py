import datetime
import time
import imaplib
import os
import email

# Connection specs
ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "shaocongcongcong" + ORG_EMAIL
FROM_PWD    = "970520@dsc"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993
pwd         = os.getcwd()

class Bot():
    def __init__(self, email, password, port, server):
        self.server = server
        self.password = password
        self.port = port
        self.email = email
        self.items = [] # for getting all the email from the mail object
        self.mail = None #

    def connect_inbox(self):
        mail = imaplib.IMAP4_SSL(host=self.server, port=self.port)
        mail.login(self.email, self.password)
        mail.select('inbox')
        resp, items = mail.search(None, 'ALL')
        items = items[0].split()
        self.items = items
        print(self.items)
        self.mail = mail

    def parse_attachment(message_part):
        content_disposition = message_part.get("Content-Disposition", None)
        if content_disposition:
            dispositions = content_disposition.strip().split(";")
            if bool(content_disposition and dispositions[0].lower() == "attachment"):

                file_data = message_part.get_payload(decode=True)
                attachment = StringIO(file_data)
                attachment.content_type = message_part.get_content_type()
                attachment.size = len(file_data)
                attachment.name = None
                attachment.create_date = None
                attachment.mod_date = None
                attachment.read_date = None

                for param in dispositions[1:]:
                    name,value = param.split("=")
                    name = name.lower()

                    if name == "filename":
                        attachment.name = value
                    elif name == "create-date":
                        attachment.create_date = value
                    elif name == "modification-date":
                        attachment.mod_date = value
                    elif name == "read-date":
                        attachment.read_date = value
                return attachment

        return None

    def fetch_files(self):
        for item in self.items:
            resp, data = self.mail.fetch(item, "(RFC822)")

            email_body = data[0][1]
            m = email.message_from_bytes(email_body)
            parent_path = os.path.join(pwd, 'tmp')

            if m.get_content_maintype() == 'multipart':
                for part in m.walk():

                    if part.get_content_maintype() == 'multipart':
                        continue

                    if part.get('Content-Disposition') is None:
                        continue

                    fileName = part.get_filename()

                    if bool(fileName):
                        folderPath = os.path.join(parent_path, '2017_9_29_pass')
                        if not os.path.exists(folderPath):
                            os.makedirs(folderPath)
                        filePath = os.path.join(folderPath, fileName)
                        fileAbsPath = os.path.abspath(filePath)
                        print (fileAbsPath)
                        fp = open(fileAbsPath, 'wb')
                        fp.write(part.get_payload(decode=True))
                        fp.close()

def main():
    bot = Bot(FROM_EMAIL,FROM_PWD,SMTP_PORT,SMTP_SERVER)
    bot.connect_inbox()
    bot.fetch_files()

if __name__ == '__main__':
    main()
