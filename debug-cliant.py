import socket

def send_data(data):
    HOST = '127.0.0.1'  # サーバーのIPアドレス
    PORT = 12345        # サーバーのポート番号
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(data.encode())
        response = s.recv(1024).decode()  # 応答を受信
        print("サーバーからの応答:", response)

if __name__ == "__main__":
    line_name = "Line2"
    product_number = "Product1"
    serial_number = "0000020"
    
    data = f"{line_name},{product_number},{serial_number}"
    send_data(data)
