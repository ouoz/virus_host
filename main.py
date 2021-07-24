import receiveIP
import sshConnect

def main():
    IP = receiveIP.receiveIP()
    sshConnect.sshConnect(IP)

if __name__=="__main__":
    main()