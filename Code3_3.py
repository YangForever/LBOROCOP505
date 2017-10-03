from Code3_2 import SortedList
import sys, ast

def MergeAndSort(List1, List2):
    print List1, List2
    List1 = SortedList(List1)
    List2 = SortedList(List2)
    print List1, List2
    List = []
    i = 0
    j = 0
    while i < len(List1) and j < len(List2): 
	if List1[i] >= List2[j]:
	    List.append(List1[i])
	    i+=1
	else:
	    List.append(List2[j])
            j+=1
    if i < len(List1):
	for temp in range(i, len(List1)):
	    List.append(List1[temp])
    if j < len(List2):
	for temp in range(j, len(List2)):
	    List.append(List2[temp])
    return List

List1 = ast.literal_eval(sys.argv[1])
List2 = ast.literal_eval(sys.argv[2])

print MergeAndSort(List1, List2)
