#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：李建均
日期：2019/11/20
"""

print("欢迎使用RPSLS游戏")
print("----------------")
player_choice=input("您的选择为:")

def name_to_number(player_choice):
    """
    将游戏对象对应到不同的整数
    """
    if player_choice!="石头" and player_choice!="史波克" and player_choice!="纸" and player_choice!="蜥蜴" and player_choice!="剪刀":
	    print("Error: No Correct Name") 
    if player_choice=="石头":
	    print("你的选择为石头")
    if player_choice=="史波克":
	    print("你的选择为史波克")
    if player_choice=="纸":
	    print("你的选择为纸")
    if player_choice=="蜥蜴":
	    print("你的选择为蜥蜴")
name_to_number(player_choice)
import random
number=random.randint(0,4)
def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:
       return("石头")
    if number==1:
       return("史波克")
    if number==2:
       return("纸")
    if number==3:
       return("蜥蜴")
    if number==4:
       return("剪刀")
comp_choice=number_to_name(number)
print("计算机的选择为%s"%comp_choice)
def rpsls(player_choice,comp_choice):
    if comp_choice==player_choice:
       print("你们二者一样")
    if comp_choice=="纸" and player_choice=="石头":
       print("计算机赢了")
    elif comp_choice=="剪刀" and player_choice=="史波克":
       print("计算机赢了")
    elif comp_choice=="石头" and player_choice=="剪刀":
        print("计算机赢了")
    elif comp_choice=="石头" and player_choice=="蜥蜴":	
        print("计算机赢了")
    elif comp_choice=="蜥蜴" and player_choice=="史波克":
        print("计算机赢了")
    elif comp_choice=="史波克" and player_choice=="蜥蜴":
        print("您赢了")
    elif comp_choice=="石头" and player_choice=="纸":
        print("您赢了")
    elif comp_choice=="纸" and player_choice=="剪刀":
        print("您赢了")
    elif comp_choice=="蜥蜴" and player_choice=="石头":
        print("您赢了")
    elif comp_choice=="剪刀" and player_choice=="石头":
	    print("您赢了")
rpsls(player_choice,comp_choice)

    
