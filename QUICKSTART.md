# Quick Start Guide

## 🚀 Try It in 30 Seconds

```bash
# Run the complete workflow on example file
python3 workflow_orchestrator.py example_calculator.py

# That's it! Tests are generated and reviewed automatically.
```

## 📊 What Just Happened?

1. ✅ **Analyzed** `example_calculator.py` 
2. ✅ **Generated** `test_example_calculator.py` with 8 test cases
3. ✅ **Reviewed** the tests and scored them
4. ✅ **Created** `workflow_report.txt` with findings

## 📁 Files Created

```
test_example_calculator.py     ← Generated test templates
workflow_report.txt            ← Summary report
```

## 👀 See What Was Generated

```bash
# View the generated test file
cat test_example_calculator.py

# View the workflow report
cat workflow_report.txt
```

## 🎯 Understanding the Output

### Score: 0/100 (Generated Templates)
- Generated tests are **templates** with TODO comments
- They need to be **implemented** by you
- Score improves as you add assertions

### Score: 50-70/100 (Good Tests)
- Tests have proper assertions
- Minor improvements needed
- Ready for production use

### Score: 80-100/100 (Excellent Tests)
- Comprehensive coverage
- All patterns present
- Best practices followed

## ✏️ Next Steps

### 1. Open the Generated Test File

```bash
# Open in your editor
nano test_example_calculator.py
# or
code test_example_calculator.py
```

### 2. Implement the TODOs

**Before (Generated):**
```python
def test_factorial_basic():
    """Test basic functionality of factorial"""
    result = factorial(None)  # TODO: Fix this
    assert result is not None
```

**After (Your Implementation):**
```python
def test_factorial_basic():
    """Test basic functionality of factorial"""
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1
```

### 3. Review Again

```bash
python3 test_reviewer_agent.py test_example_calculator.py
```

Score should improve! 📈

### 4. Run Your Tests

```bash
# Install pytest if needed
pip install pytest

# Run the tests
pytest test_example_calculator.py -v
```

## 🎬 Interactive Demo

```bash
# Run the step-by-step demo
./demo.sh
```

## 📚 Complete Example

See `test_example_calculator_complete.py` for a fully implemented example.

```bash
# Review the complete version
python3 test_reviewer_agent.py test_example_calculator_complete.py

# See the difference in scores!
```

## 🔧 Use With Your Own Code

```bash
# Single file
python3 workflow_orchestrator.py your_module.py

# Entire directory
python3 workflow_orchestrator.py ./src ./tests

# With custom threshold
python3 workflow_orchestrator.py your_module.py . 80
```

## 💡 Pro Tips

### Tip 1: Better Code = Better Tests
```python
# Good: Clear, documented function
def calculate_tax(amount: float, rate: float) -> float:
    """Calculate tax on amount"""
    if rate < 0 or rate > 1:
        raise ValueError("Rate must be between 0 and 1")
    return amount * rate
```
Generates better test templates automatically!

### Tip 2: Use Type Hints
```python
def add(a: int, b: int) -> int:  # Type hints help!
    return a + b
```

### Tip 3: Review Iteratively
```bash
# Generate → Implement → Review → Improve
python3 workflow_orchestrator.py mycode.py
# Edit tests
python3 test_reviewer_agent.py test_mycode.py
# Repeat until score is good
```

## 🐛 Troubleshooting

### "command not found: python"
Use `python3` instead of `python`

### "No module named 'pytest'"
```bash
pip install pytest
```

### Tests generated but empty
That's normal! Implement the TODOs.

### Import errors when running tests
Make sure you're in the correct directory:
```bash
cd /path/to/your/code
python3 workflow_orchestrator.py .
```

## 📖 More Details

- **Full documentation**: See `README.md`
- **Complete usage guide**: See `USAGE_GUIDE.md`
- **Example implementation**: See `test_example_calculator_complete.py`

## 🎉 That's It!

You now have:
- ✅ Autonomous test generation
- ✅ Automatic quality review
- ✅ Test templates ready to implement
- ✅ Quality scores and feedback

Happy testing! 🚀
