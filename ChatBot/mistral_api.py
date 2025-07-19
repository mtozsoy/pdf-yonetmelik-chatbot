import requests

def get_relevant_chunk(text, question):
    keywords = ["devamsızlık", "yoklama", "katılım", "ders", "ders saati", "devam"]
    for paragraph in text.split("\n"):
        for keyword in keywords:
            if keyword in paragraph.lower() and keyword in question.lower():
                return paragraph.strip()
    return text[:1000]  # fallback: ilk 1000 karakter

def ask_mistral(text, question):
    context = get_relevant_chunk(text, question)
    
    prompt = f"""
Sen bir üniversite yönetmelik danışmanısın. Aşağıdaki metne göre soruyu cevapla.

Metin:
\"\"\"
{context}
\"\"\"

Soru: {question}

Cevabı açık, sade ve TÜRKÇE ver.
"""
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code == 200:
        return response.json()["response"]
    else:
        return f"Hata oluştu: {response.status_code}"
