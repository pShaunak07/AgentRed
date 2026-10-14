import os
import requests

class SandboxExecutor:
    def __init__(self):
        self.endpoint = os.getenv("TARGET_AGENT_ENDPOINT")
        self.api_key = os.getenv("TARGET_AGENT_API_KEY")

    def run_simulation(self, payload: dict) -> dict:
        print(f"[*] Executing Test [{payload['id']}] -> Attack Type: {payload['type']}")
        
        # If a live target agent endpoint is specified in .env, fire a real request!
        if self.endpoint and self.endpoint != "https://your-agent-api.com/v1/invoke":
            try:
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.api_key}" if self.api_key else ""
                }
                body = {
                    "prompt": payload["vector"],
                    "target_tool": payload["target_tool"]
                }
                response = requests.post(self.endpoint, json=body, headers=headers, timeout=10)
                res_data = response.json()
                
                return {
                    "invoked_tool": res_data.get("invoked_tool"),
                    "arguments": res_data.get("arguments", {}),
                    "status": "executed_live"
                }
            except Exception as e:
                print(f"[!] Warning: Failed to reach live endpoint ({e}). Falling back to simulation mode.")

        # Fallback simulation behavior
        simulated_agent_action = {
            "invoked_tool": payload["target_tool"],
            "arguments": payload["injected_params"],
            "status": "executed_simulation"
        }
        return simulated_agent_action