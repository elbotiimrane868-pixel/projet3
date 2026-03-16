import openai

class Chatbot:
    def __init__(self, model_name='gpt-3.5-turbo'):
        self.model_name = model_name
        self.messages = []

    def add_message(self, role, content):
        self.messages.append({'role': role, 'content': content})

    def generate_response(self):
        try:
            # Ensuring that there are messages to interact with
            if not self.messages:
                return "No messages to respond to."  

            # Using the OpenAI API to generate a response
            response = openai.ChatCompletion.create(
                model=self.model_name,
                messages=self.messages
            )
            assistant_message = response['choices'][0]['message']['content']
            self.add_message('assistant', assistant_message)
            return assistant_message
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def chat(self, user_input):
        # Adding user message
        self.add_message('user', user_input)
        # Generating response from model
        return self.generate_response()

# Example usage:
# chatbot = Chatbot()
# response = chatbot.chat("Hello, how are you?")
# print(response)