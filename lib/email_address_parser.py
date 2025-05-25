# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string

    def parse(self):
       
        emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', self.email_string)

        return sorted(set(emails))