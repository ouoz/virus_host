import receiveIP
import sshConnect

def main():
    IP, USER, PASS = receiveIP.receiveIP()
    sshConnect.sshConnect(IP_ADDRESS=IP, USER_NAME=USER, serverPass=PASS)

if __name__=="__main__":
    main()