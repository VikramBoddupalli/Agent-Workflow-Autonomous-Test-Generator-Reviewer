"""
Workflow Orchestrator

Coordinates the Test Generator and Test Reviewer agents in an autonomous workflow.
"""

import os
import sys
from typing import List, Dict, Any
from dataclasses import dataclass
from datetime import datetime

from test_generator_agent import TestGeneratorAgent
from test_reviewer_agent import TestReviewerAgent, Severity


@dataclass
class WorkflowResult:
    """Result of a complete workflow execution"""
    source_file: str
    test_file: str
    generated: bool
    reviewed: bool
    score: int
    findings_count: int
    timestamp: str
    status: str  # success, failed, needs_improvement


class WorkflowOrchestrator:
    """Orchestrates the autonomous test generation and review workflow"""

    def __init__(self, source_path: str, output_dir: str = None, min_score: int = 70):
        self.source_path = source_path
        self.output_dir = output_dir or os.path.dirname(source_path) or '.'
        self.min_score = min_score
        self.results: List[WorkflowResult] = []

    def execute_workflow(self, source_file: str) -> WorkflowResult:
        """Execute the complete workflow for a single source file"""
        print(f"\n{'='*80}")
        print(f"WORKFLOW: Processing {source_file}")
        print(f"{'='*80}\n")

        test_file = None
        generated = False
        reviewed = False
        score = 0
        findings_count = 0
        status = "failed"

        try:
            print("STEP 1: Generating tests...")
            generator = TestGeneratorAgent(source_file)
            tests = generator.generate_tests_for_file(source_file)

            if tests:
                test_file_name = f"test_{os.path.basename(source_file)}"
                test_file = os.path.join(self.output_dir, test_file_name)
                generator.generate_test_file(source_file, test_file)
                generated = True
                print(f"✓ Generated {len(tests)} test cases\n")
            else:
                print("✗ No tests generated\n")
                status = "no_tests"

        except Exception as e:
            print(f"✗ Test generation failed: {str(e)}\n")
            status = "generation_failed"

        if generated and test_file and os.path.exists(test_file):
            try:
                print("STEP 2: Reviewing generated tests...")
                reviewer = TestReviewerAgent(test_file)
                review_result = reviewer.review()

                reviewed = True
                score = review_result['score']
                findings_count = len(review_result['findings'])

                if score >= self.min_score:
                    status = "success"
                    print(f"✓ Tests passed review (score: {score}/100)\n")
                else:
                    status = "needs_improvement"
                    print(f"⚠ Tests need improvement (score: {score}/100)\n")

            except Exception as e:
                print(f"✗ Test review failed: {str(e)}\n")
                status = "review_failed"

        result = WorkflowResult(
            source_file=source_file,
            test_file=test_file or "",
            generated=generated,
            reviewed=reviewed,
            score=score,
            findings_count=findings_count,
            timestamp=datetime.now().isoformat(),
            status=status
        )

        self.results.append(result)
        return result

    def process_directory(self, directory: str) -> List[WorkflowResult]:
        """Process all Python files in a directory"""
        python_files = [
            os.path.join(directory, f)
            for f in os.listdir(directory)
            if f.endswith('.py') and not f.startswith('test_')
        ]

        print(f"Found {len(python_files)} Python files to process")

        for python_file in python_files:
            self.execute_workflow(python_file)

        return self.results

    def run(self) -> List[WorkflowResult]:
        """Main execution method"""
        print("\n" + "="*80)
        print("AUTONOMOUS TEST GENERATION & REVIEW WORKFLOW")
        print("="*80)
        print(f"Source: {self.source_path}")
        print(f"Output: {self.output_dir}")
        print(f"Minimum Score: {self.min_score}/100")
        print("="*80 + "\n")

        if os.path.isfile(self.source_path):
            self.execute_workflow(self.source_path)
        elif os.path.isdir(self.source_path):
            self.process_directory(self.source_path)
        else:
            print(f"Error: {self.source_path} is not a valid file or directory")
            return []

        self.generate_summary()
        return self.results

    def generate_summary(self):
        """Generate a summary report of all workflow executions"""
        print("\n" + "="*80)
        print("WORKFLOW SUMMARY")
        print("="*80 + "\n")

        total = len(self.results)
        successful = sum(1 for r in self.results if r.status == "success")
        needs_improvement = sum(1 for r in self.results if r.status == "needs_improvement")
        failed = total - successful - needs_improvement

        print(f"Total Files Processed: {total}")
        print(f"  ✓ Successful:        {successful}")
        print(f"  ⚠ Needs Improvement: {needs_improvement}")
        print(f"  ✗ Failed:            {failed}")

        if self.results:
            avg_score = sum(r.score for r in self.results) / len(self.results)
            print(f"\nAverage Test Score: {avg_score:.1f}/100")

        print("\nDetailed Results:")
        print("-" * 80)

        for result in self.results:
            status_symbol = {
                "success": "✓",
                "needs_improvement": "⚠",
                "failed": "✗",
                "no_tests": "○",
                "generation_failed": "✗",
                "review_failed": "⚠"
            }.get(result.status, "?")

            print(f"{status_symbol} {os.path.basename(result.source_file)}")
            print(f"  Generated: {result.generated}, Reviewed: {result.reviewed}")
            if result.reviewed:
                print(f"  Score: {result.score}/100, Findings: {result.findings_count}")
            if result.test_file:
                print(f"  Test file: {os.path.basename(result.test_file)}")
            print()

        print("=" * 80 + "\n")

        report_file = os.path.join(self.output_dir, "workflow_report.txt")
        with open(report_file, 'w') as f:
            f.write(f"Workflow Report - {datetime.now().isoformat()}\n")
            f.write("=" * 80 + "\n\n")
            for result in self.results:
                f.write(f"File: {result.source_file}\n")
                f.write(f"Status: {result.status}\n")
                f.write(f"Score: {result.score}/100\n")
                f.write(f"Findings: {result.findings_count}\n")
                f.write(f"Timestamp: {result.timestamp}\n")
                f.write("-" * 80 + "\n")

        print(f"Report saved to: {report_file}")


def main():
    """CLI entry point"""
    if len(sys.argv) < 2:
        print("Usage: python workflow_orchestrator.py <source_path> [output_dir] [min_score]")
        print("\nExample:")
        print("  python workflow_orchestrator.py ./src")
        print("  python workflow_orchestrator.py ./mymodule.py ./tests 80")
        sys.exit(1)

    source_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    min_score = int(sys.argv[3]) if len(sys.argv) > 3 else 70

    orchestrator = WorkflowOrchestrator(source_path, output_dir, min_score)
    results = orchestrator.run()

    successful = sum(1 for r in results if r.status == "success")
    exit_code = 0 if successful == len(results) else 1
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
