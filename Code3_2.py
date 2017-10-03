def SortedList(List):
    for i in range(0, len(List)):
        for j in range(i, len(List)):
            if List[i] < List[j]:
                temp = List[i]
		List[i] = List[j]
		List[j] = temp
    return List

List=[1,3,5,2,4]
print SortedList(List) 
