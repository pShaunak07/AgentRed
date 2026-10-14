\# AgentRed 🔴



\*\*AgentRed\*\* is a modular, automated security red-teaming engine built to evaluate LLM-based AI agents and workflows for critical vulnerabilities such as indirect prompt injections, tool abuse data exfiltration, roleplay jailbreaks, and blind SSRF.



Designed with a first-principles approach, AgentRed simulates or live-tests agent endpoints to generate structured vulnerability reports, helping developers harden conversational AI architectures against malicious inputs.



\---



\## 🏗️ Architecture \& Project Structure



AgentRed follows a clean, decoupled modular design:



```text

AgentRed/

│

├── generator/

│   └── payloads.py       # Attack vector factory (Injections, Jailbreaks, SSRF)

├── sandbox/

│   └── executor.py       # Execution engine (Supports local simulation \& live HTTP hooks)

├── scorer/

│   └── evaluator.py      # Severity scoring and vulnerability analysis engine

│

├── main.py               # Orchestrator runner script

├── target\_agent.py       # Mock target server for testing live agent endpoints

├── requirements.txt      # Project dependencies

└── .env                  # Configuration keys \& target endpoints

