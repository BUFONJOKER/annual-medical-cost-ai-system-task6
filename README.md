---

# 🏥 Annual Medical Cost AI System

### 🚀 Built with FastAPI + Streamlit + Docker + HuggingFace Spaces

This project predicts **Annual Medical Cost** for patients using Machine Learning.
It is part of **Task 6 of the Data Science & Machine Learning Internship**.

---

## 🎯 Project Overview

* When user enters patient details in the **Streamlit frontend**,
  the app sends data to the **FastAPI backend**.
* Backend validates data with **Pydantic**, loads the trained ML model,
  generates prediction, and returns the estimated **annual medical cost**.

---

## 🐳 Dockerized Full-Stack System

Both **frontend (Streamlit)** and **backend (FastAPI)** are fully dockerized and pushed to Docker Hub.

### 🔗 Docker Hub Images

* 🌐 **Frontend Image**
  [https://hub.docker.com/repository/docker/bufonjoker/frontend-task6/general](https://hub.docker.com/repository/docker/bufonjoker/frontend-task6/general)

* ⚙️ **Backend Image**
  [https://hub.docker.com/repository/docker/bufonjoker/backend-task6/general](https://hub.docker.com/repository/docker/bufonjoker/backend-task6/general)

---

## 🤗 Live Deployments (HuggingFace Spaces)

* 🎨 **Streamlit App**
  [https://huggingface.co/spaces/BUFON-JOKER/frontend-task6](https://huggingface.co/spaces/BUFON-JOKER/frontend-task6)

* ⚡ **FastAPI Backend**
  [https://bufon-joker-backend-task6.hf.space](https://bufon-joker-backend-task6.hf.space)

---

# 📥 Clone This Repository

```bash
git clone https://github.com/BUFONJOKER/annual-medical-cost-ai-system-task6.git

cd annual-medical-cost-ai-system-task6
```

---

# ▶️ Run Locally Using **uv**
```bash
uv sync
```



## 🎨 Frontend (Streamlit)

```bash
cd frontend
streamlit app.py
```

## ⚙️ Backend (FastAPI)

```bash
cd backend
uvicorn main:app --reload
```

---

# 🐳 Pull Docker Images

### 👉 Frontend

```bash
docker pull bufonjoker/frontend-task6:latest
```

### 👉 Backend

```bash
docker pull bufonjoker/backend-task6:latest
```

---

# ▶️ Run Docker Containers

### 🎨 Run Frontend

```bash
docker run -p 8501:8501 bufonjoker/frontend-task6:latest
```

Runs at: **[http://localhost:8501](http://localhost:8501)**

### ⚙️ Run Backend

```bash
docker run -p 8000:8000 bufonjoker/backend-task6:latest
```

Runs at: **[http://localhost:8000](http://localhost:8000)**

---

# 🔌 How Frontend Communicates with Backend

1. User enters data in Streamlit form
2. Streamlit sends POST request → **FastAPI endpoint**
3. FastAPI validates input using **Pydantic**
4. ML model predicts medical cost
5. API returns prediction
6. Streamlit shows result to user 🎉

---

# 📦 Libraries Used

* **FastAPI**
* **Streamlit**
* **Uvicorn**
* **Pydantic**
* **Scikit-learn**
* **Pandas**

---


