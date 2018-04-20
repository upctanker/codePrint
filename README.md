# codePrint
一套现场赛代码打印系统，用于 CCPC （或ACM ICPC）比赛打印代码

## 使用说明

### 1.环境准备

以下配置基于ubuntu，其他环境略有不同

项目基于python3 和 django，所以首先进行以下配置。在终端执行以下命令：
```
sudo apt-get install python3-pip
pip3 install django
sudo apt-get install paps
git clone https://github.com/wsc500/codePrint.git
cd codePrint
```
paps 用于支持中文打印

### 2.修改配置文件
编辑print/codePrintSetting.py
```
HOST_IP = "192.168.185.101"
PRINTER_NAME = "HP-LaserJet-P3010-Series"
CODE_PATH = "/home/ccpc/ccpcprint/codes/" #must end with /

#admin setting
ADPASSWORD = "123456"
SHOW_ADMIN_PAGE = True

```
`HOST_IP` 修改为服务器的IP地址

`PRINTER_NAME` 修改为打印机的名称

`CODE_PATH` 是储存选手提交代码的位置，路径可以任意选择，但要注意需要有可读写的权限。CODE_PATH 必须以/结尾

`ADPASSWORD` 是管理员密码，

`SHOW_ADMIN_PAGE` 默认为True,表示开启管理员页面。**在比赛开始后请将其改为`False`,否则可能会被选手看到其他队伍的账号密码**


### 3.启动服务

`sudo python manage.py runserver 0.0.0.0:80`

此时在浏览器输入打印服务器的ip地址即可访问打印系统。

当`SHOW_ADMIN_PAGE`开启时，可以访问 http://HOST_IP/cool 进入管理页面，用于配置每个队伍的账号密码。务必在配置完成后关闭`SHOW_ADMIN_PAGE`

http://HOST_IP 或 http://HOST_IP/print 是选手提交打印的页面

## 代码结构

标准的django项目结构

`printer/templates/printer/index.html`是打印页面前端，如果要修改页面内的文字可以直接在这里修改

`printer/templates/printer/admin.html`是管理页面前端

`printer/views.py`是所有后端逻辑

`print/urls.py`是路由配置



所有提交的代码都会存放在`CODE_PATH`下，命名格式为`队名-时间.print`

## 其他说明

* 支持中文打印
* 这里直接使用了django的runserver作为服务器，没有配置nginx或apache，并且setting.py的debug=true也没有关掉。考虑到现场赛的打印系统是局域网环境，而且比赛期间也不太会有人做坏事，所以这样是最方便的做法。
* 这个系统经过2017年CCPCFinal现场赛的测试，完全扛得住几百支队伍的提交。
* 如果有问题请提Issues，也欢迎贡献Pull Request！

