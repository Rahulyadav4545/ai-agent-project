# 🤖 Autonomous AI Agent - Setup & Usage Guide

## Quick Start (5 minutes)

### 1. Get Free Groq API Key (2 min)
```
1. Go to: https://console.groq.com
2. Sign up with email (instant)
3. Get API key starting with "gsk_"
4. Copy it
```

### 2. Install Dependencies (2 min)
```bash
pip install -r requirements.txt
```

### 3. Add API Key (1 min)
Open `agent.py` and find line 20:
```python
os.environ["GROQ_API_KEY"] = "gsk_YOUR_ACTUAL_API_KEY_HERE"
```

Replace with your actual key:
```python
os.environ["GROQ_API_KEY"] = "gsk_abc123xyz789..."
```

### 4. Run Server
```bash
python agent.py
```

You should see:
```
╔════════════════════════════════════════════════════════╗
║     🤖 AUTONOMOUS AI AGENT - Starting Server...        ║
╚════════════════════════════════════════════════════════╝

📍 API: http://localhost:8000
📚 Docs: http://localhost:8000/docs
```

### 5. In Another Terminal - Run Tests
```bash
python test_agent.py
```

---

## Detailed Setup

### Prerequisites
- Python 3.9+
- pip (Python package manager)
- Internet connection

### Step 1: Create Project Directory
```bash
mkdir ai-agent-project
cd ai-agent-project
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Packages
```bash
pip install -r requirements.txt
```

### Step 4: Get Groq API Key
1. Visit https://console.groq.com
2. Create account (use Gmail for quick signup)
3. Go to "API Keys" section
4. Create new key
5. Copy the key (starts with `gsk_`)

### Step 5: Configure API Key
Edit `agent.py`, line 20:
```python
os.environ["GROQ_API_KEY"] = "gsk_YOUR_KEY_HERE"
```

### Step 6: Test Setup
```bash
# Check if API will work
python -c "
from langchain_groq import ChatGroq
import os
os.environ['GROQ_API_KEY'] = 'gsk_YOUR_KEY'
llm = ChatGroq(model_name='llama-3.1-8b-instant')
print('✅ LLM initialized successfully!')
"
```

---

## Running the Agent

### Method 1: Using Test Suite (Recommended)
```bash
# Terminal 1
python agent.py

# Terminal 2
python test_agent.py
```

This will:
- ✅ Run 2 test cases (Simple + Complex)
- ✅ Show task breakdown
- ✅ Generate Word documents
- ✅ Display results

### Method 2: Manual Testing with cURL

Start server:
```bash
python agent.py
```

In another terminal, send request:
```bash
curl -X POST http://localhost:8000/agent \
  -H "Content-Type: application/json" \
  -d '{
    "request": "Create a project proposal document for a new mobile app development project"
  }'
```

### Method 3: Using Python Requests
```python
import requests

response = requests.post(
    "http://localhost:8000/agent",
    json={
        "request": "Create meeting minutes for a product review"
    }
)

print(response.json())
```

### Method 4: Interactive API Docs
1. Run the server: `python agent.py`
2. Open browser: http://localhost:8000/docs
3. Click "Try it out" on the POST /agent endpoint
4. Enter your request
5. Click "Execute"

---

## Available Endpoints

### POST /agent
**Main endpoint - Submit request and get document**

Request:
```json
{
  "request": "Create a professional document for..."
}
```

Response:
```json
{
  "status": "success",
  "message": "✅ Agent executed successfully...",
  "task_plan": [
    "Task 1: Analyze request",
    "Task 2: Structure content",
    ...
  ],
  "agent_reasoning": "The agent thought...",
  "document_created": true,
  "document_path": "output.docx",
  "execution_time": "12.34s"
}
```

### GET /download
**Download generated Word document**

```bash
curl http://localhost:8000/download -o my_document.docx
```

### GET /health
**Check API status**

```bash
curl http://localhost:8000/health
```

Response:
```json
{
  "status": "healthy",
  "service": "Autonomous AI Agent",
  "llm": "Groq Llama 3.1",
  "api_key_configured": true
}
```

### GET /docs
**Interactive API documentation (Swagger)**

Open in browser: http://localhost:8000/docs

---

## Test Cases Explained

### Test 1: Simple Request ✅
**Purpose:** Straightforward business document

**Request:** "Create meeting minutes for a product review meeting"

**What Agent Does:**
1. Identifies clear task: Create meeting document
2. Gathers standard sections: Attendees, agenda, action items
3. Uses mock data for missing information
4. Generates professional document

**Evaluation:** Easy to follow, clear output

---

### Test 2: Complex Request ⚡
**Purpose:** Ambiguous, multi-step, incomplete info

**Request:** "Create technical design for microservice with unclear requirements"

**What Agent Does:**
1. **Identifies ambiguity:** Architecture not specified, tech stack unclear, scalability vague
2. **Makes assumptions:** REST API, Node.js, handles 100K req/day
3. **Documents assumptions:** Explains why choices were made
4. **Creates full design:** System architecture, API endpoints, database schema

**Evaluation:** Shows autonomous planning & decision-making

---

## Troubleshooting

### Issue: API Key Error
```
Error: GROQ_API_KEY not found
```

**Fix:** Make sure you added the key to line 20 of `agent.py`

### Issue: Import Error - langchain_groq not found
```
ModuleNotFoundError: No module named 'langchain_groq'
```

**Fix:**
```bash
pip install --upgrade langchain-groq
```

### Issue: Connection Refused (Can't reach localhost:8000)
```
ConnectionRefusedError: [Errno 111] Connection refused
```

**Fix:** Make sure server is running in Terminal 1:
```bash
python agent.py
```

### Issue: Request Timeout
```
timeout: The operation timed out
```

**Fix:** The LLM is taking too long. Either:
1. Try again (Groq API might be busy)
2. Use smaller request
3. Increase timeout in test_agent.py line 145: `timeout=180`

### Issue: File not found when downloading
```
HTTPException: Document not found
```

**Fix:** Run the agent first to generate document:
```bash
python test_agent.py
```

---

## How to Record Video Demo

### 1. Live Demo (3-4 minutes)
```
✅ Show terminal with server running
✅ Show curl request or API call
✅ Show response with task_plan
✅ Open generated output.docx file
✅ Run Test 2 (complex)
✅ Show results handling ambiguity
```

**Script:**
```
"Here's the autonomous agent. I'll submit a meeting request.
[show curl command]
The agent identified these tasks:
- Parse meeting details
- Structure minutes
- Create document

