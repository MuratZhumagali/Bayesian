import sys
import copy
from string import index
import itertools
import copy

i=1 
j=1
k=1
m=1
r=1
Pnormal_parkinson=0
Ptremor_parkinson=0
Pstiff_parkinson=0
disease=[]
patient=[]

file = open('sample_input.txt', 'r').readlines()
x=file
number_diseases=int(file[0].split(" ")[0])
number_patients=int(file[0].split(" ")[1])

for i in range(0, number_diseases*4+1):
    disease.append(file[i])
for j in range(number_diseases*4+1, number_patients*number_diseases+number_diseases*4+1):
    patient.append(file[j])
    
disease1 = []
while m<=number_diseases:
    temp = []
    for i in range(k, k + 4):
        if i == k:
            val = file[i].split()
        else:
            val = eval(file[i].strip())
        temp.append(val)     
    k = k + 4
    disease1.append(temp)
    m = m + 1

patient1=[]
n = number_diseases*4+1
while r<=number_patients:
    temp=[]
    for j in range(n, n + number_diseases):
        val1 = eval(file[j].strip())
        temp.append(val1)
    n = n + number_diseases
    patient1.append(temp) 
    r = r + 1
    
listofdiseases = []
l=1
for i in range(l, number_diseases+1):
    listofdiseases.append(file[l]) 
    l=l+4

listof_diseases=[]
i=0
for i in range(i, number_diseases):
    listof_diseases.append(listofdiseases[i].split(" ")[0]) 
    
#for index,i in enumerate(disease1):
 #   if i==position(listof_diseases)

 
def position(x, listof_diseases):

    if x in listof_diseases:  
        return listof_diseases.index(x)
    

        
        
y = position("parkinson", listof_diseases)

def position1(z, disease1):

    if z in disease1[y][1]:  
        return disease1[y][1].index(z)
    
t = position1("normal expression", disease1)

p=disease1[y][2][t]

for v in range(0, number_patients):
    

    for g in range(0, number_diseases):
        
        num=1
        den=1
        testdetails=patient1[v][g]
        
        for i in range (0, len(testdetails)):
            if testdetails[i]=='T':
                num=num*disease1[g][2][i]
            else :
                if testdetails[i]=='F':
                    num=num*(1-disease1[g][2][i])
                    
        num=num*float(disease1[g][0][2])
                   
        for i in range (0, len(testdetails)):
            if testdetails[i]=='T':
                den=den*disease1[g][3][i]
            else:
                if testdetails[i]=='F':
                    den=den*(1-disease1[g][3][i])
                    
        den=den*(1-float(disease1[g][0][2]))  
         
        resultquestion1=num/(num+den) 
        
        print "question1:", v, disease1[g][0][0], round(resultquestion1,4)

def calculation(testdetails, diseasenumber):
    
    num=1
    den=1
   
            
    for i in range (0, len(testdetails)):
                if testdetails[i]=='T':
                    num=num*disease1[diseasenumber][2][i]
                else :
                    if testdetails[i]=='F':
                        num=num*(1-disease1[diseasenumber][2][i])
                    
            
    num=num*float(disease1[diseasenumber][0][2])
                     
    for i in range (0, len(testdetails)):
                if testdetails[i]=='T':
                    den=den*disease1[diseasenumber][3][i]
                else:
                    if testdetails[i]=='F':
                        den=den*(1-disease1[diseasenumber][3][i])
                 
    den=den*(1-float(disease1[diseasenumber][0][2]))  
             
    result=num/(num+den)
    
    return result

for v in range(0, number_patients):
    

    for g in range(0, number_diseases):

        testdetails=patient1[v][g]
        
        for i in range(0, len(testdetails)):
            if testdetails[i]=='U':
                testdetails[i]='T'
                m=calculation(testdetails, g)
                testdetails[i]='F'
                n=calculation(testdetails, g)
                testdetails[i]='U'
                print "patient:", v, disease1[g][0][0], disease1[g][1][i] , m, n  
                
                
q=[]                
for v in range(0, number_patients):
    

    for g in range(0, number_diseases):
                          
        num=0
        testdetails=patient1[v][g]
        
        for i in range(0, len(testdetails)):
            if testdetails[i]=='U':
                num=num+1
        print "number of U:", num
        if num != 0:
                q=["".join(seq) for seq in itertools.product("TF", repeat=num)]
                #print "q:", q
    
    
                
            
                flag = True
                max = -1
                min = 1000
                temp=copy.deepcopy(testdetails)
                for item in range(0, len(q)):
                    index=0
                    for i in range(0, len(testdetails)):
                        if testdetails[i]=='U':
                            temp[i]=q[item][index]
                            index=index+1
                            
                    z=calculation(temp, g)
                    if(flag):
                        max = z
                        min = z 
                        flag = False
                    if max < z:
                        max = z
                    if min > z:
                        min = z
                    #print "question2:", temp, round(z,4)
            
                print "patient", v, "disease", g, "max:", format(max,'.4f')
                print "patient", v, "disease", g, "min:",  format(min,'.4f')
        else:
                print "no u for this patient"


   

"""              
print "diseases: ",number_diseases
print "patients: ",number_patients
print "listofdiseases:", listofdiseases
print "disease1:", disease1, len(disease1)
print "patient1:", patient1, len(patient1)
print "listof_diseases:", listof_diseases

"""


