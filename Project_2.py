print("Welcome to resume generator".title())
class basic_info:
    def about(self,name,email,phone):
        with open('Resume.txt' , 'wt') as f:
            f.write ('Name : '+ name + '\n')
            f.write ('email : '+ email + '\n')
            f.write ('phone : ' + str(phone) + '\n')
            f.write ('\n')

    def objective(self,describe):
        with open('Resume.txt' , 'a') as f:
            f.write ('Objective : ' +'\n')
            f.write (describe + '\n')
            f.write ('\n')
            
    def edu(self,a,b,c):
        with open('Resume.txt' , 'a') as f:
            f.write ('10th score : ' + a + '\n')
            f.write ('12th score : ' + b + '\n')
            f.write ('degree scoren : ' + c + '\n')
            f.write ('\n')
class exp:
    def proj_exp(self):
        with open('Resume.txt' , 'a') as f:
            f.write ('Experience details : ' + '\n')
            f.write ('\n')
    def details(self,a,b,c,d):
        with open('Resume.txt' , 'a') as f:
            f.write ('Project name : '+ a +'\n')
            f.write ('\n')
            f.write ('Role in project : ' + b + '\n')
            f.write ('Team size : ' + c + '\n')
            f.write ('Responsibities : ' + d + '\n')
            f.write ('\n')

class certification:
    def cert(self):
        with open('Resume.txt' , 'a') as f:
            f.write ('Certications : ' + '\n')
            f.write ('\n')
    def cert_det(self,a,b):
        with open('Resume.txt' , 'a') as f:    
            f.write (a + ' Valid till ' + b + '\n')
            f.write ('\n')
obj1 = basic_info()
obj1.about(input("Enter your full name : ") ,input("Enter your valid email id : "), int(input("Enter your phone number : ")))
obj1.objective(input("Enter the objective : "))
obj1.edu(input("Enter your 10th score in '%' : "),input("Enter your 12th score in '%' : "),input("Enter your degree score in '%' : "))
obj2 = exp()
obj2.proj_exp()
s = int(input("Enter the number of projects you handled : "))
for i in range(s):
    obj2.details(input("Enter your project name : "),input("Enter your role in your project : "),input("Enter the team size of your project : "),input("Explain your responsibilities in your project : "))
obj3 = certification()
obj3.cert()
cert_num = int(input("Enter the number of certifications : "))
for i in range(cert_num):
    obj3.cert_det(input("Enter the Certification you did : "),input("Certificate valid till (dd/mm/yyyy) : "))
    
