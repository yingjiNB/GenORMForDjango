# GenORMForDjango
通过读取数据库反向生成ORM文件

### 安装

> pip install -r requirements.txt



### 用法

1.在config.py文件夹配置正确的数据库连接

```mysql
# MYSQL
IP = "127.0.0.1"
PORT = 3306
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "test_db"
```

2.在table中对comment进行如下格式的编写可以对==choices==支持

![image-20220619001006266](https://i0.hdslb.com/bfs/album/b81505f237814d9014f7882d15073bfe5cb93bbf.png)

3.执行 python genorm.py可在model包下生成对应的orm文件
