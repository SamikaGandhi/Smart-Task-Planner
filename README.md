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

## 📂 Project Structure


smart-task-planner-fastAPI/
│
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI entry point
│   ├── planner.py       # AI planner logic (OpenAI or custom logic)
│   ├── db.py            # SQLite database setup + CRUD operations
│   ├── schemas.py       # Pydantic schemas
│   │
│   ├── templates/       # Jinja2 templates
│   │    ├── index.html
│   │    ├── result.html
│   │    └── plans.html
│   │
│   └── static/
│        └── styles.css  # Modern clean UI styling
│
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables
└── README.md            # Project documentation

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


## 🖼️ Screenshots

```
screenshots/
│ index.png
│ result.png
│ plans.png
```

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

