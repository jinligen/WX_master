#coding=utf-8

# worker 数量
WORKERS = 4
#服务端口
SERVER_PORT = 6789
#接口密码
SECRET = ''
#slave 缺省的取任务数量
TO_SLAVE_COUNT = 500 
#任务最大重试次数
TASK_RETRY = 5 
#finsh set 清理的阀值
TASK_AMOUNT = 2500 
#任务队列
TASK_TODO = 'wx_todo'
#正在做的任务
TASK_DOING = 'wx_doing'
#失败的任务
TASK_FAILED = 'wx_failed'
#完成的任务
TASK_FINISH = 'wx_finish'

#日志目录
LOG_DIR = 'log'
#日志大小M
LOG_SIZE = 20
# 日志文件备份数
LOG_BACKUP = 50

#微信公众号redis配置
REDIS_HOST = ''
REDIS_PORT = ''
REDIS_PWD = ''

#微信公众号pg配置
PG_DB = ''
PG_USER = ''
PG_PWD = ''
PG_HOST = ''
PG_PORT = ''


#群控的redis配置
REDIS_HOST_2 = ''
REDIS_PORT_2 = ''
REDIS_PWD_2 = ''
TASK_QUEUE = ''
RESULT_QUEUE = ''
REDIS_ENCODING = ''


#广州aes加密的地址
AES_URL = ''

