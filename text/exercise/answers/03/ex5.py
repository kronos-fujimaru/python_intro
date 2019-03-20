price = 1500   # 書籍の値段
tax = 0.08     # 税率

# 税込金額を計算
including = price * (1 + tax)
print("金額は、" + str(including) + "円です。")
