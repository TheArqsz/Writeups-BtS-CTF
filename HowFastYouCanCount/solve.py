# Import socket module 
import socket                
import time 
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 30202
  
# connect to the server on local computer 
s.connect(('ctf.whitehats.pwr.edu.pl', port)) 

result = 'not_changed'
while True: 
# receive data from the server 
    try:
        firstline =  str(s.recv(1024)) 
       #result.append(firstline)
       # print(firstline)
       # firstline = firstline.split('')[1]
        print(firstline)
        arithmetic = firstline.split(' ')[0:3]
        print(arithmetic)
       
	sep=" "
        arithmetic = sep.join(arithmetic)
        result = eval(arithmetic)
        res = repr(result)
        print("res: %s" % res)
        s.send(repr(result).encode())
        
	print(res)
        print(s.recv(4096))
    except KeyboardInterrupt:
        print(result)
    except Exception as e:
        print(e)
        break
        
#    time.sleep(0.01) 

# close the connection 
s.close()  
