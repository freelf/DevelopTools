#!/usr/bin/env python
#coding=utf-8 
import os
import requests
import webbrowser
import subprocess
import shutil

#app所在文件夹,就是 Xcode 中 product文件夹下的.app的全路径。
appProductFileFullPath = '/Users/zhangdongpo/Library/Developer/Xcode/DerivedData/TuWanApp-bnhlkwrmcktnephfyldhiuehhpsf/Build/Products/Debug-iphoneos/TuWanApp.app'
#这两个路径只需要修改用户名就可以
payLoadPath = '/Users/zhangdongpo/Desktop/Payload'
packageBagPath = '/Users/zhangdongpo/Desktop/ProgramBag'
#蒲公英打开的页面url
openUrl = 'https://www.pgyer.com/manager/dashboard/app/69c8aa7b2efdbbdeae93e53ac0b9e31b'


#蒲公英上传必要数据需要自行修改
PGYER_USER_KEY = "4d1927e481e668ffe5dd27f343e6925d"
PGYER_API_KEY = "471161a7b167f2cd8d9f996f70c47e4d"

#上传蒲公英
def uploadIPA(IPAPath):
	if(IPAPath==''):
		print("\n ---------- 没有 IPA 包上传 ----------\n")
		return
	else:
		print("\n----------开始上传到蒲公英----------\n")
		url='http://www.pgyer.com/apiv1/app/upload'
		data={
			'uKey':PGYER_USER_KEY,
			'_api_key':PGYER_API_KEY,
			'installType':'2',
			'password':'',
			'updateDescription':""
		}
		files={'file':open(IPAPath,'rb')}
		r=requests.post(url,data=data,files=files)

def openDownloadUrl():
	webbrowser.open(openUrl,new=1,autoraise=True)
	print ("\n---------- 上传成功 ----------\n")

#打包流程
def bulidIPA():
	
	#删除以前打包的文件夹
	subprocess.call(["rm","-rf",packageBagPath])
	
	#创建PayLoad文件夹
	mkdir(PayLoadPath)
	
	#将编译成功的 Payload 拷贝到 PayLoadPath 路径下
	subprocess.call(["cp","-r",appFileFullPath,PayLoadPath])
	
	#创建 packageBagPath 的文件夹
	subprocess.call(["mkdir","-p",packageBagPath])
	
	#将PayLoadPath文件夹拷贝到 packageBagPath 文件夹
	subprocess.call(["cp","-r",PayLoadPath,packageBagPath])
	
	#删处 PayLoadPath 文件夹
	subprocess.call(["rm","-rf",PayLoadPath])
	
	#切换到 packageBagPath 目录
	os.chdir(packageBagPath)
	
	#压缩 packageBagPath 文件夹下的 PayLoadPath 文件夹夹
	subprocess.call(["zip","-r","./Payload.zip","."])
	print ("\n---------- 打包成功 ----------\n")
	
	#将压缩的文件后缀改为 ipa
	subprocess.call(["mv","Payload.zip","Payload.ipa"])
	
	#删除Payload文件夹
	subprocess.call(["rm","-rf","./Payload"])


#创建PayLoad文件夹
def mkdir(PayLoadPath):
	isExists = os.path.exists(PayLoadPath)
	if not isExists:
		os.makedirs(PayLoadPath)
		print(PayLoadPath + '成功创建')
		return True
	else:
		print (PayLoadPath + '目录已存在')
		return False

#打包获得 ipa
bulidIPA()
#上传到蒲公英
uploadIPA('%s/Payload.ipa'%packageBagPath)
#打开下载网站
openDownloadUrl()


	



	

