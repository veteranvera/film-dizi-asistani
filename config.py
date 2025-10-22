# config.py
# Proje seviyesinde kullanılacak sabitler ve model tanımları

from sentence_transformers import SentenceTransformer
import os

# Embedding modeli (küçük ve çok-dilli; Türkçe için uygun)
# Eğer makinede GPU yoksa sentence-transformers otomatik olarak CPU'da çalışacaktır.
EMBEDDING_MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"

# Burada model nesnesi oluşturuluyor. (Uygulama başladığında yüklenir)
def get_embedding_model():
    return SentenceTransformer(EMBEDDING_MODEL_NAME)

# Veri dosyası yolu
DATA_PATH = os.path.join("data", "film_dizi_bilgileri.txt")

# Streamlit başlık ve diğer ayarlar
APP_TITLE = "🎬 Film & Dizi Asistanı"
ANSWER_MAX_TOKENS = 400
