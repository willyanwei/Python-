
<数据分析步骤>  
	通过案例来看看学数据分析挖掘、机器学习还需要学哪些知识点

	<0. 明确数据分析的目标 >
		想要得到的分析结果是什么样的？ 
	</0. 明确数据分析的目标>
		
	<1. 获取数据>  
		1.1 本地的csv文件    （kaggle、 阿里天池）
			import pandas as pd
			data1 = pd.read_csv()
			Pandas用及其简单的代码，完成读取数据的功能
		
		1.2 关系型数据库	（mysql、sqlite）  数据库SQL语句  
			0. import pymysql库（遇到不熟悉的数据库，可以先了解下是否有python支持的包）
			1. 定义Query_Mysql()函数
			2. 配置mysql数据库连接信息
			3. 编写sql查询语言
			4. 执行Query_Mysql()函数
			
		1.3 大数据数据仓库	（大数据hive数据仓库）spark表
			0. import pyhive/impala
			1. 定义Query_Hive()函数
			2. 配置hive数据库连接信息
			3. 编写sql查询语言
			4. 执行Query_Hive()函数		
					
		以上内容， 从数据库中读取数据，那么如何将数据导入到数据库中呢？
		<书写函数>
		
		Query_mysql  导出数据库
		import_mysql  导入数据库
		
		</书写函数>
		
		<书写类>
		结合之前讲的Python的类、函数等知识点，可以优化代码：
			import pymysql
			import pandas as pd
			from sqlalchemy import create_engine

			class PyMysql(object):
				'''
				使用mysql进行数据的输入输出
				'''
				def __int__(self):
					pass

				def mysql2csv(self, DSN, sql):
					conn = pymysql.connect(
						host=DSN["host"],
						port=DSN["port"],
						database=DSN["database"],
						user=DSN["user"],
						password=DSN["password"])
					cursor = conn.cursor()
					# 去掉sql结尾的；号，不然会报错
					cursor.execute(sql.rstrip("").rstrip("\n").rstrip("").rstrip(";"))
					data = list(cursor.fetchall())

					# 列名
					col_name_list = [tuple[0] for tuple in cursor.description]
					df = pd.DataFrame(data, columns=col_name_list)
					conn.commit()
					cursor.close()
					conn.close()
					print('导出成功')
					return df

				def csv2mysql(self, DSN, table_name, path, sheetname):
					# 数据库连接信息
					host = DSN["host"],
					port = DSN["port"],
					database = DSN["database"],
					user = DSN["user"],
					password = DSN["password"]

					data = pd.read_excel(path, sheet_name=sheetname)
					engine = create_engine("mysql+pymysql://{user}:{password}@{host}:{port}/{database}".format(**DSN),
										   max_overflow=5)
					data.to_sql(table_name, engine, index=False, if_exists='replace', )
					print('导入成功...')


			# 数据库连接信息
			DSN = {
				"host": "localhost",
				"port": 3306,
				"database": "dbmanual",
				"user": "root",
				"password": "123456"
			}


			# 数据的导出
			sql = """show tables;"""

			PM = PyMysql() # 通过类定义对象PM
			# data1 = PM.Query_Mysql(DSN, sql)
			# print(data1)
			#
			# data1.to_csv('tmp.csv')

			# 表名
			# 如果不存在表，则自动创建
			table_name = '数据操作'
			# 文件路径
			path = r'D:\数据库\SQL速查手册.xlsx'
			sheetname = table_name

			PM.csv2mysql(DSN, table_name, path,  sheetname)
			</书写类>
			
			
		<书写库>
			第三方库的存放目录
			D:\ProgramData\Anaconda3\Lib\site-packages
			
			自定义的库，通过调用库的形式导入方法，
			首先要新建自己的库文件： 
				import pymysql
				import pandas as pd
				from sqlalchemy import create_engine


				class PyMysql(object):
					'''
					使用mysql进行数据的输入输出

					'''
					def __int__(self):
						pass

					def mysql2csv(self, DSN, sql):
						conn = pymysql.connect(
							host=DSN["host"],
							port=DSN["port"],
							database=DSN["database"],
							user=DSN["user"],
							password=DSN["password"])
						cursor = conn.cursor()
						# 去掉sql结尾的；号，不然会报错
						cursor.execute(sql.rstrip("").rstrip("\n").rstrip("").rstrip(";"))
						data = list(cursor.fetchall())

						# 列名
						col_name_list = [tuple[0] for tuple in cursor.description]
						df = pd.DataFrame(data, columns=col_name_list)
						conn.commit()
						cursor.close()
						conn.close()
						print('导出成功')
						return df

					def csv2mysql(self, DSN, table_name, path, sheetname):
						# 数据库连接信息
						host = DSN["host"],
						port = DSN["port"],
						database = DSN["database"],
						user = DSN["user"],
						password = DSN["password"]

						data = pd.read_excel(path, sheet_name=sheetname)
						engine = create_engine("mysql+pymysql://{user}:{password}@{host}:{port}/{database}".format(**DSN),
											   max_overflow=5)
						data.to_sql(table_name, engine, index=False, if_exists='replace', )
						print('导入成功...')			
			
			调用库文件，实现数据导入导出功能

				import aaywcustom.ywmysql.pymysql as pm

				DSN = {
					"host": "localhost",
					"port": 3306,
					"database": "dbmanual",
					"user": "root",
					"password": "123456"
				}

				'''数据的导出
				'''


				# sql = """show tables;"""
				#
				# PM = pm.PyMysql()
				# data1 = PM.mysql2csv(DSN, sql)
				# print(data1)

				# data1.to_csv('tmp.csv')
				#
				#
				'''数据导入到数据库'''
				# 表名
				# 如果不存在表，则自动创建
				table_name = '连接与断开服务器'
				# 文件路径
				path = r'D:\数据库\SQL速查手册.xlsx'

				sheetname = table_name

				PM = pm.PyMysql()
				PM.csv2mysql(DSN, table_name, path, sheetname)
			
		</书写库>
		
		<setuptools分发打包>
			setuptools：进行分发打包，课后查阅资料
		</setuptools分发打包>
 		
		把以上三种数据源，通过pandas，转换成dataframe（pandas的数据类型），通过python进行数据分析挖掘
		
		
		<补充SQL教程>
			我们学习SQL的目前是从各种数据库中读取到数据，这里主要学习如何连接数据库，并使用 select语句查询数据； 其他的交给Python。
			
			<安装数据库>
				自行安装mysql， dbeaver			
			</安装数据库>
		
			<连接数据库>
				一、设置远程登录	
				1.使用“mysql -uroot -p”命令可以连接到本地的mysql服务。
				2.使用“use mysql”命令，选择要使用的数据库，修改远程连接的基本信息，保存在mysql数据库中，因此使用mysql数据库。
				3. 使用“GRANT ALL PRIVILEGES ON *.* TO \'root\'@\'%\' IDENTIFIED BY \'root\' WITH GRANT OPTION;”命令可以更改远程连接的设置（用户名和密码自己定义）。
				4. 使用“flush privileges;”命令刷新刚才修改的权限，使其生效。
				5. 使用“select host,user from user;”查看修改是否成功。"
				
				二、 通过Dbeaver软件，登录数据库，登录信息如下： 
				host='localhost',
                user='root',
                password='123456',# 在安装的时候进行设置，要记住他
			</连接数据库>
			
			<进入数据库>
				# 查看有哪些数据库
				show databases; 

				# 进入指定的数据库
				use covid19;
				
				# 查看已进入的数据库中有哪些表
				show tables;				
			</进入数据库>
			
			<select查询>
				选定数据库有中的目标表进行select查询
			
				SELECT 字段列表 FROM 表名[ 其他子句]
				万能公式： 
				SELECT [ALL|DISTINCT] select_expr 				
				FROM -> 
				WHERE -> 
				GROUP BY [合计函数] -> 
				HAVING -> 
				ORDER BY -> 
				LIMIT

				0. DISTINCT, ALL 选项
					DISTINCT 去除重复记录
					默认为 ALL, 全部记录"
				
				1. select_expr
					-- 可以用 * 表示所有字段。
						SELECT * FROM tb;
					-- 可以使用表达式（计算公式、函数调用、字段也是个表达式）
						SELECT stu, 29+25, NOW() FROM tb;
					-- 可以为每个列使用别名。适用于简化列标识，避免多个列标识符重复。
						- 使用 AS 关键字，也可省略 as.
						SELECT stu+10 AS add10 FROM tb;
						
				2. FROM 子句
					用于标识查询来源。
					-- 可以为表起别名。使用as关键字。
						SELECT * FROM tb1 AS tt, tb2 AS bb;
					-- from子句后，可以同时出现多个表。
						-- 多个表会横向叠加到一起，而数据会形成一个笛卡尔积。
						SELECT * FROM tb1, tb2;
					-- 向优化符提示如何选择索引
						USE INDEX、IGNORE INDEX、FORCE INDEX
						SELECT * FROM table1 USE INDEX (key1,key2) WHERE key1=1 AND key2=2 AND key3=3;
						SELECT * FROM table1 IGNORE INDEX (key3) WHERE key1=1 AND key2=2 AND key3=3;"
				3. "WHERE 子句
					-- 从from获得的数据源中进行筛选。
					-- 整型1表示真，0表示假。
					-- 表达式由运算符和运算数组成。
						-- 运算数：变量（字段）、值、函数返回值
						-- 运算符：
							=, 《=》, 《》, !=, 《=, 《, 》=, >, !, &&, ||,
							IN (NOT) NULL, (NOT) LIKE, (NOT) IN, (NOT) BETWEEN AND, IS (NOT), AND, OR, NOT, XOR
							IS/IS NOT 加上ture/FALSE/unknown，检验某个值的真假
							《=》与《》功能相同，《=》可用于null比较"
				4. "GROUP BY 子句, 分组子句
					GROUP BY 字段/别名 [排序方式]
					分组后会进行排序。升序：ASC，降序：DESC

					以下[合计函数]需配合 GROUP BY 使用：
					COUNT 返回不同的非NULL值数目  COUNT(*)、count(字段)
					SUM 求和
					MAX 求最大值
					MIN 求最小值
					AVG 求平均值
					GROUP_CONCAT 返回带有来自一个组的连接的非NULL值的字符串结果。组内字符串连接。"
					
				5. "HAVING 子句，条件子句
					与 WHERE 功能、用法相同，执行时机不同。
					WHERE 在开始时执行检测数据，对原数据进行过滤。
					HAVING 对筛选出的结果再次进行过滤。
					HAVING 字段必须是查询出来的，where 字段必须是数据表存在的。
					WHERE 不可以使用字段的别名，having 可以。因为执行WHERE代码时，可能尚未确定列值。
					WHERE 不可以使用合计函数。一般需用合计函数才会用 HAVING
					SQL标准要求HAVING必须引用GROUP BY子句中的列或用于合计函数中的列。"
					
				6. "ORDER BY 子句，排序子句
					ORDER BY 排序字段/别名 排序方式 [,排序字段/别名 排序方式]...
					升序：ASC，降序：DESC
					支持多个字段的排序。"
					
				7. "LIMIT 子句，限制结果数量子句
					仅对处理好的结果进行数量限制。将处理好的结果的看作是一个集合，按照记录出现的顺序，索引从0开始。
					LIMIT 起始位置, 获取条数
					省略第一个参数，表示从索引0开始。limit 获取条数"				
			</select查询>	
		</补充SQL教程>
	
	</1. 获取数据> 
	
	<2. 理解数据>
	（根据数据资产表，了解数据的含义）
		数据资产表（vonr数据资产表）-> 大数据平台运维、开发人员获取 
	</2. 理解数据>	
	
	<3. 分析数据>  
		广义上讲，统称数据分析
		狭义上讲 数据分析分为：  数据分析和数据挖掘
		
			
		Python的数据科学库：  
		数据分析： Numpy Pandas 
		机器学习： skleran
		数据可视化： Pyechart matplotlib（serborn）
	</3. 分析数据>	
	
