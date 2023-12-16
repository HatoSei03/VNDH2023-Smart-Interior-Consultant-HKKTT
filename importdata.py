import csv
import mysql.connector

# Mở file CSV
with open('IKEA.csv', 'r') as f:
    reader = csv.reader(f)

    # Tạo kết nối với cơ sở dữ liệu MySQL
    connection = mysql.connector.connect(
        host="localhost",
        port="3306",
        user = "root",
        password="@K2942004",
        database="IKEA")

    # Tạo cursor
    cursor = connection.cursor()

    # Lặp qua các dòng dữ liệu trong file CSV
    for row in reader:
        # Lấy các giá trị của dòng dữ liệu
        itemLink = row[0]
        price = row[1]

        # if price == '0' :
        #     query = f'INSERT INTO IkeaItem (itemID, itemName, category, itemLink, price) VALUES ("{itemID}", "{itemName}", "{category}", "{itemLink}", 0)'
        # else :
        #     price = price[2:]
        #     price_float = float(price)
        #     query = f'INSERT INTO IkeaItem (itemID, itemName, category, itemLink, price) VALUES ("{itemID}", "{itemName}", "{category}", "{itemLink}", {price_float})'

        if price == 0:
            # Tạo lệnh INSERT
            query = f'INSERT INTO IkeaItem (itemLink, itemPrice) VALUES ("{itemLink}", 0)'
        else:
            if price.startswith("SR"):
                price = price[2:]
            price = price.replace(',', '')
            price_float = float(price)
            query = f'INSERT INTO IkeaItem (itemLink, itemPrice) VALUES ("{itemLink}", {price_float})'

        # query = f'INSERT INTO IkeaItem (itemID, itemName, category, itemLink) VALUES ("{itemID}", "{itemName}", "{category}", "{itemLink}")'

        # Thực thi lệnh INSERT
        cursor.execute(query)

    # Lưu thay đổi
    connection.commit()

    # Đóng kết nối
    connection.close()