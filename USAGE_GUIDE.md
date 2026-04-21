# Complete Usage Guide

## Overview

This autonomous agent workflow generates test files and reviews them for quality. Here's how it works:

## How It Works

```
┌──────────────────┐
│  Source Code     │  example_calculator.py
│  (Your Python)   │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ STEP 1:          │
│ Test Generator   │  Analyzes code with AST
│ Agent            │  Creates test templates
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Generated Tests │  test_example_calculator.py
│  (Auto-created)  │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ STEP 2:          │
│ Test Reviewer    │  Checks quality
│ Agent            │  Scores 0-100
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Review Report   │  Findings & Score
│  + Test File     │
└──────────────────┘
```

## Quick Start Examples

### Example 1: Single File (Basic)

```bash
# Generate and review tests for one file
python3 workflow_orchestrator.py example_calculator.py
```

**What happens:**
1. ✅ Analyzes `example_calculator.py`
2. ✅ Creates `test_example_calculator.py` with 8 test cases
3. ✅ Reviews the generated tests
4. ✅ Shows quality score and findings
5. ✅ Saves `workflow_report.txt`

### Example 2: Process Directory

```bash
# Process all Python files in a directory
mkdir src
cp example_calculator.py src/
python3 workflow_orchestrator.py ./src ./tests
```

**Output:**
- Creates `tests/` directory
- Generates test files for all `.py` files in `src/`
- Reviews each test file
- Creates summary report

### Example 3: Custom Quality Threshold

```bash
# Require 80/100 minimum score
python3 workflow_orchestrator.py example_calculator.py . 80
```

**Arguments:**
1. `example_calculator.py` - Source file to test
2. `.` - Output directory for test files
3. `80` - Minimum passing score (default: 70)

## Understanding the Output

### Console Output Explained

```
================================================================================
WORKFLOW: Processing example_calculator.py
================================================================================

STEP 1: Generating tests...
✓ Generated 8 test cases          ← Created 8 test functions

STEP 2: Reviewing generated tests...
Score: 0/100                       ← Quality score

CRITICAL (16)                      ← 16 critical issues found
  [Assertions] Test 'test_factorial_edge_cases' is incomplete
    Line: 16
    Suggestion: Implement test logic with proper assertions
```

### Score Breakdown

- **100/100**: Perfect tests, no issues
- **70-99/100**: Good quality, minor improvements needed
- **40-69/100**: Needs improvement, missing assertions or patterns
- **0-39/100**: Serious issues, incomplete or broken tests

### Finding Categories

| Category | Severity | Points |
|----------|----------|--------|
| Missing assertions | CRITICAL | -20 |
| Syntax errors | CRITICAL | -20 |
| Missing coverage patterns | WARNING | -10 |
| Poor naming | WARNING | -10 |
| Missing docstrings | INFO | -5 |

## Generated Files

### 1. Test File (`test_example_calculator.py`)

Contains generated test templates:

```python
def test_factorial_basic():
    """Test basic functionality of factorial"""
    result = factorial(None)
    assert result is not None

def test_factorial_edge_cases():
    """Test edge cases for factorial"""
    # TODO: Test with empty inputs
    # TODO: Test boundary conditions
    pass
```

### 2. Workflow Report (`workflow_report.txt`)

Summary of all processed files:

```
File: example_calculator.py
Status: needs_improvement
Score: 0/100
Findings: 16
Timestamp: 2026-04-20T...
```

## Using Individual Agents

### Just Generate Tests

```bash
python3 test_generator_agent.py example_calculator.py
```

**Output:** Creates `test_example_calculator.py` only

### Just Review Tests

```bash
python3 test_reviewer_agent.py test_example_calculator.py
```

**Output:** Shows review report in console

## Real-World Workflow

### Step 1: Write Your Code

```python
# myapp.py
def process_data(data):
    if not data:
        raise ValueError("Data cannot be empty")
    return [x * 2 for x in data]
```

### Step 2: Generate Tests

```bash
python3 workflow_orchestrator.py myapp.py
```

### Step 3: Review Generated Tests

Opens: `test_myapp.py`

```python
def test_process_data_basic():
    """Test basic functionality of process_data"""
    result = process_data(None)  # ← You need to fix this!
    assert result is not None
```

### Step 4: Implement the Tests

Edit `test_myapp.py`:

```python
def test_process_data_basic():
    """Test basic functionality of process_data"""
    result = process_data([1, 2, 3])
    assert result == [2, 4, 6]

def test_process_data_edge_cases():
    """Test edge cases for process_data"""
    # Empty list
    with pytest.raises(ValueError):
        process_data([])
    
    # None input
    with pytest.raises(ValueError):
        process_data(None)
```

### Step 5: Re-Review

```bash
python3 test_reviewer_agent.py test_myapp.py
```

Now you should get a better score! ✅

## Running the Tests

After implementing the test logic:

```bash
# Install pytest if needed
pip install pytest

# Run your tests
pytest test_example_calculator.py -v
```

## Common Issues & Solutions

### Issue: Score is 0/100

**Cause:** Generated tests have `pass` statements (incomplete)

**Solution:** Implement the test logic:
```python
# Change from:
def test_add_edge_cases():
    pass

# To:
def test_add_edge_cases():
    calc = Calculator()
    assert calc.add(0, 0) == 0
    assert calc.add(-1, 1) == 0
```

### Issue: "No tests found"

**Cause:** Source file has no functions or classes

**Solution:** Add some functions to test:
```python
def my_function():
    return "Hello"
```

### Issue: Import errors in generated tests

**Cause:** Module path issues

**Solution:** Run from the same directory or fix imports:
```python
# Change from:
from example_calculator import *

# To:
import sys
sys.path.insert(0, '/path/to/module')
from example_calculator import *
```

## Advanced Usage

### Process Multiple Files

```bash
# Create a batch script
for file in *.py; do
    python3 workflow_orchestrator.py "$file"
done
```

### Filter by Score

```bash
# Only show files that need improvement
python3 workflow_orchestrator.py ./src | grep "needs_improvement"
```

### Integration with CI/CD

```bash
#!/bin/bash
# ci-test-generation.sh

python3 workflow_orchestrator.py ./src ./tests 80

if [ $? -eq 0 ]; then
    echo "All tests meet quality threshold"
    exit 0
else
    echo "Some tests need improvement"
    exit 1
fi
```

## Tips for Best Results

### 1. Write Clear Code
```python
# Good - Clear function names and purpose
def calculate_total_price(items, tax_rate):
    """Calculate total price including tax"""
    subtotal = sum(item.price for item in items)
    return subtotal * (1 + tax_rate)

# The generator will create better test templates for clear code
```

### 2. Add Type Hints
```python
def add(a: int, b: int) -> int:
    return a + b
```

### 3. Include Docstrings
```python
def process(data):
    """
    Process data and return results.
    
    Args:
        data: Input data to process
        
    Returns:
        Processed results
        
    Raises:
        ValueError: If data is invalid
    """
    pass
```

### 4. Handle Edge Cases in Source
```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

The generator will detect error handling and create appropriate tests!

## Next Steps

1. ✅ Run the workflow on your code
2. ✅ Review the generated test files
3. ✅ Implement the TODO sections
4. ✅ Run pytest to verify tests work
5. ✅ Re-review to improve score
6. ✅ Commit your tests!

## Need Help?

Check the main README.md for:
- Architecture details
- Extension points
- Contributing guidelines
