_author__ = 'qindongliang'
#导入pymysql的包
import pymysql
class SqlHelpter:
    def insert(self,title,url,content=""):
        conn=pymysql.connect(host='localhost',user='root',passwd='admin',db='test',port=3306,charset='utf8')
        cur=conn.cursor()
        try:
            count=cur.execute("insert into dug(title,url,content) values(%s,%s,%s)",(title,url,content))
        except Exception:
            print("")
        finally:
            count=cur.execute("insert into dug(title,url,content) values(%s,%s,%s)",(title,url,content[0:2000]))
        cur.close();
        conn.commit()
        conn.close();
        return count

