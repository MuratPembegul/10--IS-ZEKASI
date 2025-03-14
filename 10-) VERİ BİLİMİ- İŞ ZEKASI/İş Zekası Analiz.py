import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 📌 1. Veri Setini Yükleyelim
df = pd.read_csv("sales_data.csv")

# 📌 2. Toplam Geliri Hesaplayalım
df["Toplam Gelir"] = df["Adet"] * df["Fiyat"]

# 📌 3. En Çok Satış Yapılan Ayı Bulalım
df["Tarih"] = pd.to_datetime(df["Tarih"])
df["Ay"] = df["Tarih"].dt.month
aylik_satis = df.groupby("Ay")["Toplam Gelir"].sum()

# 📌 4. En Çok Gelir Getiren Ürünü Bulalım
urun_satis = df.groupby("Ürün")["Toplam Gelir"].sum()

# 📌 5. Şehir Bazlı Satışları İnceleyelim
sehir_satis = df.groupby("Şehir")["Toplam Gelir"].sum()

# 📌 6. Grafikler Çizelim
plt.figure(figsize=(12, 5))

# 🔹 Aylık Satış Grafiği
plt.subplot(1, 3, 1)
sns.barplot(x=aylik_satis.index, y=aylik_satis.values, palette="viridis")
plt.title("Aylık Satış Geliri")
plt.xlabel("Ay")
plt.ylabel("Gelir")

# 🔹 Ürün Bazlı Gelir Grafiği
plt.subplot(1, 3, 2)
sns.barplot(x=urun_satis.index, y=urun_satis.values, palette="coolwarm")
plt.title("Ürün Bazlı Gelir")
plt.xlabel("Ürün")
plt.ylabel("Gelir")

# 🔹 Şehir Bazlı Gelir Grafiği
plt.subplot(1, 3, 3)
sns.barplot(x=sehir_satis.index, y=sehir_satis.values, palette="magma")
plt.title("Şehir Bazlı Gelir")
plt.xlabel("Şehir")
plt.ylabel("Gelir")

plt.tight_layout()
plt.show()
