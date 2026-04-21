"""
Autonomous Test Reviewer Agent

This agent reviews generated tests for quality, coverage, and best practices.
"""

import ast
import re
from typing import List, Dict, Any
from dataclasses import dataclass
from enum import Enum


class Severity(Enum):
    """Review finding severity levels"""
    CRITICAL = "critical"
    WARNING = "warning"
    INFO = "info"


@dataclass
class ReviewFinding:
    """Represents a review finding"""
    severity: Severity
    category: str
    message: str
    line_number: int = None
    suggestion: str = None


class TestReviewerAgent:
    """Agent that autonomously reviews test quality"""

    def __init__(self, test_file_path: str):
        self.test_file_path = test_file_path
        self.findings: List[ReviewFinding] = []
        self.score = 0

    def load_test_file(self) -> str:
        """Load the test file content"""
        with open(self.test_file_path, 'r') as f:
            return f.read()

    def check_test_structure(self, code: str) -> List[ReviewFinding]:
        """Check test file structure and organization"""
        findings = []

        try:
            tree = ast.parse(code)
        except SyntaxError as e:
            findings.append(ReviewFinding(
                severity=Severity.CRITICAL,
                category="Syntax",
                message=f"Syntax error in test file: {str(e)}",
                line_number=e.lineno
            ))
            return findings

        has_imports = False
        test_count = 0

        for node in ast.walk(tree):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                has_imports = True
            elif isinstance(node, ast.FunctionDef):
                if node.name.startswith('test_'):
                    test_count += 1

        if not has_imports:
            findings.append(ReviewFinding(
                severity=Severity.WARNING,
                category="Structure",
                message="No imports found in test file",
                suggestion="Add necessary imports for testing framework and code under test"
            ))

        if test_count == 0:
            findings.append(ReviewFinding(
                severity=Severity.CRITICAL,
                category="Structure",
                message="No test functions found",
                suggestion="Add test functions with names starting with 'test_'"
            ))

        return findings

    def check_test_naming(self, code: str) -> List[ReviewFinding]:
        """Check test naming conventions"""
        findings = []

        try:
            tree = ast.parse(code)
        except SyntaxError:
            return findings

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if node.name.startswith('test_'):
                    if len(node.name) < 10:
                        findings.append(ReviewFinding(
                            severity=Severity.WARNING,
                            category="Naming",
                            message=f"Test name '{node.name}' is too short",
                            line_number=node.lineno,
                            suggestion="Use descriptive test names that explain what is being tested"
                        ))

                    if not ast.get_docstring(node):
                        findings.append(ReviewFinding(
                            severity=Severity.INFO,
                            category="Documentation",
                            message=f"Test '{node.name}' missing docstring",
                            line_number=node.lineno,
                            suggestion="Add docstring explaining test purpose"
                        ))

        return findings

    def check_assertions(self, code: str) -> List[ReviewFinding]:
        """Check for proper use of assertions"""
        findings = []

        try:
            tree = ast.parse(code)
        except SyntaxError:
            return findings

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name.startswith('test_'):
                has_assert = False
                has_pass = False

                for child in ast.walk(node):
                    if isinstance(child, ast.Assert):
                        has_assert = True
                    elif isinstance(child, ast.Pass):
                        has_pass = True

                if has_pass and not has_assert:
                    findings.append(ReviewFinding(
                        severity=Severity.CRITICAL,
                        category="Assertions",
                        message=f"Test '{node.name}' is incomplete (contains 'pass')",
                        line_number=node.lineno,
                        suggestion="Implement test logic with proper assertions"
                    ))
                elif not has_assert:
                    findings.append(ReviewFinding(
                        severity=Severity.CRITICAL,
                        category="Assertions",
                        message=f"Test '{node.name}' has no assertions",
                        line_number=node.lineno,
                        suggestion="Add assertions to verify expected behavior"
                    ))

        return findings

    def check_test_coverage_patterns(self, code: str) -> List[ReviewFinding]:
        """Check for common test coverage patterns"""
        findings = []

        patterns = {
            'edge_case': r'test.*edge',
            'error_handling': r'test.*(error|exception|invalid)',
            'boundary': r'test.*(boundary|limit|max|min)',
            'integration': r'test.*(integration|workflow)'
        }

        found_patterns = {key: False for key in patterns}

        for pattern_name, pattern in patterns.items():
            if re.search(pattern, code, re.IGNORECASE):
                found_patterns[pattern_name] = True

        missing_patterns = [name for name, found in found_patterns.items() if not found]

        if missing_patterns:
            findings.append(ReviewFinding(
                severity=Severity.WARNING,
                category="Coverage",
                message=f"Missing test patterns: {', '.join(missing_patterns)}",
                suggestion="Consider adding tests for edge cases, error handling, and boundaries"
            ))

        return findings

    def check_test_independence(self, code: str) -> List[ReviewFinding]:
        """Check if tests are independent"""
        findings = []

        if 'global ' in code:
            findings.append(ReviewFinding(
                severity=Severity.WARNING,
                category="Independence",
                message="Tests use global variables",
                suggestion="Tests should be independent and not rely on global state"
            ))

        try:
            tree = ast.parse(code)
            class_tests = []

            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    for item in node.body:
                        if isinstance(item, ast.FunctionDef) and item.name.startswith('test_'):
                            class_tests.append(item.name)

            if class_tests:
                has_setup = any('setup' in str(node.name).lower()
                               for node in ast.walk(tree)
                               if isinstance(node, ast.FunctionDef))

                if not has_setup:
                    findings.append(ReviewFinding(
                        severity=Severity.INFO,
                        category="Setup",
                        message="Test class missing setup method",
                        suggestion="Consider adding setup_method or fixtures for test isolation"
                    ))
        except SyntaxError:
            pass

        return findings

    def calculate_score(self) -> int:
        """Calculate test quality score (0-100)"""
        if not self.findings:
            return 100

        critical_count = sum(1 for f in self.findings if f.severity == Severity.CRITICAL)
        warning_count = sum(1 for f in self.findings if f.severity == Severity.WARNING)
        info_count = sum(1 for f in self.findings if f.severity == Severity.INFO)

        score = 100
        score -= critical_count * 20
        score -= warning_count * 10
        score -= info_count * 5

        return max(0, score)

    def generate_report(self) -> str:
        """Generate a comprehensive review report"""
        report = f"""
{'='*80}
TEST REVIEW REPORT
{'='*80}
File: {self.test_file_path}
Score: {self.score}/100

"""

        if not self.findings:
            report += "✓ No issues found. Tests look good!\n"
        else:
            by_severity = {
                Severity.CRITICAL: [],
                Severity.WARNING: [],
                Severity.INFO: []
            }

            for finding in self.findings:
                by_severity[finding.severity].append(finding)

            for severity in [Severity.CRITICAL, Severity.WARNING, Severity.INFO]:
                findings = by_severity[severity]
                if findings:
                    report += f"\n{severity.value.upper()} ({len(findings)})\n"
                    report += "-" * 80 + "\n"

                    for finding in findings:
                        report += f"  [{finding.category}] {finding.message}\n"
                        if finding.line_number:
                            report += f"    Line: {finding.line_number}\n"
                        if finding.suggestion:
                            report += f"    Suggestion: {finding.suggestion}\n"
                        report += "\n"

        report += "=" * 80 + "\n"
        return report

    def review(self) -> Dict[str, Any]:
        """Main review method"""
        print(f"TestReviewerAgent reviewing: {self.test_file_path}")

        code = self.load_test_file()

        self.findings.extend(self.check_test_structure(code))
        self.findings.extend(self.check_test_naming(code))
        self.findings.extend(self.check_assertions(code))
        self.findings.extend(self.check_test_coverage_patterns(code))
        self.findings.extend(self.check_test_independence(code))

        self.score = self.calculate_score()

        report = self.generate_report()
        print(report)

        return {
            'score': self.score,
            'findings': self.findings,
            'report': report,
            'passed': self.score >= 70
        }


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python test_reviewer_agent.py <test_file_path>")
        sys.exit(1)

    agent = TestReviewerAgent(sys.argv[1])
    result = agent.review()

    sys.exit(0 if result['passed'] else 1)
