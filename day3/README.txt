Python运维开发第三天作业，程序名字为ha.py，我的博客地址为http://www.cnblogs.com/zhangxunan/p/5527094.html
1.目录结构
      |--ha.py
day3--|--ha.png
      |--HAProxy.conf
	  |--README
	  
ha.py为主程序，ha.png是流程图，HAProxy.conf是ha的配置文件，README。
2.程序的运行环境及方法
本程序是在CentOS6.5_x86_64下运行的，运行命令为：
[root@localhost ~]# python3 ha.py
3.程序的功能
1）显示节点记录的功能，当你输入节点的名字时，记录会显示出来。
2）增加记录的功能，如果输入的节点不存在，也会创建节点，并把记录添加这个节点下面。
3）删除记录的功能，如果节点下的记录被删除完，那么这个节点也被删除。
4）配置文件备份的功能，当配置文件修改之后，旧的配置文件会改名为配置文件名+ _ + 修改文件的时间
4.如果有任何疑问或bug,请发邮件到zhangxunan5233@163.com或加QQ:1519542593