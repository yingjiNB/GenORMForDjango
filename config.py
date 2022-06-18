# MYSQL
IP = "127.0.0.1"
PORT = 3306
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "test_db"

# 文件路径
g_output_dir = "app/model/"  # 目标文件输出目录
g_output_initfile = f"{g_output_dir}__init__.py"  # 目标文件__init__目录

# 模板文件路径
TEMP_FILE_PATH = './template/orm.template'
TEMP_INIT_PATH = './template/__init__.template'
TEMP_INFO_PATH = './template/info.template'
TEMP_README_PATH = './template/readme.md.template'
TEMP_DB_API_PATH = './template/dbs_api.template'
TEMP_DB_DTO_PATH = './template/dto.template'
TEMP_DB_MAPPER_PATH = './template/mapper.template'

# 导包路径
out_put_dir = g_output_dir.split("/")[0:2]  # ['app', 'model',]
IMPORT_INIT_PATH = f'from {".".join(out_put_dir)}.'  # app.model
