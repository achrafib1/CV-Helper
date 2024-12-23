FROM python:3.11-slim AS builder

WORKDIR /app

# Create a virtual environment
RUN python -m venv venv

# Activate the virtual environment
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the source code
COPY src/ .

FROM python:3.11-slim

WORKDIR /app

# Copy the virtual environment folders
COPY --from=builder /app/venv/bin /app/venv/bin
COPY --from=builder /app/venv/lib /app/venv/lib

# Copy only the source code 
COPY --from=builder /app  /app/


# Activate the virtual environment and set the PATH to include the bin folder of venv
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]