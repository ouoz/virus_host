
import paramiko
import warnings

warnings.simplefilter("ignore")

def sshConnect(IP_ADDRESS = "192.168.127.129", 
                USER_NAME = 'kali', 
                KEY_FILENAME = 'password.pem', 
                serverPass="student",
                CMD = 'cd ~ ; ls -l'
                # CMD = "vncserver"
                ):
    # sshクライアントの作成
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.WarningPolicy())
    # 上記で設定したIPアドレス、ユーザー名、キーファイルを渡す
    client.connect(IP_ADDRESS,
                username=USER_NAME,
                password=serverPass,
                timeout=5.0)

    print("")
    print("[*] Launching Twitter prompt ...")
    print("")
    while True:

        CMD = input("Tweet: ")
        if(CMD=="exit"):
            break
        # コマンドの実行
        CMD=r"./go/bin/twty "+CMD
        stdin, stdout, stderr = client.exec_command(CMD)
        # コマンド実行結果を変数に格納
        cmd_result = ''
        for line in stdout:
            cmd_result += line

        # 実行結果を出力
        print(cmd_result)

    # ssh接続断
    client.close()
    del client, stdin, stdout, stderr

