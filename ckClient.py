#coding:utf-8
from clickhouse_driver import Client
from readHdfsFiles import readFiles
import argparse
import datetime
#clickhouse工具类，封装clickhouse操作
class ckClient(object):
    def __init__(self,host='localhost',port=9000,user='default',password=''):
        self.client=Client(host='localhost',port=9000,user='default',password='',
                           database='bigdata')
    #插入数据
    def insert(self,sql):
        print(self.client.execute(sql))

#将数据转化为相应的格式
def valueTockValue(file,types):
    for i in range(len(file)):
        for j in range(len(file[i])):
            if types[j].lower() in "int":
                file[i][j]=int(file[i][j].split('.')[0])
            elif types[j].lower() in 'date':
                file[i][j] = datetime.datetime.strptime(file[i][j], "%Y-%m-%d").date()
            elif types[j].lower() in "float":
                file[i][j] = float(file[i][j])
            elif types[j].lower() in "double":
                file[i][j] = float(file[i][j])
            else:
                file[i][j] = str(file[i][j])
    return file
if __name__=='__main__':
    parse=argparse.ArgumentParser(usage="it's usage tip.",description="help info.")#创建解析对象
    parse.add_argument("--fileuri","-f",help="hdfs中文件路径(包含ip,port),例如：hdfs://localhost:9000/user/cb/data/dm")
    parse.add_argument("--ip","-ip",help="clickhouse节点ip")
    parse.add_argument("--port","-P",default=9000,help="clickhouse native端口，默认9000")
    parse.add_argument("--username","-u",default='default',help="clickhouse用户名，默认default")
    parse.add_argument("--password","-p",default='',help="clickhouse用户密码，默认为空")
    parse.add_argument("--database","-d",default='bigdata',help='需要导入的目标数据库')
    parse.add_argument("--table","-t",help='需要导入的数据库名')
    parse.add_argument("--columns","-cs",help='目标数据库列名')
    parse.add_argument("--types","-cts",help='目标数据库列类型')
    parse.add_argument("--partition_name","-pt",help='分区值')
    args=parse.parse_args()
    ck=ckClient()
    file=readFiles('{}'.format(args.fileuri),args.partition_name)
    file=valueTockValue(file,args.types.split(','))
    ck.client.execute("insert into {}.{} ({}) values ".format(args.database,args.table,args.columns),
                      file,types_check=True)