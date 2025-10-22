# 🎬 Film & Dizi Asistanı - Mini RAG Projesi

Bu proje, **GAIH GenAI Bootcamp**'teki yapının (modüler dosya yapısı ve Haystack tabanlı RAG pipeline) aynısını koruyarak,
içerik olarak **Film ve Dizi** bilgileriyle çalışan küçük bir RAG (Retrieval-Augmented Generation) uygulamasıdır.

Proje öğretici amaçlıdır — basit, çalıştırması kolay ve anlaşılır olması hedeflenmiştir.

## Dosya Yapısı

```
film-dizi-asistani/
│
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── config.py
├── data_processing.py
├── vector_store_manager.py
├── rag_pipeline.py
├── app.py
└── data/
    └── film_dizi_bilgileri.txt
```

## Özellikler
- Basit RAG pipeline: Belgelerden ilgili parçaları getirip (retriever) prompt ile modelden yanıt üretir.
- Sentence Transformers ile embedding oluşturur.
- Haystack `InMemoryDocumentStore` kullanır (küçük veri setleri için uygundur).
- Streamlit arayüzü sunar.

## Gereksinimler

- Python 3.8 veya üzeri
- Aşağıdaki paketleri yükleyin:

```bash
pip install -r requirements.txt
```

> Not: `farm-haystack[all]` paketi büyük ve bazı sistemlerde kurulum sırasında ek bağımlılıklar gerektirebilir. Küçük denemeler için `farm-haystack` yerine `haystack` veya sadece `haystack`'in bazı bileşenleri tercih edilebilir.

## Kurulum ve Çalıştırma

1. Proje klasörüne girin:
   ```bash
   cd film-dizi-asistani
   ```

2. Gerekli paketleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

3. Streamlit uygulamasını başlatın:
   ```bash
   streamlit run app.py
   ```

4. Tarayıcıda `http://localhost:8501` adresini açın.

## Kullanım

- `data/film_dizi_bilgileri.txt` dosyasına kendi film/dizi bilgilerinizi, özetleri, kronolojileri vs. ekleyin. Her belge arasında boş bir satır bırakarak birden fazla belge ekleyebilirsiniz.
- Uygulama basit bir Retriever + PromptNode akışı kullanır. API anahtarı gerektiren bir model kullanmak isterseniz `rag_pipeline.py` içindeki açıklamaları takip edin.

## Lisans

MIT License — detaylar `LICENSE` dosyasında.

## Sorumluluk Reddi

Bu rehber eğitseldir. Telif hakkı koruması altında olan içerikleri kullanırken ilgili izinleri almanız gerekir. Akademik veya ticari amaçlarla kullanım öncesi lisans ve telif haklarına dikkat ediniz.
