# AI Social Media Agents 🤖📲  

## Business Problem This Project Solves 💡

Modern AI-powered content pipelines often rely heavily on **paid cloud APIs** — especially for **voice generation** and **media creation**. While platforms like OpenAI offer high-quality voice and multimodal APIs, **costs scale linearly with usage**, making them expensive and unsustainable for:

- Daily social media posting
- High-frequency content automation
- Indie creators, startups, and early-stage products
- Experimentation-heavy AI agent workflows

### ⚠️ The Cost Challenge
For example:
- Generating voice via OpenAI’s API incurs **per-request / per-token costs**
- Scaling voice + image + video generation quickly becomes expensive
- Repeated generation (A/B testing, retries, automation) multiplies API spend

---

## 💥 Solution: Offline-First AI Content Agents

This project demonstrates a **cost-optimized, offline-first alternative** by:

### ✅ Replacing paid voice APIs with open-source voice cloning
- **Cloned OpenAI-style voice locally** using **Coqui XTTS**
- Runs **fully offline** once set up
- Zero per-request cost
- High-quality, natural-sounding speech
- Ideal for repeatable and scalable automation

### ✅ Combining offline AI with lightweight APIs only where needed
- **Text generation** (captions): LLM-driven
- **Voice generation**: **Offline (Coqui XTTS)**
- **Image generation**: Python-based generation
- **Video assembly**: Local (image + voice → MP4)
- **Publishing**: Platform APIs only (Instagram / Reddit)

This architecture ensures:
- 💸 **Minimal operational cost**
- 📈 **Scales without increasing AI spend**
- 🔁 **Fast iteration & experimentation**
- 🧠 **Agent-driven automation without vendor lock-in**

---

## 🎯 Real-World Use Cases

- Daily Instagram reels with AI voiceovers
- Personal brand content automation
- Startup marketing pipelines
- Creator tools with predictable costs
- AI agents that act continuously (not per-request expensive)

---

## 🧠 Architectural Philosophy

> **Use paid APIs for intelligence, open-source models for generation, and automation for scale.**

This repo is intentionally designed to show how:
- AI agents can orchestrate tools
- Offline models can replace expensive SaaS APIs
- End-to-end pipelines can be production-ready *without burning money*

---


### 1) Generate captions (AI / LLM)
**Tech used:** `Python`, `OpenAI API`, **LangChain**, `python-dotenv`  
- Uses **LangChain LLM chains** to generate platform-ready Instagram captions  
- Supports tone control, hashtag strategies, and prompt templating  
- Designed to be reusable as a tool inside an agent workflow  
- Includes a local test runner for fast iteration  

**Script:** `scripts/caption_generator.py`  
**Test:** `scripts/test_caption.py`

---

### 2) Generate images (AI)
**Tech used:** `Python`, **OpenAI DALL·E 3 API**, `requests`  
- Generates high-quality, prompt-driven images suitable for Instagram posts  
- Image generation is driven by caption or prompt context  
- Outputs images as local assets for video assembly or posting  

**Script:** `scripts/image_generator.py`  
**Output:** `temp_image.png`

---

### 3) Generate voice offline (OpenAI-style voice cloning)
**Tech used:** `Python`, **Coqui XTTS** (offline open-source TTS)  
- Clones an OpenAI-style voice locally  
- Runs fully offline after setup (no per-request cost)  
- Enables unlimited narration generation at predictable cost  

**Output:** `.wav` / `.mp3` narration files

---

### 4) Build video (image + voice → MP4)
**Tech used:** `Python`, `ffmpeg` / `moviepy`  
- Combines generated DALL·E images with XTTS narration into short-form videos  
- Produces Instagram-ready MP4 output  

**Output:** `final_instagram_post.mp4`

---

### 5) Orchestrate the pipeline (Agent-style flow)
**Tech used:** **LangChain**, `Python`  
- LangChain orchestrates tools end-to-end (caption → image → voice → video → publish)  
- Enables modular, agent-driven execution instead of rigid scripts  
- Makes the system extensible for scheduling, retries, and multi-platform support  

---

### 6) Post to Instagram (Graph API)
**Tech used:** `Python`, `requests`, **Instagram Graph API**  
- Uploads and publishes media programmatically  
- Designed for automated and scheduled posting workflows  

**Script:** `scripts/instagram_poster.py`

---

### 7) Host video on S3 for reliable Instagram uploads
**Tech used:** `AWS S3`, `boto3`, `UUID`, `video/mp4 Content-Type`  
- Uploads MP4 to S3 and uses the public URL as the Instagram media source  
- Improves reliability for programmatic Instagram video publishing  
