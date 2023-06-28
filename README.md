# 操作系统识别方法

该系统可有效区分windows及linux系统，其他系统未适用

Windows请使用以下命令安装python所需模块：

	pip3 import scapy

Linux请使用以下命令安装python所需模块
	
	sudo pip3 import scapy

使用以下命令即可识别操作系统：
	
	python 3 OS_identifu.py [ip地址] [端口号]

	注意：请使用管理员权限运行



若想查看其他系统识别配比，请将main()中的self.get_reault()解除注释。



使用以下命令可对实验室内网络进行批量识别，并生成表格：

	python3 auto.py [端口号]
	
	注意：未进行数据交互者，系统为 unknow
