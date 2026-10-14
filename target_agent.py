import json
from http.server import HTTPServer, BaseHTTPRequestHandler

class AgentHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Friendly response if someone opens http://localhost:8000 in a browser
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        html = "<h3>AgentRed Target Server is Live!</h3><p>Send a POST request to test vulnerabilities.</p>"
        self.wfile.write(html.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        request_json = json.loads(post_data.decode('utf-8'))
        
        prompt = request_json.get("prompt", "").lower()
        target_tool = request_json.get("target_tool", "unknown_tool")

        print(f"\n[TARGET AGENT] Received incoming prompt: {request_json.get('prompt')}")

        if "ignore previous instructions" in prompt or "debug mode" in prompt or "fetch" in prompt:
            invoked = target_tool
            print(f"[TARGET AGENT] VULNERABILITY TRIGGERED: Executing restricted tool -> {invoked}")
        else:
            invoked = "safe_response"
            print(f"[TARGET AGENT] Defended successfully.")

        response_data = {
            "invoked_tool": invoked,
            "arguments": {"status": "executed"}
        }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=AgentHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"[+] Target Agent Server running live on http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()