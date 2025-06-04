# 🏋️‍♂️ Fitness & Nutrition Coach Chatbot

A personal fitness and diet assistant chatbot powered by Groq's blazing-fast LLaMA 3 model, served via a simple Gradio interface.

Ask anything from:
- "What's a good workout to lose belly fat?"
- "How much protein do I need daily?"
- "Suggest a vegetarian muscle gain diet plan"

Live Demo: [Hugging Face Space](https://huggingface.co/spaces/JRjp777/fitness-nutrition-coach)

---

## 🔑 How to Get a Groq API Key

To run this app, you'll need an API key from [Groq](https://groq.com/).

1. Visit: https://console.groq.com/keys  
2. Sign up or log in with your account.  
3. Click **"Create API Key"**  
4. Copy the key (starts with `gsk_...`) and **store it securely**.

---

## 💻 Running Locally

### 1. Clone the Repo

```bash
git clone https://github.com/vishnuprakash-777/fitness-nutrition-coach.git
cd fitness-nutrition-coach
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create .env File

In the root folder, create a file named `.env` and add your Groq key:

```env
GROQ_API_KEY=gsk_your_real_key_here
```

### 4. Run the App

```bash
python app.py
```

This will start the Gradio app locally and provide a public `gradio.live` link.

---

## 🌍 Deploying to Hugging Face Spaces

Hugging Face makes it super easy to deploy Gradio apps.

### Step-by-Step Guide:

1. Go to: https://huggingface.co/spaces  
2. Click **"Create new Space"**  
3. Fill in:
   - **Space Name**: `fitness-nutrition-coach`  
   - **SDK**: Gradio  
   - **Template**: chatbot (optional)  

Once the Space is created, upload the following files:
- `app.py`
- `requirements.txt`
- `.gitignore` (optional)

### Add Your Secret API Key Securely:

1. Go to your Space → **Settings** → **Secrets**
2. Add:
   - **Name**: `GROQ_API_KEY`
   - **Value**: `gsk_your_real_key_here`

Your app will automatically rebuild and go live.

---

## 📦 Dependencies

```
gradio
groq
python-dotenv
```

---

## 🛡️ Security Note

Never commit your `.env` file or API key to version control.  
Always use `.gitignore` and Hugging Face Secrets for deployment.

---

