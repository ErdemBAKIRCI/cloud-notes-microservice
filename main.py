from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# --- 1. AI Servis Mantığı (Kategori Önerici) ---
def suggest_category(note_content: str):
    content = note_content.lower()
    if any(word in content for word in ["ekmek", "market", "süt", "al", "peynir"]):
        return "Alışveriş"
    elif any(word in content for word in ["ödev", "ders", "sınav", "hoca", "üniversite"]):
        return "Eğitim"
    elif any(word in content for word in ["toplantı", "iş", "proje", "ofis", "sunum"]):
        return "İş"
    else:
        return "Genel"

# --- 2. Veri Modeli (Domain Entity) ---
class Note(BaseModel):
    id: Optional[int] = None
    title: str
    content: str
    category: Optional[str] = None

# --- 3. FastAPI Başlatma ---
app = FastAPI(
    title="Secure Cloud Notes API",
    description="Güvenlikli ve Yapay Zeka Destekli Mikroservis",
    version="1.1.0"
)

# Geçici veri deposu
db_notes = []

# --- 4. API Endpoint'leri ---

@app.get("/", tags=["Genel"])
def read_root():
    return {"message": "Güvenli API Çalışıyor!", "auth_status": "Protected"}

@app.get("/notes", response_model=List[Note], tags=["Not İşlemleri"])
def get_all_notes():
    return db_notes

@app.post("/notes/create", tags=["Not İşlemleri"])
def create_note(note: Note, x_api_key: str = Header(...)):
    """
    Not eklemek için 'x-api-key' başlığına 'odev123' yazılmalıdır.
    """
    # GÜVENLİK KONTROLÜ (Security Basics)
    if x_api_key != "odev123":
        raise HTTPException(status_code=403, detail="Geçersiz API Anahtarı! Erişim Reddedildi.")

    # AI KATEGORİZASYON (AI Integration)
    if not note.category or note.category == "string":
        note.category = suggest_category(note.content)
    
    note.id = len(db_notes) + 1
    db_notes.append(note)
    
    return {
        "message": "Güvenli şekilde oluşturuldu", 
        "ai_suggestion": note.category, 
        "data": note
    }

@app.get("/health", tags=["Monitoring"])
def health_check():
    return {"status": "healthy", "observability": "active"}
