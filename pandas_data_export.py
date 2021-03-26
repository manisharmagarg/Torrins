from sqlalchemy import create_engine
import pandas as pd
import pymysql


def read_write_sql():
	engine = create_engine('mysql://root:dev@localhost:3306/torrins', echo=False)
	df = pd.read_sql_query('SELECT menu, slug, sortorder, parent, role, icon, active FROM sidebar_menus', engine)

	print(df.to_dict("recods"))
	# Connect to the database
	connection = pymysql.connect(host='localhost',
			user='root',
			password='dev',
			db='torrins_dev')
	
	# create cursor
	cursor=connection.cursor()
	
	# get columns
	cols = "`,`".join([str(i) for i in df.columns.tolist()])
	
	for index, row in df.iterrows():
		sql = "INSERT INTO `sidebar_menus` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
		print(sql)
		print(tuple(row))
		cursor.execute(sql, tuple(row))
		connection.commit()


if __name__ == '__main__':
	read_write_sql()


