#!/usr/bin/python3
import pymysql

def save(title, url):
	# 打开数据库连接
	db = pymysql.connect("localhost", "root", "msi;123", "test")
	# 使用cursor()方法获取操作游标 
	cursor = db.cursor()	
	# 使用 execute() 方法执行 SQL，如果表存在则删除
	#cursor.execute("DROP TABLE IF EXISTS RESULT")
	#创建表
	cursor.execute("""CREATE TABLE IF NOT EXISTS RESULT 
		(ID  INT UNSIGNED NOT NULL AUTO_INCREMENT, TITLE CHAR(20), 
		URL CHAR(200), PRIMARY KEY(ID))""")
	# SQL 插入语句
	for each in title:
		sql = "INSERT INTO RESULT(TITLE, URL)\
			VALUES ('%s', '%s')" %\
			(each, url)
		try:
			# 执行sql语句
			cursor.execute(sql)
			# 提交到数据库执行
			db.commit()
		except:
			# 如果发生错误则回滚
			db.rollback()

	# 关闭数据库连接
	db.close()


def read(title):
	# 打开数据库连接
	db = pymysql.connect("localhost", "root", "msi;123", "test")
	# 使用cursor()方法获取操作游标 
	cursor = db.cursor()	
	#sql 查询
	try:
		cursor.execute("SELECT URL FROM RESULT \
			WHERE TITLE = '%s'" % title )
        # 获取所有记录列表
		results = cursor.fetchall()
		#print (results)
		urls = []
		for row in results:
			for col in row:
				urls.append(col)
		if urls:
			return urls
		else:
			return 0
	except:
		print("Read Error")
		return 0

   	# 关闭数据库连接
	db.close()

def empty():
	# 打开数据库连接
	db = pymysql.connect("localhost", "root", "msi;123", "test")
	# 使用cursor()方法获取操作游标 
	cursor = db.cursor()	
	try:
		cursor.execute("SELECT URL FROM RESULT WHERE id = 1 ")
		# 获取所有记录列表
		results = cursor.fetchall()
		if results:
			return 0
		else:
			return 1
	except:
		return 1

if __name__ == '__main__':
	#save("中文", "https://www.baidu.com")
	print(read("山东"))
	#print(empty())