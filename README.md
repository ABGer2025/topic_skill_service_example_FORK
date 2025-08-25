
# Topic and Skill Service (Python Flask)

## Setup & Start

1. **Virtuelle Umgebung aktivieren**
	 - **Linux/macOS:**
		 ```bash
		 source venv/bin/activate
		 ```
	 - **Windows (PowerShell):**
		 ```powershell
		 .\venv\Scripts\Activate.ps1
		 ```
	 - **Windows (Cmd):**
		 ```cmd
		 venv\Scripts\activate.bat
		 ```

2. **Abhängigkeiten installieren**
	 ```bash
	 pip install -r requirements.txt
	 ```

3. **Server starten**
	 ```bash
	 python app.py
	 ```

Der Server läuft auf: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## API-Übersicht

### Topics
| Methode | Endpoint           | Beschreibung                        |
|---------|--------------------|-------------------------------------|
| GET     | `/topics`          | Alle Topics abrufen                 |
| GET     | `/topics/<id>`     | Einzelnes Topic per ID abrufen      |
| POST    | `/topics`          | Neues Topic anlegen                 |
| PUT     | `/topics/<id>`     | Topic per ID aktualisieren          |
| DELETE  | `/topics/<id>`     | Topic per ID löschen                |

### Skills
| Methode | Endpoint           | Beschreibung                        |
|---------|--------------------|-------------------------------------|
| GET     | `/skills`          | Alle Skills abrufen                 |
| GET     | `/skills/<id>`     | Einzelnen Skill per ID abrufen      |
| POST    | `/skills`          | Neuen Skill anlegen                 |
| PUT     | `/skills/<id>`     | Skill per ID aktualisieren          |
| DELETE  | `/skills/<id>`     | Skill per ID löschen                |

---

## Datenstruktur

### topics.json
```json
[
	{
		"id": "<uuid>",
		"name": "Thema-Name",
		"description": "Beschreibung des Themas"
	}
]
```

### skills.json
```json
[
	{
		"id": "<uuid>",
		"name": "Skill-Name",
		"topicId": "<topic-uuid>",
		"difficulty": "leicht | mittel | schwer | unknown"
	}
]
```

---

## Fehlerbehandlung

- Bei nicht gefundenen Ressourcen wird ein Fehlerobjekt mit passender Statusnummer zurückgegeben, z.B. `{ "error": "Topic not found" }` (Status 404).
- Bei ungültigen Requests (fehlende Felder) wird ein Fehlerobjekt mit Status 400 zurückgegeben.

---

## Beispiel-Requests

### Topic anlegen (POST)
```bash
curl -X POST http://127.0.0.1:5000/topics \
	-H "Content-Type: application/json" \
	-d '{"name": "Mathematik", "description": "Mathematische Grundlagen"}'
```

### Skill anlegen (POST)
```bash
curl -X POST http://127.0.0.1:5000/skills \
	-H "Content-Type: application/json" \
	-d '{"name": "Ableiten", "topicId": "<topic-uuid>", "difficulty": "mittel"}'
```

---

## Hinweise

- Die Daten werden in den Dateien `data/topics.json` und `data/skills.json` gespeichert.
- Die API ist für Lernzwecke gedacht und speichert Daten nur lokal.