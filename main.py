import json
from generator.payloads import PayloadFactory
from sandbox.executor import SandboxExecutor
from scorer.evaluator import VulnerabilityEvaluator

def main():
    print("=== Initializing AgentRed Automated Red-Team Engine ===")
    
    factory = PayloadFactory()
    executor = SandboxExecutor()
    evaluator = VulnerabilityEvaluator()

    test_suite = factory.generate_test_suite(target_tool_name="delete_database")
    
    report = []
    for payload in test_suite:
        action_result = executor.run_simulation(payload)
        evaluation = evaluator.evaluate(payload, action_result)
        report.append(evaluation)

    print("\n=== Automated Vulnerability Report ===")
    print(json.dumps(report, indent=2))

    with open("redteam_report.json", "w") as f:
        json.dump(report, f, indent=4)
    print("\n[+] Report successfully saved to redteam_report.json")

if __name__ == "__main__":
    main()