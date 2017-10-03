def MeanFunc(List):
    sum = 0
    for i in range(0, len(List)):
        sum += List[i]
    return (sum+0.0)/len(List)

List = [1,2,3,4,5]
print List
print MeanFunc(List)
