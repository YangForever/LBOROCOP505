import time
DateTime = {}
Str = raw_input("Please input a date in format YY-MM-DD: ")
struct_time = time.strptime(Str, "%Y-%m-%d")
#time_tuple = (struct_time)
print struct_time
time_tuple = (struct_time.tm_mday, struct_time.tm_mon,struct_time.tm_year)
print time_tuple
time_dic = {"Year":struct_time.tm_year, "month":struct_time.tm_mon, "day":struct_time.tm_mday}
print time_dic
