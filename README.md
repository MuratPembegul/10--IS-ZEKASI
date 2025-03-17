# 10--IS-ZEKASI

# 📊 İş Zekası (Business Intelligence) README

## 📌 Giriş (Introduction)
İş Zekası (Business Intelligence - BI), verileri analiz ederek stratejik kararlar almayı sağlayan süreçler, teknolojiler ve araçlardan oluşur.
BI, şirketlerin geçmiş verileri anlamasını, mevcut durumu analiz etmesini ve geleceğe yönelik tahminler yapmasını sağlar. 🚀

Bu repo, iş zekası araçları ve veri analitiği süreçlerine dair bilgiler ve Python ile temel BI uygulamalarını içermektedir. 🏗️

---

## 🚀 Kurulum (Installation)
Aşağıdaki komutla gerekli Python kütüphanelerini yükleyebilirsiniz:

```bash
pip install pandas numpy matplotlib seaborn plotly dash sqlalchemy openpyxl
```

---

## 🔥 Kullanılan Kütüphaneler (Libraries Used)

1. **Pandas** 📊 - Veri manipülasyonu.
2. **NumPy** 🔢 - Sayısal işlemler.
3. **Matplotlib & Seaborn** 📉 - Veri görselleştirme.
4. **Plotly & Dash** 📊 - Etkileşimli grafikler ve panolar.
5. **SQLAlchemy** 🛢️ - Veri tabanı bağlantısı.
6. **OpenPyXL** 📂 - Excel dosyalarını işleme.

---

## 📚 İş Zekası Süreçleri
İş zekası, aşağıdaki temel süreçlerden oluşur:

- **Veri Toplama** 🏗️: SQL, API veya CSV gibi kaynaklardan veri çekme.
- **Veri Temizleme** 🧹: Eksik değerleri doldurma, aykırı değerleri belirleme.
- **Veri Analizi** 📊: Deskriptif ve ileri seviye analizler.
- **Görselleştirme ve Raporlama** 📈: Dashboard oluşturma.
- **Tahminleme ve Veri Modelleme** 🔮: Makine öğrenmesi ile tahminleme.

---

## 🏗️ Örnek Kullanım (Examples)

### 📌 Pandas ile Temel Veri Analizi
```python
import pandas as pd

data = pd.read_csv("sales_data.csv")
print(data.head())  # İlk 5 satırı göster

# Eksik verileri kontrol etme
print(data.isnull().sum())
```

### 📊 Matplotlib ile Basit Grafik Çizimi
```python
import matplotlib.pyplot as plt

data.groupby("product_category")["sales"].sum().plot(kind="bar")
plt.title("Ürün Kategorilerine Göre Satışlar")
plt.show()
```

### 📈 Dash ile Basit Bir Dashboard
```python
import dash
from dash import dcc, html
import plotly.express as px

df = px.data.gapminder()
fig = px.scatter(df, x="gdpPercap", y="lifeExp", color="continent", size="pop")

app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)
```

---

## 📚 Ek Kaynaklar (Additional Resources)
- [Tableau](https://www.tableau.com/)
- [Power BI](https://powerbi.microsoft.com/)
- [Dash by Plotly](https://dash.plotly.com/)
- [Matplotlib](https://matplotlib.org/)

---

## 📌 Katkı Yapma (Contributing)
Projeye katkı sağlamak isterseniz fork'layın, geliştirin ve PR gönderin! 🚀

---

## 📜 Lisans (License)
Bu proje MIT lisansı altındadır, dilediğiniz gibi kullanabilirsiniz! 😊

