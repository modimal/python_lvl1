# coding: utf-8

list1 = input("Введите первый список фруктов, через запятую: ").replace(" ", "").lower().split(",")
list2 = input("Введите второй список фруктов, через запятую: ").replace(" ", "").lower().split(",")

cross_list = [x for x in list1 if x in list2]

print(cross_list)
