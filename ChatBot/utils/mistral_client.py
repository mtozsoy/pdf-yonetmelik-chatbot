import requests

def ask_mistral(context, question):
    prompt = f"""Aşağıdaki metne göre soruyu cevapla:\n\n{context}\n\nSoru: {question}"""

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
        return f"Hata: {response.status_code}, {response.text}"
