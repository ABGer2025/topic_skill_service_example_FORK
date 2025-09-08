
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
| Methode | Endpoint           | Beschreibung                        | Parameter (Query/Body)                |
|---------|--------------------|-------------------------------------|---------------------------------------|
| GET     | `/topics`          | Alle Topics abrufen                 | `q`, `parentId`, `limit`, `offset`    |
| GET     | `/topics/<id>`     | Einzelnes Topic per ID abrufen      |                                       |
| POST    | `/topics`          | Neues Topic anlegen                 | `name` (str, Pflicht), `description`, `parentTopicID` |
| PUT     | `/topics/<id>`     | Topic per ID aktualisieren          | `name`, `description`, `parentTopicID`|
| DELETE  | `/topics/<id>`     | Topic per ID löschen                |                                       |

### Skills
| Methode | Endpoint           | Beschreibung                        | Parameter (Query/Body)                |
|---------|--------------------|-------------------------------------|---------------------------------------|
| GET     | `/skills`          | Alle Skills abrufen                 | `q`, `topicId`, `limit`, `offset`     |
| GET     | `/skills/<id>`     | Einzelnen Skill per ID abrufen      |                                       |
| POST    | `/skills`          | Neuen Skill anlegen                 | `name` (str, Pflicht), `topicID` (Pflicht), `difficulty` |
| PUT     | `/skills/<id>`     | Skill per ID aktualisieren          | `name`, `topicID`, `difficulty`       |
| DELETE  | `/skills/<id>`     | Skill per ID löschen                |                                       |

---

## Datenmodell

Die Daten werden in einer PostgreSQL-Datenbank gespeichert. Die wichtigsten Felder:

**Topic:**
- `id` (UUID, Primary Key)
- `name` (str)
- `description` (str)
- `parent_topic_id` (UUID, optional)

**Skill:**
- `id` (UUID, Primary Key)
- `name` (str)
- `topic_id` (UUID, Foreign Key)
- `difficulty` (str, z.B. "beginner", "mittel", "schwer")

---

## Fehlerbehandlung

- Bei nicht gefundenen Ressourcen wird ein Fehlerobjekt mit passender Statusnummer zurückgegeben, z.B. `{ "error": "Topic not found" }` (Status 404).
- Bei ungültigen Requests (fehlende Felder, falsche UUID, etc.) wird ein Fehlerobjekt mit Status 422 zurückgegeben.
- Bei Konflikten (z.B. Topic hat noch Skills) wird ein Fehlerobjekt mit Status 409 zurückgegeben.

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
	-d '{"name": "Ableiten", "topicID": "<topic-uuid>", "difficulty": "mittel"}'
```

---

## Hinweise

- Die Daten werden in einer PostgreSQL-Datenbank gespeichert (nicht mehr in JSON-Dateien).
- Die API ist für Lernzwecke gedacht und speichert Daten nur lokal.
- UUIDs werden als IDs verwendet (z.B. für `/topics/<id>`).