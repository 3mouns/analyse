import pandas as pd

data = pd.read_csv('tmall_order_report.csv')
print(data.head())  
print(data.tail())  
print(data.info())
print(data.describe())
import matplotlib.pyplot as plt
import seaborn as sns

# 绘制柱状图
plt.bar(data['category'], data['value'])
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart of Value by Category')
plt.show()

# 绘制折线图
plt.plot(data['date'], data['sales'])
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Trend over Time')
plt.xticks(rotation=45)
plt.show()

# 绘制散点图
sns.scatterplot(x='x_variable', y='y_variable', data=data)
plt.xlabel('X Variable')
plt.ylabel('Y Variable')
plt.title('Scatter Plot of X vs Y')
plt.show()
# 删除包含缺失值的行
data_cleaned = data.dropna()

# 使用均值填充数值型列的缺失值
data['column_name'].fillna(data['column_name'].mean(), inplace=True)
grouped_data = data.groupby('category')['value'].sum()
print(grouped_data)
correlation_matrix = data.corr()
print(correlation_matrix)
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 选择特征列和目标列
X = data[['feature1', 'feature2']]
y = data['target']

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建并训练线性回归模型
model = LinearRegression()
model.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = model.predict(X_test)
from sklearn.metrics import mean_squared_error, mean_absolute_error

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print('Mean Squared Error:', mse)
print('Mean Absolute Error:', mae)
