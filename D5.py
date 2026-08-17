import csv
# with open('score.csv','r',encoding='utf-8')as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

score=[]
with open('score.csv','r',encoding='utf-8')as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        score.append(int(row[-1]))
    print(score)

average_score = sum(score)/len(score)
max_score=max(score)
min_score=min(score)
print(f'average_score={average_score}',f'max_score={max_score}',f"min_score={min_score}")

with open('score.csv','r',encoding='utf-8')as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if max_score==int(row[-1]):
            print(f"获得最高分的是{row[0]}")


# # dict法

# scores_dict={}
# with open('score.csv','r',encoding="utf-8") as f:
#     reader = csv.reader(f)
#     next(reader)
#     for row in reader:
#         name = row[0]
#         score = int(row[-1])
#         scores_dict[name] = score

# print(scores_dict)

# max_name = max(scores_dict,key=scores_dict.get)
# max_score = scores_dict[max_name]
# print(f"{max_name}get{max_score}points")