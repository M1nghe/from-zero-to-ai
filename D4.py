def is_prime(n):
   if n <=1:
      return False
   for i in range(2,n):
      if n % i == 0:
         return False
   return True

print(is_prime(10))

# def reverse_str(s):
#     new_s=''
#     for ch in s:
#         new_s=ch + new_s
#     return new_s

# print(reverse_str("My name"))

# def dedupe(lst):
#     result = []
#     for ch in lst:
#         if ch not in result:
#             result.append(ch)
#     return result

# print(dedupe([1, 2, 2, 3, 3, 3, 4]))

#  类型: str
#   是什么: 一串字符，不可变
#   能做什么: s[i] 读、s[1:3] 切片、.upper() .split() .replace()
#   不能做什么: 不能 s[0]="x" 改、没有 .append()
#   ────────────────────────────────────────
#   类型: list
#   是什么: 一串东西，可变
#   能做什么: lst[i] 读/写、.append() .remove() .pop()
#   不能做什么: 元素能改，这是它和 str 最大的区别
#   ────────────────────────────────────────
#   类型: dict
#   是什么: 键值对，按 key 找
#   能做什么: d["name"]、.get() .keys() .items()
#   不能做什么: 不能 d[0]（除非 key 正好是 0）
#   ────────────────────────────────────────
#   类型: int/float
#   是什么: 一个数
#   能做什么: 算术运算
#   不能做什么: 没有下标、没有 .append()、啥方法都没有