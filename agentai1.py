import OpenAI
import subprocess

# Uninstall and reinstall the OpenAI package
subprocess.run(["python", "-m", "pip", "uninstall", "openai", "-y"])
subprocess.run(["python", "-m", "pip", "install", "openai"])

#Set your API key
openai.api_key = ""

# Define the prompt
prompt = "What tech trends are we likely to see in 2025"

# Call the OpenAI API
response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )