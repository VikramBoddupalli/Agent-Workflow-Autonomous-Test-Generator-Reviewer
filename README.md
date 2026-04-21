# Agent Workflow: Autonomous Test Generator & Reviewer

An autonomous multi-agent system that generates and reviews test cases for Python code.

## Overview

This project implements a workflow with two specialized agents:

1. **Test Generator Agent** - Analyzes source code and automatically generates comprehensive test cases
2. **Test Reviewer Agent** - Reviews generated tests for quality, coverage, and best practices
3. **Workflow Orchestrator** - Coordinates both agents in an automated pipeline

## Features

### Test Generator Agent
- 🔍 Analyzes Python source code using AST parsing
- 🧪 Generates unit tests for functions
- 🔗 Generates integration tests for classes
- 📝 Creates edge case and error handling tests
- 🎯 Follows pytest conventions

### Test Reviewer Agent
- ✅ Validates test structure and syntax
- 📊 Checks for proper assertions
- 🏷️ Reviews naming conventions
- 📈 Analyzes test coverage patterns
- 🔬 Ensures test independence
- 💯 Generates quality scores (0-100)

### Workflow Orchestrator
- 🔄 Automated end-to-end workflow
- 📁 Batch processing of multiple files
- 📋 Comprehensive reporting
- ⚙️ Configurable quality thresholds

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd Agent-Workflow-Autonomous-Test-Generator-Reviewer-main

# No dependencies required - uses only Python standard library
```

## Usage

### Quick Start

Generate and review tests for a single file:

```bash
python workflow_orchestrator.py mymodule.py
```

Process an entire directory:

```bash
python workflow_orchestrator.py ./src ./tests
```

With custom quality threshold:

```bash
python workflow_orchestrator.py ./src ./tests 80
```

### Individual Agents

Run just the test generator:

```bash
python test_generator_agent.py mymodule.py
```

Run just the test reviewer:

```bash
python test_reviewer_agent.py test_mymodule.py
```

## Example Workflow

```
Input: calculator.py

┌─────────────────────────┐
│  Test Generator Agent   │
│  Analyzes calculator.py │
│  Creates test cases     │
└───────────┬─────────────┘
            │
            ▼
   test_calculator.py
            │
            ▼
┌─────────────────────────┐
│  Test Reviewer Agent    │
│  Reviews test quality   │
│  Scores: 85/100         │
└───────────┬─────────────┘
            │
            ▼
     Review Report
```

## Output

The workflow generates:

1. **Test Files** - `test_<original_filename>.py` with generated tests
2. **Review Reports** - Detailed quality analysis in console
3. **Workflow Report** - `workflow_report.txt` with summary of all processed files

## Quality Scoring

Tests are scored on multiple criteria:

- **Critical Issues** (-20 points each): Missing assertions, syntax errors, incomplete tests
- **Warnings** (-10 points each): Missing coverage patterns, naming issues
- **Info** (-5 points each): Missing docstrings, setup methods

**Passing Score**: 70/100 (configurable)

## Architecture

```
workflow_orchestrator.py
├── Coordinates workflow
├── Manages multiple files
└── Generates reports

test_generator_agent.py
├── Analyzes source code AST
├── Identifies functions/classes
└── Generates test templates

test_reviewer_agent.py
├── Validates test structure
├── Checks assertions
└── Calculates quality score
```

## Example Output

```
================================================================================
AUTONOMOUS TEST GENERATION & REVIEW WORKFLOW
================================================================================
Source: calculator.py
Output: ./tests
Minimum Score: 70/100
================================================================================

WORKFLOW: Processing calculator.py
================================================================================

STEP 1: Generating tests...
✓ Generated 3 test cases

STEP 2: Reviewing generated tests...
================================================================================
TEST REVIEW REPORT
================================================================================
File: test_calculator.py
Score: 65/100

CRITICAL (3)
--------------------------------------------------------------------------------
  [Assertions] Test 'test_add_basic' is incomplete (contains 'pass')
    Line: 12
    Suggestion: Implement test logic with proper assertions

⚠ Tests need improvement (score: 65/100)

================================================================================
WORKFLOW SUMMARY
================================================================================

Total Files Processed: 1
  ✓ Successful:        0
  ⚠ Needs Improvement: 1
  ✗ Failed:            0

Average Test Score: 65.0/100
```

## Extending the System

### Add New Review Checks

```python
def check_custom_pattern(self, code: str) -> List[ReviewFinding]:
    findings = []
    # Add your custom logic
    return findings

# Add to review() method in test_reviewer_agent.py
self.findings.extend(self.check_custom_pattern(code))
```

### Add New Test Types

```python
def generate_performance_tests(self, function_info: Dict) -> TestCase:
    # Generate performance tests
    return TestCase(...)

# Add to generate_tests_for_file() in test_generator_agent.py
```

## Limitations

- Currently supports Python files only
- Generates test templates that need manual implementation
- Requires pytest framework
- Best effort AST analysis (may miss complex patterns)

## Future Enhancements

- [ ] Support for additional languages (JavaScript, Java, Go)
- [ ] Integration with CI/CD pipelines
- [ ] Machine learning-based test generation
- [ ] Automatic test implementation using LLMs
- [ ] Visual coverage reports
- [ ] Test execution and validation
- [ ] Integration with version control systems

## Contributing

Contributions welcome! Areas for improvement:
- Additional review checks
- More sophisticated test generation
- Support for different testing frameworks
- Better error handling
- Performance optimizations

## License

MIT License - feel free to use and modify as needed.

## Contact

For questions or issues, please open an issue on the repository.
