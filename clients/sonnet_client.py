import anthropic
import os

class SonnetClient:
    def __init__(self):
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        self.client = anthropic.Anthropic(api_key=api_key)
    
    def send_message(self,message: str, role: str = "user") -> str:
        response = self.client.messages.create(
                model="claude-3-5-sonnet-20240620",
                messages=[{"role": role, "content": message}], 
                max_tokens=15000
                )
        return response 
