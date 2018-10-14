#! /usr/bin/python3
# -*- coding:utf-8 -*-
import sys
import os
import shutil


def parseParam(param):
    """解析输入的参数，获取生成项目的路径"""
    if len(param) < 3:
        print("wrong command!\ncommand format is init-project projectName [-d path]")
        return None

    if param[1] == "init-project":
        if len(param) == 3:
            return param[2], os.getcwd()
        elif len(param) == 5:
            if param[3] == "-d":
                return param[2], param[4]
            else:
                print("wrong parameter!\ncommand format is init-project projectName [-d path]")
                return None
        else:
            print("wrong command!\ncommand format is init-project projectName [-d path]")
            return None
    else:
        print("wrong command!\ncommand format is init-project projectName [-d path]")
        return None


def copyProject(path):
    """复制项目模板到指定路径"""
    print("coping project,wait seconds...")
    shutil.copytree(os.path.join(os.getcwd(), "ProjectTemplate"), path)
    print("copy is over")


def changeFileContent(name, oldKey, newKey):
    """替换文件中的oldKey为newKey"""
    with open(name, "r", encoding='gbk', errors="ignore") as f:
        s = f.read()
        s2 = s.replace(oldKey, newKey)

    with open(name, "w", encoding='gbk', errors="ignore") as f:
        f.write(s2)


def changeName(name, path):
    """修改项目名称"""
    print("changing project name,wait seconds...")
    newName = name + "App"
    # 修改项目名称
    simplePath = os.path.join(path, name, "Projects", "zstack", "Samples")
    os.rename(os.path.join(simplePath, "GenericApp"), os.path.join(simplePath, newName))

    # Generic
    path1 = os.path.join(simplePath, newName, "Source")
    for f in os.listdir(path1):
        changeFileContent(os.path.join(path1, f), "Generic", name)
        fileName = os.path.splitext(f)[0]
        fileExtension = os.path.splitext(f)[1]
        newFileName = fileName.replace("Generic", name)
        os.rename(os.path.join(path1, f), os.path.join(path1, newFileName + fileExtension))

    path2 = os.path.join(simplePath, newName, "CC2530DB")
    for f in os.listdir(path2):
        changeFileContent(os.path.join(path2, f), "Generic", name)
        fileName = os.path.splitext(f)[0]
        fileExtension = os.path.splitext(f)[1]
        newFileName = fileName.replace("Generic", name)
        os.rename(os.path.join(path2, f), os.path.join(path2, newFileName + fileExtension))


if __name__ == '__main__':
    result = parseParam(sys.argv)
    if result is not None:
        targetPath = os.path.join(result[1], result[0])
        copyProject(targetPath)
        changeName(result[0], result[1])
        print("project created success")
