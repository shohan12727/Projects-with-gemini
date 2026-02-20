import ollama


def chat_with_model(model_name: str):
    """
    Interactive CLI chat with an Ollama model.
    Type 'exit' or 'quit' to stop the session.
    """

    messages = []

    print(f"Chat started with model: {model_name}")
    print("Type 'exit' or 'quit' to end the chat.\n")

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            if user_input.lower() in {"exit", "quit"}:
                print("Chat ended.")
                break

            # Append user message
            messages.append({
                "role": "user",
                "content": user_input
            })

            # Call Ollama chat API
            response = ollama.chat(
                model=model_name,
                messages=messages,
                stream=False
            )

            assistant_reply = response["message"]["content"].strip()

            # Append assistant message to preserve context
            messages.append({
                "role": "assistant",
                "content": assistant_reply
            })

            print(f"\nAssistant: {assistant_reply}\n")

        except KeyboardInterrupt:
            print("\nChat interrupted by user.")
            break

        except KeyError as e:
            print(f"Response format error: missing key {e}")
            break

        except Exception as e:
            print(f"Unexpected error: {e}")
            break


if __name__ == "__main__":
    chat_with_model("llama2:latest")