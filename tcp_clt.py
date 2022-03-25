import socket

target_host = ' ' # insert target host here
target_post = 80

# create a socket object 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_post))

client.send(b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n')

response = client.recv(4096)

print(response.decode())
client.close()
