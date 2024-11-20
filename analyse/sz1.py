

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data = pd.read_csv('C:/Users/86199/AppData/Local/Programs/Python/Python39/analyse/双十一淘宝美妆数据.csv')
print('数据基本信息：')
data.info()
print('数据的前几行：')
print(data.head())
# 提取日期
data['Day'] = data['update_time'].str.split(' ').str[0]

# 可视化各日的订单数排行
plt.rcParams['figure.dpi'] = 300
plt.rcParams['axes.unicode_minus'] = False

# 设置中文编码
plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']

# 统计各日的订单数
daily_counts = data['Day'].value_counts().reset_index(name='销售数量')

# 获取前 20 条数据
top_20_name = daily_counts.head(20)

# 绘制柱状图
plt.figure(figsize=(10, 6))
bars = sns.barplot(data=top_20_name, x='Day', y='销售数量')

# 添加数据标签
for bar in bars.patches:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 5, int(height), ha='center', va='bottom')

# 设置标题和标签
plt.title('日销售排行')
plt.xlabel('日期')
plt.xticks(rotation=90)
plt.ylabel('销售数量')

# 显示图形
plt.show()
# 统计各类美妆的总销售数量
total_sale = data.groupby('title')['sale_count'].sum()

# 提取品牌名
data['品牌名'] = data['title'].str.split('/').str[0]

# 统计各类美妆品牌的总销售数量
brand_total_sale = data.groupby('品牌名')['sale_count'].sum()

# 获取排行前 10 品牌名
top_10_brand = brand_total_sale.nlargest(10).reset_index()

# 筛选获得数据
merged_data = pd.merge(top_10_brand, data, on='品牌名')

# 绘制柱状图
plt.figure(figsize=(5, 10))
sns.barplot(data=top_10_brand, x='sale_count', y='品牌名')

# 添加数据标签
for i, v in enumerate(top_10_brand['sale_count']):
    plt.text(v, i, str(v), fontsize=8, ha='right', va='center')

# 设置轴标签和标题
plt.xlabel('销售数量')
plt.xticks(rotation=45)
plt.ylabel('品牌名')
plt.title('美妆品牌销售数量排行')

# 显示图形
plt.show()
