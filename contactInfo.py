class ContactInfo:
    def __init__(self, name, phone,email):
        self.name= name
        self.email= email
        self.phone =phone

    def print_info(self):
        print('{0}:{1}:{2}'.format(self.name,self.phone,self.email))

if __name__ == '__main__':
    sanghyun = ContactInfo('박상현','seenlab@gmail.com')
    hanbit = ContactInfo('hanbit','noreply@hanb.co.kr')

    sanghyun.print_info()
    hanbit.print_info()

