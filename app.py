# app.py
# Streamlit arayüzü - kullanıcıdan soru alır, retriever ile ilgili belgeleri bulur ve
# PromptNode aracılığıyla LLM'den yanıt döndürür.

import streamlit as st
from config import get_embedding_model, DATA_PATH, APP_TITLE
from data_processing import load_documents
from vector_store_manager import create_vector_store
from rag_pipeline import create_rag_pipeline

st.set_page_config(page_title=APP_TITLE, page_icon="🎥", layout="centered")
st.title(APP_TITLE)
st.markdown("""Bu küçük uygulama, önceden yüklenmiş film/dizi bilgileri üzerinden 
            sorulara kaynaklı cevaplar üretir. """)

# Yükleme düğmeleri / durum göstergesi
if 'initialized' not in st.session_state:
    st.session_state['initialized'] = False

if not st.session_state['initialized']:
    with st.spinner('Belgeler yükleniyor ve embedding oluşturuluyor (ilk seferde zaman alabilir)...'):
        # Belgeleri yükle
        docs = load_documents(DATA_PATH)

        # Embedding modelini al
        embedding_model = get_embedding_model()

        # Vektör deposu ve retriever oluştur
        document_store, retriever = create_vector_store(docs, embedding_model)

        # RAG pipeline oluştur (LLM ayarlarını .env veya ortam değişkenlerinden almayı tercih edin)
        pipeline = create_rag_pipeline(retriever, llm_model_name=None, api_key=None)

        # Store in session state
        st.session_state['docs'] = docs
        st.session_state['document_store'] = document_store
        st.session_state['retriever'] = retriever
        st.session_state['pipeline'] = pipeline
        st.session_state['initialized'] = True
    st.success('Hazır ✅')

query = st.text_input('Soru yazın:', placeholder='Örnek: "MCU izleme sırası nasıl?"')

if st.button('Sor'):
    if not query.strip():
        st.warning('Lütfen bir soru yazın.')
    else:
        with st.spinner('Yanıt hazırlanıyor...'):
            pipeline = st.session_state['pipeline']
            output = pipeline.run(query=query, params={"Retriever": {"top_k": 5}})
            # PromptNode cevabını al
            answers = output.get('answers') or output.get('output') or output.get('results')
            st.markdown('### 📝 Yanıt')
            # Basit gösterim (pipeline çıktısına göre uyarlanmıştır)
            st.write(output)
