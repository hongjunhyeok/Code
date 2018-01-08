
class Pibo:
    def __init__(self,old1,old2):
        self.old1=0
        self.old2=1


    def __iter__(self):
        return self


    def __next__(self):

            current = self.old1+self.old2
            self.old1=self.old2
            self.old2=current
            return current

# iter=Pibo().__iter__()


for i in Pibo():
        print(i)
        count +=1
        if count ==100:
            break