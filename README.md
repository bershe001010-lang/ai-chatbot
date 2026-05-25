# AI Chatbot with Groq API

A simple AI chatbot built with Flask and Groq's fast LLM API. Deployed on AWS EC2 using Terraform.

## Features
- Ask any question and get an AI response
- Uses Groq's Llama 3.3 70B model (fast and free)
- Simple web interface
- Hosted on AWS

## Tech Stack
- **Backend:** Python, Flask
- **AI API:** Groq (Llama 3.3 70B)
- **Infrastructure:** Terraform, AWS EC2
- **Version Control:** GitHub

## How to Use
1. Go to: http://ec2-13-61-155-227.eu-north-1.compute.amazonaws.com:5000
2. Type your question
3. Click "Skicka" (Send)
4. Get AI response instantly

## Local Development
```bash
git clone https://github.com/bershe001010-lang/ai-chatbot.git
cd ai-chatbot
pip install -r requirements.txt
python app.py
