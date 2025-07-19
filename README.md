# 🧠 PDF Okuyan Chatbot (Mistral + Flask)

Bu proje, klasörünüzdeki PDF dosyalarını okuyarak öğrencilerin sorduğu sorulara PDF'lere dayalı olarak cevap verebilen bir chatbot sistemidir. Arka planda [Mistral](https://ollama.com/library/mistral) büyük dil modeli ve [Flask](https://flask.palletsprojects.com/) web framework'ü kullanılmaktadır.

## 📂 Özellikler

- 📄 Bir veya birden fazla PDF dosyasını okuyabilir.
- 🤖 Ollama üzerinden Mistral modelini kullanır.
- 🌐 Flask tabanlı web arayüzü ile soru-cevap sistemi sunar.
- ✨ Basit ve şık bir kullanıcı arayüzü içerir.

## 🚀 Kurulum

### 1. Gerekli paketleri yükleyin

```bash
pip install -r requirements.txt
```

### 2. Ollama ile Mistral modelini indirip çalıştırın
Eğer yüklü değilse, Ollama uygulamasını indirip kurun. Ardından terminale şu komutu yazın:
```bash
ollama run mistral
```
### 3. PDF dosyalarınızı yerleştirin
Proje dizininde bir pdfs/ klasörü oluşturun ve içine istediğiniz PDF yönetmeliklerini veya belgeleri atın.

### 4. Uygulamayı başlatın
```bash
python app.py
```
Uygulama çalıştığında tarayıcınızdan şu adrese giderek chatbot'u kullanabilirsiniz:
```cpp
http://127.0.0.1:5000
```
### 📝 Kullanım
Web arayüzü açıldığında kullanıcıdan soru alır.

Arka planda tüm PDF'leri okur ve bunlara göre Mistral ile cevap üretir.

PDF'lerdeki içerik değişirse uygulamayı yeniden başlatmanız gerekir.

### 📦 Gereksinimler
Python 3.8+

Flask

PyPDF2

Ollama (arka planda model çalıştırmak için)
