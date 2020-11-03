inp_str = str(input())
res = [inp_str[i: j] for i in range(len(inp_str)) 
          for j in range(i + 1, len(inp_str) + 1)]
temp = []
min_val = len(set(inp_str))
for i in res:
    if len(i) >= min_val and len(set(i))  == min_val:
        temp.append(i)
cou_ = len(inp_str)
for i in temp:
    cou_ = min(cou_,len(i))
print(cou_)
