#coding:gbk
"""
程序:提取黎明破晓的街道中的人物关系
作者:lijianjun
"""
import os
import jieba
import jieba.posseg as pseg
names={}#用来储存姓名和姓名出现的次数的字典
relationships={}#用于储存两个人关系，人名为主键，次数为values的字典
lines=[]#储存每由readlines输出的每一行的名字的列表
#统计人物自己与自己的关系次数
with open("黎明破晓的街道.txt", "r") as file:
    for line in file.readlines():
        line=line.strip("\n")
        words = pseg.lcut(line)#jieba中的pseg用来分词，返回词性
        lines.append([])
        for wo in words:#使用循环向字典中输入数据
            if wo.flag != "nr" or len(wo.word)<2:
                continue#当分词长度小于2或该词词性不为nr(人名)时认为该词不为人名
            lines[-1].append(wo.word)
            if names.get(wo.word) is None:
               names[wo.word]=0
               relationships[wo.word] = {}
            names[wo.word] += 1      
for line in lines:#统计两个名字的关系
    for name1 in line:
        for name2 in line:
            if relationships[name1].get(name2) is None:
               relationships[name1][name2] = 1
               
            else:
                 relationships[name1][name2]= 1+relationships[name1][name2]
with open("similarname.txt", "a") as file3:
    file3.write("id label weight\n")
    for name,times in names.items():
        file3.write(name + " " + name + " " + str(times) + "\n")
#统计人物之间的关系	
with open("黎明破晓的街道.txt", "r") as file2:
    for line in file2.readlines():
        line=line.strip("\n")
        words = pseg.lcut(line)#jieba中的pseg用来分词
        lines.append([])
        for wo in words:#使用循环向字典中输入数据
            if wo.flag != "nr" or len(wo.word)<2:#jieba中的nr用来提取名字
                continue
            lines[-1].append(wo.word)		
            if names.get(wo.word) is None:
               names[wo.word]=0
               relationships[wo.word] = {}
            names[wo.word] += 1       
for line in lines:#统计两个名字的关系
    for name1 in line:
        for name2 in line:
            if relationships[name1].get(name2) is None:
               relationships[name1][name2]= 1              
            else:
                 relationships[name1][name2]= 1+relationships[name1][name2]
with open("relationship.txt", "a") as file2:
    file2.write("source target seight\n")
    for name in relationships.keys():
        for  d,times in relationships.items():
             for a, b in times.items():
                 if b> 11:
                    file2.write(name + " " + a + " " + str(b) + "\n")




			
			
		
