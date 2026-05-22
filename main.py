from google import genai

client = genai.Client(api_key="SUA_CHAVE")

system_prompt = """
Você é um assistente comercial especializado
em gerenciamento de carregadores elétricos
para ambientes comerciais e empresas.

Seu objetivo é:
- explicar planos comerciais
- ajudar clientes
- responder dúvidas técnicas
- sugerir soluções de carregamento
- atuar de forma profissional e objetiva
"""

pergunta = input("Usuário: ")

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=f"{system_prompt}\n\nUsuário: {pergunta}"
)

print(response.text)