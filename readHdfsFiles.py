#coding:utf-8
from pyspark import SparkContext

#读取hdfs文件
def readFiles(uri,dt):
    sc=SparkContext("local")
    lines=sc.textFile(uri)
    datas=lines.map(lambda line:(line+'\001{}'.format(dt)).split("\001"))
    return datas.collect()