</数据分析步骤>
	
<狭义上的数据分析>	
	<疫苗接种率案例>
		数据分析需要用到哪些Python库函数？  
		1. pandas： 用到的库函数 ：  20221115
		read_csv、 data1['country']
		data1.dropna
		data1.isna() data1.all()
		data1.iloc[-1]
		pd.DataFrame
		data.to_csv()
		ranking2['people_fully_vaccinated_per_hundred'] 《= 100
		data.values
		
		2. numpy: np.unique(),np.array   20221108 
		
		3. matplotlib/serborn/pyecharts  20221122
		
		Pandas的 API使用，API：封装好的方法 
					
	</疫苗接种率案例>
</狭义上的数据分析>	


<狭义上的数据挖掘>  机器学习
	<泰坦尼克号生存预测>

		1. CRISP-DM (cross-industry standard process for data mining), 即为"跨行业数据挖掘标准流程"。
			
			1. 商业理解（business understanding）： 判断泰坦尼克号上的乘客是否能够生存下来
			
			2. 数据理解（data understanding）： 探索性数据分析（EDA）
			
			3. 数据准备（data preparation）： 数据获取、数据清洗、数据训练集、验证集、测试集（20221206）		
					
			4. 建模（modeling）评估（evaluation）
			构建特征工程，数据的特征缩放（标准化或者归一化）
			选择模型、训练、评估
			超参数调优
			
			5. 部署（deployment）模型实施
			基于调优后的模型进行预测，在训练集上得到的参数应用到测试集中
								
		2. 泰坦尼克号生存预测案例中涉及到的python数据科学库： 
			2.1 Pandas： 
			df_test.head()
			df_train.info()
			df_train.shape
			分箱： pandas.cut
			分解类别属性: pandas.get_dummies
			dataframe.corr()
			
			2.2 sklearn.model_selection 
			train_test_split 
			K-Folds cross-validator
			sklearn.model_selection import GridSearchCV
			list1 = 1,2,3,4,5
			list2 = 6,7,8,9,10
			
			
			2.3 seaborn
			sns.heatmap
		
	</泰坦尼克号生存预测>
</狭义上的数据挖掘>























