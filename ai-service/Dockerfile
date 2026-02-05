# 1️⃣ Use official Python image
FROM python:3.11-slim

# 2️⃣ Set working directory
WORKDIR /app

# 3️⃣ Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4️⃣ Copy source code
COPY . .

# 5️⃣ Expose port
EXPOSE 8000

# 6️⃣ Healthcheck (optional)
HEALTHCHECK --interval=10s --timeout=2s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# 7️⃣ Start FastAPI app with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
