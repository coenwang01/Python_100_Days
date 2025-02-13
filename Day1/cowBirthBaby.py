# 问题描述: 母牛生小牛，从第4年开始生小牛，问第n年一共多少只牛。
# 问题分析
#
#   前提条件：
#         前三年（即第 1、2、3 年）由于小母牛尚未达到生育年龄，因此每年只有 1 头母牛。
#         从第四年开始，每一头母牛每年都会生一头小母牛。也就是说，第 N 年新增的牛数正好等于第 N‑3 年已有的牛数（这些牛在第 N 年达到生育年龄）。
#
#   递推公式：
#         当 N ≤ 3 时，F(N) = 1
#         当 N ≥ 4 时，F(N) = F(N‑1) + F(N‑3)A

def cowBirthBaby(n):
  if n <= 3:
    return 1
  else:
    return cowBirthBaby(n-1) + cowBirthBaby(n-3)

print("请输入年份:")
n = int(input())
print("第", n, "年有", cowBirthBaby(n), "头牛.")

