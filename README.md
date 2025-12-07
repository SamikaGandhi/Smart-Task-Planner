# 📝 **Smart Task Planner — FastAPI**

A clean, modern, full-stack task-planning application powered by **FastAPI**, with a structured, user-friendly UI that generates actionable plans from any goal using an AI planner.
Plans are saved locally using SQLite and rendered using Jinja2 templates.

---

## 🌟 Features

* ✔ Generate structured task plans from any user goal
* ✔ Tasks displayed in a clean horizontal card layout
* ✔ Save and revisit previously generated task plans
* ✔ Beautiful modern UI using custom CSS (no Tailwind needed)
* ✔ SQLite database persistence
* ✔ Environment-based configuration
* ✔ Simple, clean project structure

---

## 🏗️ Tech Stack

**Backend:** FastAPI, Python 3.10+, SQLite
**Frontend:** HTML, Jinja2 Templates, Custom CSS
**AI Planner:** Lightweight text generation logic (can integrate OpenAI/TogetherAI/Local models)

---

## ⚙️ Environment Variables

Create a `.env` file in the project root:

```env
# backend_app/.env

TOGETHER_API_KEY=your-API-Key
LLM_MODEL=meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo


# Optional: a system prompt override (leave empty if not needed)
SYSTEM_PROMPT=You are a smart task planner that generates structured, priority-based plans with steps, durations, and time-based scheduling when needed.

# === Only if your app still uses SQLite for saving plans ===
SQLITE_DB_PATH=./plans.db
```

---

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

### 3️⃣ Open in Browser

```
http://localhost:8000
```

This automatically serves:

* `/` → Goal input page
* `/generate` → AI planning + result page
* `/plans` → Saved plans page


---

## 🎨 Frontend UI

Your HTML pages automatically render from templates:

* `index.html` – Goal input
* `result.html` – Generated tasks in beautiful horizontal cards
* `plans.html` – List of saved plans

UI styling comes from `static/styles.css`.

---

##  Video Demo
Link - https://drive.google.com/file/d/1nyENDo3pdf5fSS6BmFtQ5vyDyAwb0M2c/view?usp=sharing


https://github.com/user-attachments/assets/1e6bd914-31cd-40c2-9059-52e9fee2406b




---


## 🖼️ Screenshots


│ index.png


<img width="1047" height="411" alt="image" src="https://github.com/user-attachments/assets/670c0e89-6f1a-49ba-958f-2bef7f76fe28" />



│ result.png


<img width="1016" height="649" alt="image" src="https://github.com/user-attachments/assets/a2cc5a41-f008-404b-866f-a242c2ae948f" />



│ plans.png

<img width="927" height="543" alt="Screenshot 2025-12-07 121618" src="https://github.com/user-attachments/assets/efd138b9-f918-440d-a32e-557aa0c02dce" />



---


## 🚀 Deployment

You can deploy using:

### **Render / Railway / Fly.io / Deta / EC2**

Use:

```
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

Set environment variables in the platform dashboard.

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch
3. Commit & push
4. Create a Pull Request

---

## 📜 License

This project is provided under the **MIT License** — feel free to modify and use it!







