# 					测试数据库设计
## 1.测试表(t_test)


| 代码 | 数据类型 | 主键 | 备注 | 默认值 |
| - | - | - | - | - |
| F_id|int(11)|Y||None|
| F_test_no|varchar(64)||测试编号||
| F_test_code|varchar(64)||测试代码||
| F_test_name|varchar(64)||测试名称||
| F_gender|int(11)||性别 enum:0,female,女#1,male,男#2,other,其他|0|
| F_deleted|varchar(1)||删除标记 0-否 1-是|0|
| F_operator|varchar(32)||操作员||
| F_create_time|bigint(20)||创建时间戳 单位秒|0|
| F_modify_time|bigint(20)||更新时间戳 单位秒|0|


唯一索引:  F_id

唯一索引:  F_test_code

普通索引:  F_modify_time



