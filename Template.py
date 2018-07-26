#! /usr/bin/env python3
import pyperclip, sys, re, os
#创建 Reducer 模板
def creatReducerModel(className):
	reducerFile = open("./TemplateReducer.swift")
	classNameRe = re.compile(r'<#ClassName#>')
	reducerFileContent = reducerFile.read()
	newReducerContent = classNameRe.sub(className, reducerFileContent)
	
	newReducerFile = desktopPath + className + "Reducer.swift"
	writeFile = open(newReducerFile, 'w')
	writeFile.write(newReducerContent)
	writeFile.close()
#创建普通类模板
def creatNormalClassModel(className):
	classFile = open("./TemplateViewController.swift")
	classFileContent = classFile.read()
	classNameRe = re.compile(r'<#ClassName#>')
	newClassContent = classNameRe.sub(className, classFileContent)
	
	newFile = desktopPath + className + "ViewController.swift"
	writeFile = open(newFile, 'w')
	writeFile.write(newClassContent)
	writeFile.close()
	creatReducerModel(className)
#创建 listView 类模板
def creatListViewClassModel(className,listViewType):
	classFile = open("./TemplateListViewController.swift")
	classFileContent = classFile.read()
	classNameRe = re.compile(r'<#ClassName#>')
	listViewNameRe = re.compile(r'<#ListView#>')
	listViewNameRe1 = re.compile(r'<#listView#>')
	newClassContent = classNameRe.sub(className, classFileContent)
	newListViewContent = listViewNameRe.sub(listViewType.capitalize() + 'View', newClassContent)
	newContent = listViewNameRe1.sub(listViewType+ 'View', newListViewContent)

	newFile = desktopPath + className + "ViewController.swift"
	writeFile = open(newFile, 'w')
	writeFile.write(newContent)
	writeFile.close()
	creatReducerModel(className)
	
#输出路径
desktopPath = os.path.expanduser(r'~/Desktop/')

if len(sys.argv) < 2:
	print("请输入类名以生成模板")
	sys.exit()
if len(sys.argv) == 2:
	#生成普通类
	className = sys.argv[1]
	creatNormalClassModel(className)
elif len(sys.argv) == 3:
	#生成列表类
	listViewName = sys.argv[2]
	if (listViewName != "table") and (listViewName != "collection"):
		print("请输入正确的 listView 类型，比如：table，或者 collection")
		sys.exit()
	else:
		creatListViewClassModel(sys.argv[1], sys.argv[2])
else:
	print("当前不支持传入三个参数，如果有这个需求请提出来")
	sys.exit()
	

	