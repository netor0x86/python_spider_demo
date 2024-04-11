from sklearn.linear_model import LinearRegression

# 离市中心的距离
distances = [[1.0], [2.0], [3.0], [4.0], [5.0], [6.0], [7.0], [8.0], [9.0], [10.0]]

# 对应的房子的单价
prices = [10.14, 9.89, 8.41, 9.61, 7.95, 7.46, 6.62, 5.23, 4.70, 4.77]

# 创建并训练线性回归模型
model = LinearRegression()
model.fit(distances, prices)

# 预测离市中心距离为 15 的房子的单价
predicted_price11 = model.predict([[11]])
predicted_price12 = model.predict([[12]])
predicted_price13 = model.predict([[13]])
predicted_price14 = model.predict([[14]])
predicted_price15 = model.predict([[15]])
predicted_price20 = model.predict([[20]])

print("预测离市中心距离为 11 的房子的单价是:", predicted_price11[0])
print("预测离市中心距离为 12 的房子的单价是:", predicted_price12[0])
print("预测离市中心距离为 13 的房子的单价是:", predicted_price13[0])
print("预测离市中心距离为 14 的房子的单价是:", predicted_price14[0])
print("预测离市中心距离为 15 的房子的单价是:", predicted_price15[0])
print("预测离市中心距离为 20 的房子的单价是:", predicted_price20[0])
