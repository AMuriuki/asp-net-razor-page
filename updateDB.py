import sqlite3

def updateSqliteTable():
	try:
		sqliteConnection = sqlite3.connect('MvcProduct.db')
		cursor = sqliteConnection.cursor()
		print("Connected to SQLite")

		images = ['1.png', '10.png', '1003.png', '11.png', '12.png', '13.png', '14.png', '15.png', '16.png', '17.png', '18.png', '19.png', '2.png', '20.png', '21.png', '22.png', '23.png', '24.png', '25.png', '26.png', '27.png', '28.png', '29.png', '3.png', '30.png', '31.png', '32.png', '33.png', '34.png', '35.png', '36.png', '37.png', '38.png', '39.png', '4.png', '40.png', '41.png', '42.png', '43.png', '45.png', '46.png', '47.png', '48.png', '49.png', '5.png', '50.png', '6.png', '7.png', '8.png', '9.png', 'FGFBD0000031.png', 'FGFBF0000032.png', 'FGFBF0000034.png', 'FGFBF0000035.png', 'FGFBM0000036.png', 'FGFBM0000037.png', 'FGFBM0000039.png', 'FGFBM0004943.png', 'FGFBW0005921.png', 'FGFCD0006064.png', 'FGFCD0006065.png', 'FGFCD0006066.png', 'FGFCF0000048.png', 'FGFCF0000050.png', 'FGFCF0000052.png', 'FGFCF0004762.png', 'FGFCF0004763.png', 'FGFCF0004764.png', 'FGFCF0004765.png', 'FGFCF0004766.png', 'FGFCF0004899.png', 'FGFCF0004900.png', 'FGFCF0004901.png', 'FGFCF0004902.png', 'FGFCM0000059.png', 'FGFCM0000061.png', 'FGFCM0000062.png', 'FGFCM0000064.png', 'FGFCM0004767.png', 'FGFCM0004768.png', 'FGFCM0004769.png', 'FGFCM0004770.png', 'FGFCM0004771.png', 'FGGCD0004043.png', 'FGGCD0004044.png', 'FGMSL0005306.png', 'FGOBF0000076.png', 'FGOBF0000077.png', 'FGOBF0000081.png', 'FGOBF0000082.png', 'FGOBO0000127.png', 'FGOBS0000097.png', 'FGOBS0000098.png', 'FGOCF0000103.png', 'FGOCF0000104.png', 'FGOCF0000105.png', 'FGOCF0000106.png', 'FGOCF0000107.png', 'FGOCF0000109.png', 'FGOCP0000117.png', 'FGOCP0000118.png', 'FGOCP0000119.png', 'FGOCP0000120.png', 'FGOCP0000121 - Copy.png', 'FGOCP0000121.png', 'FGOCS0006137.png', 'FGOCS0006138.png', 'FGOCS0006139.jpg', 'FGOCS0006139.png', 'FGOCS0006140.jpg', 'FGOCS0006140.png', 'FGOCS0006141.jpg', 'FGOCS0006141.png', 'FGSBN0000136.png', 'FGSBN0000137.png', 'FGSBN0000140.png', 'FGSBN0000141.png', 'FGSBN0000860.png', 'FGSBN0004260.png', 'FGSBN0004515.png', 'FGSBN0004516.png', 'FGSBN0005024.png', 'FGSBN0005025.png', 'FGSBP0000148 - Copy.png', 'FGSBP0000148.png', 'FGSBP0000152 - Copy.png', 'FGSBP0000152.png', 'FGSBW0000155 - Copy.png', 'FGSBW0000155.png', 'FGSBW0000156.png', 'FGSBW0000176 - Copy.png', 'FGSBW0000176.png', 'FGSBW0000178.png', 'FGSBW0000179.png', 'FGSBW0006200 - Copy.png', 'FGSBW0006200.png', 'FGSBW0006201.png', 'FGSCD0000158.png', 'FGSCD0000159.png', 'FGSCD0000160.png', 'FGSCD0000163.png', 'FGSCD0000164.png', 'FGSCD0000165.png', 'FGSCD0003768.png', 'FGSCD0003769.png', 'FGSCD0003770.png', 'FGSCD0003771.png', 'FGSCD0003772.png', 'FGSCD0003773.png', 'FGSCD0003774.png', 'FGSCD0003775.png', 'FGSCD0003776.png', 'FGSCD0003777.png', 'FGSCD0003778.png', 'FGSCD0003779.png', 'FGSCD0004529.png', 'FGSCD0004530.png', 'FGSCD0004531.png', 'FGSCD0004532.png', 'FGSCD0004533.png', 'FGSCD0004534.png', 'FGSCD0004535.png', 'FGSCD0004536.png', 'FGSCD0004537.png', 'FGSCD0004538.png', 'FGSCD0004539.png', 'FGSCD0004540.png', 'FGSCD0004576.png', 'FGSCP0005733.png', 'FGSCS0000169.png', 'FGSCS0000170.png', 'FGSCS0000171.png', 'FGSCS0000172.png', 'FGSCS0000173.png', 'FGSCS0003963.png', 'FGSCS0003964.png', 'FGSCS0003965.png', 'FGSCS0003966.png', 'FGSCS0004128.png', 'FGSCS0004129.png', 'FGSCS0004130.png', 'FGSCS0004131.png', 'FGSCS0005178.png', 'FGSCS0005179.png', 'FGSCW0000174.png', 'FGSCW0000175.png', 'FGSCW0000177.png', 'FGSCW0000180.png', 'FGSCW0000181.png', 'FGSCW0003780.png', 'FGSCW0003910.png', 'FGSCW0004124.png', 'FGSCW0004138.png', 'FGSCW0005144.png', 'FGSCW0005180.png', 'FGSLP0005307.png', 'Popco.png', 'Salit-3L.png']
		
		cursor.execute("Select ID from Product")
		records = (cursor.fetchall())
		ids = []
		for record in records:
			remove_chars = str(record).replace(",",'').replace(")","")
			id = remove_chars.replace("(", "")
			ids.append(id)
		i = 0
		_id = 0
		while _id < len(ids):
			for id in ids:
				cursor.execute("UPDATE Product SET image_path = ? WHERE id=?",(images[i], id))
				sqliteConnection.commit()
				i += 1
				_id += 1
				print(id)
				if i == len(images):
					i = 0
		cursor.close()
		print("Records updated successfully")
	except sqlite3.Error as error:
		print(error)
	finally:
		if (sqliteConnection):
			sqliteConnection.close()
			print("The SQLite connection is closed")

updateSqliteTable()
		

