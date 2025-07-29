import json
import os

RECORDS_FILE = "records.json"
MAX_RECORDS = 5
MAX_NAME_LENGTH = 10

def load_records():
    """Carga los records desde el archivo"""
    if os.path.exists(RECORDS_FILE):
        try:
            with open(RECORDS_FILE, 'r') as f:
                return json.load(f)
        except:
            return []
    return []

def save_records(records):
    """Guarda los records en el archivo"""
    with open(RECORDS_FILE, 'w') as f:
        json.dump(records, f)

def add_record(name, score):
    """Agrega un nuevo record si califica"""
    records = load_records()
    
    # Agregar nuevo record
    new_record = {"name": name[:MAX_NAME_LENGTH], "score": score}
    records.append(new_record)
    
    # Ordenar por score (mayor primero)
    records.sort(key=lambda x: x["score"], reverse=True)
    
    # Mantener solo los mejores 5
    records = records[:MAX_RECORDS]
    
    # Guardar
    save_records(records)
    return records

def is_high_score(score):
    """Verifica si el score califica para un record"""
    records = load_records()
    if len(records) < MAX_RECORDS:
        return True
    return score > records[-1]["score"]

def get_records():
    """Retorna la lista de records"""
    return load_records() 