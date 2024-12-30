from openai import OpenAI

client = OpenAI()

def generate_response(prompt, model="gpt-4-turbo", max_tokens=150):
    """
    Generates a response using the OpenAI GPT-4 model.

    Parameters:
        prompt (str): The input text prompt for the model.
        model (str): The OpenAI model to use (default is "gpt-4-turbo").
        max_tokens (int): The maximum number of tokens to generate.

    Returns:
        str: The response generated by the model.
    """
    try:
        # Call the OpenAI API
        response = client.chat.completions.create(model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens)

        # Extract and return the response text
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Ensure your OpenAI API key is set as an environment variable or replace "your-api-key" with your actual key

    # Example prompt
    user_prompt = "What are the key benefits of AI in modern industries?"

    # Generate and print the response
    response = generate_response(user_prompt)
    print("AI Response:", response)
