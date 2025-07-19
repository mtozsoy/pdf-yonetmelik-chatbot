from flask import Flask, render_template, request
from utils import read_all_pdfs_from_folder, split_text
from embedding import create_faiss_index, search_similar
import subprocess

app = Flask(__name__)

folder_path = "docs"  # PDF’leri koyduğun klasör

print("PDF dosyaları okunuyor...")
all_texts, filenames = read_all_pdfs_from_folder(folder_path)

print("Metinler parçalanıyor ve birleştiriliyor...")
all_chunks = []
for text, fname in zip(all_texts, filenames):
    chunks = split_text(text)
    # Dosya adını chunk önüne ekleyerek bağlamı güçlendiriyoruz
    chunks = [f"[{fname}] {chunk}" for chunk in chunks]
    all_chunks.extend(chunks)

print("FAISS index oluşturuluyor...")
index = create_faiss_index(all_chunks)
print("Hazır.")

def ollama_generate(prompt):
    process = subprocess.Popen(
        ["ollama", "run", "mistral"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8"
    )
    stdout, stderr = process.communicate(input=prompt)
    if process.returncode != 0:
        print("Hata:", stderr)
        return "Model çalıştırılırken hata oluştu."
    return stdout.strip()

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    if request.method == "POST":
        question = request.form["question"]
        relevant_chunks = search_similar(question, index, all_chunks, top_k=5)
        context = " ".join(relevant_chunks)
        if len(context) > 1500:
            context = context[:1500]
        prompt = (
            f"Aşağıdaki dökümanlardan alınan bilgiler ışığında soruyu cevapla.\n\n"
            f"Döküman:\n{context}\n\n"
            f"Soru: {question}\n"
            f"Lütfen açık ve net cevap ver."
        )
        print("Prompt:\n", prompt)  # Debug için
        answer = ollama_generate(prompt)
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
