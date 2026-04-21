#!/bin/bash
# Demo script showing how to use the agent workflow

echo "=================================="
echo "AGENT WORKFLOW DEMO"
echo "=================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Step 1: Show the source code
echo -e "${BLUE}STEP 1: Source Code${NC}"
echo "-----------------------------------"
echo "File: example_calculator.py"
echo ""
head -20 example_calculator.py
echo "... (more functions below)"
echo ""
read -p "Press Enter to continue..."
echo ""

# Step 2: Generate tests
echo -e "${BLUE}STEP 2: Generate Tests${NC}"
echo "-----------------------------------"
echo "Running: python3 test_generator_agent.py example_calculator.py"
echo ""
python3 test_generator_agent.py example_calculator.py
echo ""
read -p "Press Enter to continue..."
echo ""

# Step 3: Show generated test file
echo -e "${BLUE}STEP 3: Generated Test File${NC}"
echo "-----------------------------------"
echo "File: test_example_calculator.py (first 30 lines)"
echo ""
head -30 test_example_calculator.py
echo "... (more tests below)"
echo ""
read -p "Press Enter to continue..."
echo ""

# Step 4: Review the generated tests
echo -e "${BLUE}STEP 4: Review Generated Tests${NC}"
echo "-----------------------------------"
echo "Running: python3 test_reviewer_agent.py test_example_calculator.py"
echo ""
python3 test_reviewer_agent.py test_example_calculator.py
echo ""
read -p "Press Enter to continue..."
echo ""

# Step 5: Show complete implementation
echo -e "${BLUE}STEP 5: Properly Implemented Tests${NC}"
echo "-----------------------------------"
echo "File: test_example_calculator_complete.py (showing a few tests)"
echo ""
sed -n '19,40p' test_example_calculator_complete.py
echo "... (more complete tests in the file)"
echo ""
read -p "Press Enter to continue..."
echo ""

# Step 6: Review the complete implementation
echo -e "${BLUE}STEP 6: Review Complete Implementation${NC}"
echo "-----------------------------------"
echo "Running: python3 test_reviewer_agent.py test_example_calculator_complete.py"
echo ""
python3 test_reviewer_agent.py test_example_calculator_complete.py
echo ""
read -p "Press Enter to continue..."
echo ""

# Step 7: Run complete workflow
echo -e "${BLUE}STEP 7: Full Workflow (All-in-One)${NC}"
echo "-----------------------------------"
echo "Running: python3 workflow_orchestrator.py example_calculator.py"
echo ""
python3 workflow_orchestrator.py example_calculator.py
echo ""
read -p "Press Enter to continue..."
echo ""

# Step 8: Show workflow report
echo -e "${BLUE}STEP 8: Workflow Report${NC}"
echo "-----------------------------------"
echo "File: workflow_report.txt"
echo ""
cat workflow_report.txt
echo ""

echo -e "${GREEN}=================================="
echo "DEMO COMPLETE!"
echo "==================================${NC}"
echo ""
echo "Next steps:"
echo "1. Edit test_example_calculator.py and implement the TODOs"
echo "2. Run: pytest test_example_calculator.py -v"
echo "3. Re-review with: python3 test_reviewer_agent.py test_example_calculator.py"
echo ""
echo "Files created:"
echo "  - test_example_calculator.py (template - needs implementation)"
echo "  - test_example_calculator_complete.py (example of completed tests)"
echo "  - workflow_report.txt (summary report)"
echo ""
