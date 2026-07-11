"""
TEST SUITE for Autonomous AI Agent
Two test cases: Simple + Complex (as per assignment requirement)
"""

import requests
import json
import time

BASE_URL = "http://localhost:8000"

# Colors for terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*70}")
    print(f"  {text}")
    print(f"{'='*70}{Colors.ENDC}\n")

def print_success(text):
    print(f"{Colors.OKGREEN} {text}{Colors.ENDC}")

def print_info(text):
    print(f"{Colors.OKCYAN}ℹ {text}{Colors.ENDC}")

def print_warning(text):
    print(f"{Colors.WARNING}  {text}{Colors.ENDC}")

def print_error(text):
    print(f"{Colors.FAIL} {text}{Colors.ENDC}")

# TEST 1: SIMPLE REQUEST

test_1_request = """
Create a professional meeting minutes document for a Product Roadmap Review Meeting.

Include:
- Meeting Title: Product Roadmap Review Meeting Q3 2026
- Date: July 12, 2026
- Attendees: Alice Johnson (Product Manager), Bob Smith (Engineering Lead), Carol Davis (Design Lead), David Chen (QA Lead), Eve Wilson (Product Analyst)
- Meeting Duration: 1 hour
- Three main agenda items that were discussed:
  1. New features for mobile app
  2. Performance optimization roadmap
  3. Customer feedback integration plan
- Action Items with owners and due dates
- Next meeting date

Format it as a professional business document.
"""

# TEST 2: COMPLEX REQUEST (AMBIGUOUS/MULTI-STEP)

test_2_request = """
Create a technical design document for building a new microservice, but make reasonable assumptions because:

AMBIGUOUS REQUIREMENTS:
- Architecture not specified (decide between REST, gRPC, or hybrid)
- Tech stack not chosen (decide on appropriate technologies)
- Scalability requirements vague (assume handling 100K+ requests/day)
- Database choice not specified (decide on SQL vs NoSQL)
- Integration points unclear (assume 2-3 common services like authentication, payment, logging)

The agent MUST:
1. Make reasonable assumptions for all ambiguous points
2. Explain each assumption clearly in the document
3. Justify why certain choices were made
4. Create a complete technical design including:
   - System architecture diagram (textual description)
   - API endpoints
   - Database schema outline
   - Deployment strategy
   - Risk mitigation

This tests the agent's ability to handle incomplete information and autonomous decision-making.
"""

# HELPER FUNCTIONS

def test_health_check():
    """Check if API is running"""
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            data = response.json()
            print_success(f"API is healthy!")
            print_info(f"LLM: {data.get('llm')}")
            print_info(f"API Key Configured: {data.get('api_key_configured')}")
            return True
        else:
            print_error(f"API health check failed: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Cannot connect to API: {str(e)}")
        print_info("Make sure the API is running: python agent.py")
        return False

def run_test(test_name, request_text, test_number):
    """Run a single test"""
    print_header(f"TEST {test_number}: {test_name}")
    print_info(f"Request: {request_text[:100]}...")
    
    try:
        # Send request to agent
        print_info("Sending request to agent...")
        start_time = time.time()
        
        response = requests.post(
            f"{BASE_URL}/agent",
            json={"request": request_text},
            timeout=120  # 2 minute timeout
        )
        
        elapsed = time.time() - start_time
        
        if response.status_code == 200:
            data = response.json()
            
            print_success(f"Agent completed in {elapsed:.2f} seconds")
            print(f"\n{Colors.BOLD}Agent Response:{Colors.ENDC}")
            print(f"Status: {data['status']}")
            print(f"Message: {data['message']}")
            
            print(f"\n{Colors.BOLD}Task Plan Identified:{Colors.ENDC}")
            for i, task in enumerate(data['task_plan'], 1):
                print(f"  {i}. {task}")
            
            print(f"\n{Colors.BOLD}Document Created:{Colors.ENDC}")
            print(f"  Created: {data['document_created']}")
            print(f"  Path: {data['document_path']}")
            
            print(f"\n{Colors.BOLD}Agent Reasoning (first 300 chars):{Colors.ENDC}")
            print(f"  {data['agent_reasoning'][:300]}...")
            
            return True
            
        else:
            print_error(f"API returned status code: {response.status_code}")
            print_error(f"Error: {response.text}")
            return False
    
    except requests.exceptions.Timeout:
        print_error("Request timed out (API took too long)")
        return False
    except Exception as e:
        print_error(f"Error running test: {str(e)}")
        return False

def check_document():
    """Check if document was created"""
    import os
    print_header("Document Verification")
    
    if os.path.exists("output.docx"):
        file_size = os.path.getsize("output.docx")
        print_success(f"Document found: output.docx")
        print_info(f"File size: {file_size} bytes")
        print_info(f"You can open this file with Microsoft Word or any office suite")
        return True
    else:
        print_warning("output.docx not found in current directory")
        print_info("Document may have been saved in a different location")
        return False

# MAIN TEST SUITE

def main():
    print(f"""
    {Colors.HEADER}{Colors.BOLD}
    ╔════════════════════════════════════════════════════════╗
    ║   🤖 AUTONOMOUS AI AGENT - TEST SUITE                  ║
    ║        An autonomous AI agent that generates professional Word documents based on user requests. ║
    ╚════════════════════════════════════════════════════════╝
    {Colors.ENDC}
    """)
    
    # Step 1: Health check
    print_header("Step 1: Health Check")
    if not test_health_check():
        print_error("Cannot proceed without API running!")
        return
    
    # Step 2: Run Test 1 (Simple)
    print_header("Step 2: Run Simple Test")
    test1_passed = run_test(
        "SIMPLE REQUEST",
        test_1_request,
        test_number=1
    )
    
    time.sleep(2)  # Wait between tests
    
    # Step 3: Run Test 2 (Complex)
    print_header("Step 3: Run Complex Test")
    test2_passed = run_test(
        "COMPLEX REQUEST (Ambiguous/Multi-step)",
        test_2_request,
        test_number=2
    )
    
    time.sleep(2)
    
    # Step 4: Check document
    check_document()
    
    # Summary
    print_header("Test Summary")
    print(f"Test 1 (Simple): {' PASSED' if test1_passed else ' FAILED'}")
    print(f"Test 2 (Complex): {'PASSED' if test2_passed else ' FAILED'}")
    
    if test1_passed and test2_passed:
        print_success("All tests completed successfully! ")
        print_info("Next: Record video demo with these results")
    else:
        print_warning("Some tests failed. Check the agent API and try again.")
    
    print(f"\n{Colors.BOLD}How to download the document:{Colors.ENDC}")
    print(f"  URL: {BASE_URL}/download")
    print(f"  Or simply: curl {BASE_URL}/download -o my_document.docx")
    
    print(f"\n{Colors.BOLD}API Documentation:{Colors.ENDC}")
    print(f"  Swagger UI: {BASE_URL}/docs")
    print(f"  ReDoc: {BASE_URL}/redoc")

if __name__ == "__main__":
    main()
