# Risk Acceptance Workflow - AI Module

## Overview

This project provides AI-powered risk analysis endpoints for a
Risk Acceptance Workflow system.

---

# Features

- Risk Classification
- Risk Summarization
- Risk Mitigation Recommendations
- Prompt Injection Protection
- SQL Injection Protection
- Rate Limiting
- Dockerized Deployment

---

# Tech Stack

- Python Flask
- Groq API
- Docker
- Java RestTemplate Client
- Pytest

---

# Endpoints

## POST /classify
Classifies risks into HIGH, MEDIUM, LOW.

## POST /summarize
Summarizes risk description.

## POST /recommend
Provides mitigation recommendations.

---

# Run Locally

## Step 1
Create `.env`

```env
GROQ_API_KEY=your_key_here
AI Module contributed by Aditya Raj