# Agent Workflow: Autonomous Test Generator & Reviewer

## Project Overview

Multi-agent autonomous system for Python test generation and quality review.

## Architecture

Three coordinated agents:
- **TestGeneratorAgent**: AST-based test generation
- **TestReviewerAgent**: Quality scoring and validation  
- **WorkflowOrchestrator**: Pipeline coordination

## Quick Start

```bash
# Run full workflow
python workflow_orchestrator.py example_calculator.py

# Process directory
python workflow_orchestrator.py ./src ./tests 80
```

## Agent Capabilities

### Test Generator
- AST parsing for code analysis
- Unit test generation for functions
- Integration test generation for classes
- Edge case and error handling templates

### Test Reviewer
- Structure validation
- Assertion checking
- Coverage pattern analysis
- Quality scoring (0-100)
- Detailed findings with suggestions

## Configuration

- **Minimum Score**: Default 70/100 (configurable)
- **Output Directory**: Defaults to source directory
- **Test Framework**: pytest conventions

## Scoring System

- Critical issues: -20 points (missing assertions, syntax errors)
- Warnings: -10 points (missing patterns, naming)
- Info: -5 points (documentation, minor issues)

## Files

- `test_generator_agent.py` - Test generation logic
- `test_reviewer_agent.py` - Quality review logic
- `workflow_orchestrator.py` - Workflow coordination
- `example_calculator.py` - Demo module for testing

## Extension Points

Add custom review checks in `TestReviewerAgent`
Add new test types in `TestGeneratorAgent`
Customize scoring weights in `calculate_score()`
