# data_processing.py
# Veri dosyasından belgeleri okur ve Haystack'in kullanacağı formatta döner.

import os

def load_documents(data_path):
    """data_path içindeki metin dosyasını okuyup,
    çift boş satır ile ayrılmış bölümleri ayrı belgeler olarak döndürür.

    Her bir döküman dict formatında olmalıdır: {'content': '...'}
    """
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Veri dosyası bulunamadı: {data_path}")
    with open(data_path, 'r', encoding='utf-8') as f:
        raw = f.read()
    # Belgeleri çift boş satır ile ayır
    parts = [p.strip() for p in raw.split('\n\n') if p.strip()]
    docs = []
    for i, p in enumerate(parts):
        docs.append({
            "id": f"doc_{i+1}",
            "content": p,
            "meta": {"source": "film_dizi_bilgileri.txt"}
        })
    return docs
