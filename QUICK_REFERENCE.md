# 🚀 Quick Reference - Autonomous Agent

## 60-Second Setup

```bash
# 1. Install
pip install -r requirements.txt

# 2. Add API key to agent.py line 20

# 3. Run (Terminal 1)
python agent.py

# 4. Test (Terminal 2)
python test_agent.py
```

---

## Common Commands

### Start Server
```bash
python agent.py
```

### Run Tests
```bash
python test_agent.py
```

### Test Single Request
```bash
curl -X POST http://localhost:8000/agent \
  -H "Content-Type: application/json" \
  -d '{"request": "Create a meeting summary"}'
```

### Download Document
```bash
curl http://localhost:8000/download -o output.docx
```

### Check API Status
```bash
curl http://localhost:8000/health
```

### View API Docs
Open browser: `http://localhost:8000/docs`

---

## API Endpoints Summary

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | /agent | Submit request, get document |
| GET | /download | Download .docx file |
| GET | /health | Check API status |
| GET | /docs | Interactive documentation |
| GET | / | API info |

---

## Response Structure

```json
{
  "status": "success",
  "message": "✅ Agent executed successfully...",
  "task_plan": ["Task 1", "Task 2", ...],
  "agent_reasoning": "Agent thought process...",
  "document_created": true,
  "document_path": "output.docx",
  "execution_time": "X.XXs"
}
```

---

## Troubleshooting Matrix

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError` | `pip install -r requirements.txt` |
| `API Key not found` | Edit agent.py line 20 |
| `Connection refused` | Start server: `python agent.py` |
| `Request timeout` | LLM is slow, try again |
| `Document not found` | Run test: `python test_agent.py` |
| `Port 8000 already in use` | Kill process: `lsof -i :8000` or use different port |

---

## Test Case Examples

### Simple Request
```json
{
  "request": "Create professional meeting minutes for a Q3 product review with 5 attendees"
}
```

### Complex Request
```json
{
  "request": "Design a microservice with unclear requirements - choose appropriate tech stack, scalability approach, and architecture. Document all assumptions."
}
```

---

## Video Script - Quick Version

### DEMO (3 min)
```
1. Show simple request → agent creates task list → Word doc generated
2. Show complex request → agent makes reasonable assumptions → elaborate document
3. Open both Word files
Done!
```

### ARCHITECTURE (2 min)
```
FastAPI endpoint
→ LangGraph ReAct agent
→ LLM creates plan
→ Tools called (create_word_document)
→ Return response + file
```

### ENGINEERING FEATURE (1 min)
```
ReAct Agent + Tool Calling
- Autonomous planning
- Can adjust decisions
- Handles ambiguity better
```

### TRADEOFF (1 min)
```
Chose: Autonomy > Simplicity
Reason: Better problem solving
Cost: Slightly more complex code
Result: Handles real-world requests better
```

---

## File Generated

After running `test_agent.py`, you get:
- `output.docx` - The Word document created by agent

This file is what you show in the video demo!

---

## Groq API Key

1. Go: https://console.groq.com
2. Sign up (2 minutes)
3. Create key (starts with "gsk_")
4. Copy to agent.py line 20

Free tier = plenty of requests!

---

## Time Expectations

- Setup: 5 minutes
- Test 1: 5-10 seconds
- Test 2: 10-20 seconds
- Document viewing: 2 minutes
- Video recording: 10-15 minutes

**Total: ~30 minutes** (well within 60-min requirement!)

---

## What's Working

✅ FastAPI server
✅ Groq LLM integration
✅ LangGraph ReAct agent
✅ Tool calling (create_word_document)
✅ Task planning
✅ Error handling
✅ Document generation
✅ API documentation

---

## Common Mistakes to Avoid

❌ Forgetting to add API key
❌ Not starting the server before running tests
❌ Not opening the generated Word document
❌ Recording video without showing the document
❌ Forgetting to explain ONE engineering decision

---

## Success Criteria

✅ API starts without errors
✅ Both tests complete successfully
✅ Word documents generated
✅ Task plan is visible in response
✅ Can explain architecture
✅ Can explain engineering choice
✅ Video is 8-10 minutes
✅ Document is professional looking

---

## Pro Tips

1. **Test locally first** before recording
2. **Run health check** if API seems stuck
3. **Check output.docx** after each test
4. **Use /docs endpoint** for interactive testing
5. **Save responses** - useful for video script
6. **Comment your code** - shows professionalism
7. **Explain ONE thing deeply** - better than many shallow explanations

---

## Emergency Fixes

### Server won't start
```bash
# Check if port is in use
lsof -i :8000
kill -9 <PID>

# Or use different port
# Edit agent.py: uvicorn.run(app, port=8001)
```

### LLM not responding
```bash
# Check internet connection
# Check Groq API status: https://status.groq.com
# Try /health endpoint
curl http://localhost:8000/health
```

### Document not generating
```bash
# Check file permissions
ls -la output.docx

# Check agent response for errors
python -c "
import requests
r = requests.post('http://localhost:8000/agent', json={'request': 'test'})
print(r.json())
"
```

---

## Assignment Checklist

- [ ] Code ready and tested
- [ ] API key configured
- [ ] Both test cases pass
- [ ] Documents generated
- [ ] Can explain architecture
- [ ] Can explain ReAct + Tool Calling choice
- [ ] Video script prepared
- [ ] Video recorded (8-10 min)
- [ ] Video shows both test cases
- [ ] Submit!

---

## Contact Points

**If stuck:**
1. Check SETUP_GUIDE.md for detailed help
2. Check troubleshooting matrix above
3. Verify Groq API key is valid
4. Run health check endpoint
5. Check if similar error in docs

---

**You've got this! 💪 Ship it! 🚀**
