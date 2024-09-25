import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('Housing.csv')
print(data.head())
print(data.dtypes)

numeric_data = data.select_dtypes(include=['number'])

plt.hist(data['area'], bins=30, color='blue', alpha=0.7)
plt.title('Ev Fiyatları vs Alan')
plt.xlabel('Alan')
plt.ylabel('Fiyat')
plt.show()

plt.hist(data['bedrooms'], bins=30, color='green', alpha=0.7)
plt.title('Ev Fiyatları vs Oda Sayısı')
plt.xlabel('Oda Sayısı')
plt.ylabel('Fiyat')
plt.show()

plt.hist(data['stories'], bins=30, color='red', alpha=0.7)
plt.title('Ev Fiyatları vs Kat Sayısı')
plt.xlabel('Kat Sayısı')
plt.ylabel('Fiyat')
plt.show()

avg_price_bathroom = data.groupby('bathrooms')['price'].mean()
avg_price_bathroom.plot(kind='bar', color='purple', alpha=0.7)
plt.title('Banyo Sayısına Göre Ortalama Ev Fiyatları')
plt.xlabel('Banyo Sayısı')
plt.ylabel('Ortalama Fiyat')
plt.show()

avg_price_furnish = data.groupby('furnishingstatus')['price'].mean()
avg_price_furnish.plot(kind='bar', color='orange', alpha=0.7)
plt.title('Eşya Durumuna Göre Ortalama Ev Fiyatları')
plt.xlabel('Eşya Durumu')
plt.ylabel('Ortalama Fiyat')
plt.show()

correlation_matrix = numeric_data.corr()
print(correlation_matrix)

plt.matshow(correlation_matrix, cmap='coolwarm')
plt.colorbar()
plt.title('Korelasyon Matrisi', pad=20)
plt.show()