Here's the generated Word file [open document].
Perfect!

Now a complex request [submit]...
The request was ambiguous - no clear architecture.
Agent made these assumptions and documented them [show document].
Great!"
```

### 2. Architecture Explanation (2-3 minutes)
```
"FastAPI server receives natural language request →
LangGraph ReAct agent analyzes request →
Agent uses tools to call LLM for planning →
LLM creates task breakdown →
Agent calls create_word_document tool →
Document saved to disk →
Response returned to client with task plan"
```

### 3. Engineering Feature (1-2 minutes)
```
"I implemented ReAct Agent with Tool Calling.

ReAct = Reason + Act (interleaved)
- Agent thinks about what to do
- Calls tools to execute
- Can adjust based on results

Why?
- Assignment asks for autonomous planning
- Handles ambiguous requests better
- No hardcoded workflow

The create_word_document tool gives agent ability
to actually save files without manual code."
```

### 4. Tradeoff Discussion (1-2 minutes)
```
"TRADEOFF: Autonomy vs Simplicity

I chose autonomy (ReAct agent with tool calling).

Simple approach:
→ Hardcoded pipeline: Step 1, Step 2, Step 3

Complex approach:
→ Agent decides what to do based on request

Why complexity won:
1. Assignment specifically asks for autonomous planning
2. Handles complex/ambiguous requests better  
3. More impressive technically
4. Still completed in 60 minutes

Trade-off accepted: Slightly more code complexity
for better problem-solving capability."
```

---

## File Structure

```
ai-agent-project/
├── agent.py                 # Main agent implementation
├── test_agent.py            # Test suite with 2 test cases
├── requirements.txt         # Python dependencies
├── SETUP_GUIDE.md          # This file
├── output.docx             # Generated document (created after running)
└── README.md               # Project info
```

---

## Key Features Implemented

✅ **1. Autonomous Planning**
- Agent analyzes request
- Creates own task list
- No hardcoded workflow

✅ **2. ReAct Agent with Tool Calling**
- Integrated LangGraph for agentic reasoning
- Tool calling for document generation
- Multi-step reasoning

✅ **3. Error Handling**
- Try-catch blocks for LLM calls
- Graceful error messages
- Validation of API responses

✅ **4. Task List Extraction**
- Parses agent response for tasks
- Returns structured task_plan
- Shows in API response

✅ **5. Word Document Generation**
- python-docx for professional formatting
- Structured sections
- Timestamps

✅ **6. Two Test Cases**
- Test 1: Simple (straightforward)
- Test 2: Complex (ambiguous, multi-step)

---

## Performance Expectations

| Metric | Expected |
|--------|----------|
| Simple Request | 5-10 seconds |
| Complex Request | 10-20 seconds |
| Document Generation | <1 second |
| Total E2E | <30 seconds |

---

## API Response Example

```json
{
  "status": "success",
  "message": "✅ Agent executed successfully. Document generated.",
  "task_plan": [
    "Analyze and understand the user request for a product design document",
    "Identify required sections such as overview, features, technical requirements",
    "Generate comprehensive content based on the product design requirements",
    "Create formatted Word document with professional structure",
    "Validate document creation and return file path"
  ],
  "agent_reasoning": "The user requested a professional design document...",
  "document_created": true,
  "document_path": "output.docx",
  "execution_time": "15.32s"
}
```

---

## Tips for Success

1. **Start Simple** - Test with a basic request first
2. **Check Task Plan** - Make sure agent identified right tasks
3. **Verify Document** - Open the generated .docx file
4. **Test Complex Request** - See how agent handles ambiguity
5. **Record Demo** - Show both test cases in video

---

## Support & Debugging

**Check logs:**
```bash
# The server prints debug info
# Look for: ✅, ❌, ⚠️ symbols
```

**Run health check:**
```bash
curl http://localhost:8000/health
```

**Check if Groq API works:**
```python
python -c "
from langchain_groq import ChatGroq
import os
os.environ['GROQ_API_KEY'] = 'gsk_YOUR_KEY'
llm = ChatGroq(model_name='llama-3.1-8b-instant')
response = llm.invoke('Say hello')
print(response.content)
"
```

---

## Next Steps

1. ✅ Install dependencies: `pip install -r requirements.txt`
2. ✅ Add Groq API key to agent.py
3. ✅ Run server: `python agent.py`
4. ✅ Run tests: `python test_agent.py`
5. ✅ Verify output.docx is created
6. ✅ Record video demo (8-10 minutes)
7. ✅ Submit!

---

Good luck! 🚀 You've got this! 💪
