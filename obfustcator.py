first = input("input string")
first = first.replace(" ","")
str_list = ""
numeric_list = ["0","1","2","3","4","5","6","7","8","9"]
operand=["+","-","*","/"]


start = 0
start_idx = 0
front =""
i =0
while(len(first)):
    try :
        #number
        if first[i] in numeric_list:
            if start !=1:
                start =1
            str_list += first[i]
        #operand
        elif first[i] in operand:
            if ((start ==1) and first[i+1] not in numeric_list) or start !=1:
                front += first[i]
            else:
                str_list += first[i]
        #character
        else:
            if start ==1:
                num = eval(str_list)
                front+= str(num)
                first = first[i-1:]
                str_list =""
                start =0
                i=0
            else:
                front += first[i]
        i+=1
    except:
        break

        
print(front)    
       