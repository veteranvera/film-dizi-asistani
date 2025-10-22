        # rag_pipeline.py
        # Basit bir Retriever -> PromptNode (veya doğrudan generation) pipeline'ı kurar.
        # Bu örnekte haystack'in Pipeline yapısını kullanıyoruz ve
        # PromptNode yerine basitçe retriever çıktısını alıp prompt ile dış bir model
        # çağırılacak şekilde düzenlenmiştir.
        #
        # Not: Eğer OpenAI veya başka bir LLM kullanacaksanız, API anahtarınızı güvenli şekilde
        # .env veya ortam değişkenlerinde tutun ve burada çağırırken o anahtarı kullanın.

        from haystack.pipelines import Pipeline
        from haystack.nodes import PromptNode, PromptTemplate

        def create_rag_pipeline(retriever, llm_model_name=None, api_key=None):
            """Retriever'ı alır, PromptNode (varsa) ile pipeline oluşturur.
            llm_model_name parametresi opsiyoneldir; kendi model entegrasyonunuza göre düzenleyin.
            """
            # Basit bir prompt template
            template = PromptTemplate(
                name='film_dizi_prompt',
                prompt_text=(
                    "Kullanıcının sorusuna sadece aşağıdaki belgelerden yararlanarak, "
                    "kaynak göstererek kısa ve Türkçe cevap ver. Eğer verilen belgelerde cevap yoksa "
                    "kısa bir şekilde 'Veritabanında ilgili bilgi bulunamadı.' yaz.
\n"
                    "Belgeler:\n{join(documents)}\n\n"
                    "Soru: {query}\n\n"
                    "Cevap:"
                )
            )

            # PromptNode örneği - burada haystack'in desteklediği bir model bağlayıcısı kullanılabilir.
            # Kullanıcı kendi LLM entegrasyonunu buraya koyabilir (OpenAI, Anthropic, yerel model vs.)
            prompt_node = PromptNode(
                model_name_or_path=llm_model_name or 'gpt-3.5-turbo',
                default_prompt_template=template,
                api_key=api_key
            )

            pipe = Pipeline()
            pipe.add_node(component=retriever, name='Retriever', inputs=['Query'])
            pipe.add_node(component=prompt_node, name='PromptNode', inputs=['Retriever'])
            return pipe
