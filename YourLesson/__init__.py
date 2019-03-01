import requests
from . import item


session = requests.session()
vode_item = item.VodeItem()
login_item = item.LoginItem()
batch_item = item.BatchItem()

# 初始化登录
print("正在初始化登录...")
from . import login
login.login()
login.bash_open()
print("登录已经完成")
