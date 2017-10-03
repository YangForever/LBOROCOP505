import sys, ast
def MeanFunc(List):
    sum = 0
    for i in range(0, len(List)):
        sum += List[i]
    return (sum+0.0)/len(List)

List = ast.literal_eval(sys.argv[1])
print List
print MeanFunc(List)
