my_set={1,2,3,4}
an_set={3,4,5,6}
temp_set=my_set.intersection(an_set)
print(temp_set)
my_set.difference_update(an_set)
print(my_set)
all_diff_temp_set=my_set.symmetric_difference(an_set)
print(all_diff_temp_set)
my_dic={'name':'hansen','email':'xxx@qq.com'}
temp_key_list=my_dic.keys()
print(temp_key_list)
my_dic.update((["key1","value1"],["key2","value1"]))
print(temp_key_list)
my_dic['gogo']='value3'
my_dic['key1']='value3'
print(my_dic.items())
print(my_dic.fromkeys('value3'))

