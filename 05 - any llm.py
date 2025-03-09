from smolagents import CodeAgent, LiteLLMModel
from dotenv import load_dotenv
import os

load_dotenv()
# Inicializar el modelo
model = LiteLLMModel(
    model_id="gemini/gemini-2.0-flash",
    api_key=os.getenv("GEMINI_TOKEN"))  # Reemplaza con tu API key de OpenAI

messages = []
print("Chat iniciado. Escribe 'exit' para salir.")

while True:
    user_input = input("\nTú: ")
    
    if user_input.lower() == "exit":
        print("¡Hasta luego!")
        break

    messages.append({"role": "user", "content": user_input})

    try:
        response = model(messages, max_tokens=500)
        if response and hasattr(response, 'content'):
            assistant_message = response.content
            print("\nAsistente:", assistant_message)
            messages.append({"role": "assistant", "content": assistant_message})
        else:
            print("\nError: No se recibió una respuesta válida del modelo.")
            continue
    except Exception as e:
        print(f"\nError al procesar la respuesta: {str(e)}")
        continue