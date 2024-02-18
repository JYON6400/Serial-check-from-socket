import socket
import csv
import os
import threading
import sys

def handle_client(conn, addr):
    print('Connected by', addr)
    data = conn.recv(1024).decode()  # データを受信
    line_name, product_number, serial_number = parse_data(data)
    if write_to_csv(line_name, product_number, serial_number):
        conn.sendall(b"OK: Serial number written to CSV.")
    else:
        conn.sendall(b"NG: Serial number is smaller than existing serial numbers in CSV.")
    conn.close()

def receive_data():
    # ソケットを作成して待機
    HOST = '127.0.0.1'
    PORT = 12345
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Opne>--",HOST,":",PORT)
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

def parse_data(data):
    # ライン名、品番、シリアル番号を抽出
    line_name, product_number, serial_number = data.split(',')
    return line_name.strip(), product_number.strip(), serial_number.strip()
   

def write_to_csv(line_name, product_number, serial_number):
    # フォルダとCSVファイルのパスを作成
    folder_path = os.path.join(os.getcwd(), line_name)
    os.makedirs(folder_path, exist_ok=True)
    csv_file_path = os.path.join(folder_path, f"{product_number}.csv")

    # CSVファイル内のシリアル番号をチェック
    if os.path.exists(csv_file_path):
        with open(csv_file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and convert_to_decimal(row[0]) >= convert_to_decimal(serial_number):
                    SOCKNUM = convert_to_decimal(row[0])
                    CSVNUM  = convert_to_decimal(serial_number)
                    print('NG', SOCKNUM,'<',CSVNUM)
                    return False  # 書き込むシリアル番号がCSV内の番号よりも小さい

    # CSVファイルにデータを書き込む
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([serial_number])
        print('OK', )
    return True  # 書き込むシリアル番号がCSV内の番号よりも大きい

def convert_to_decimal(serial):
    # シリアル番号を10進数に変換する関数
    decimal_value = 0
    for char in serial:
        if char.isdigit():
            decimal_value = decimal_value * 36 + int(char, 36)
        else:
            decimal_value = decimal_value * 36 + ord(char.upper()) - ord('A') + 10
    return decimal_value

if __name__ == "__main__":
    try:
        receive_data()
    except KeyboardInterrupt:
        print("サーバーを終了します。")
        sys.exit(0)
    
