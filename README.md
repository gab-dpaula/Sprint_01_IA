Assistente Comercial com Gemini

Este projeto implementa um **assistente comercial especializado em gerenciamento de carregadores elétricos** para ambientes comerciais e
empresas.  
O código utiliza a **API Gemini** para responder perguntas de forma profissional e objetiva, além de contar com uma base de perguntas e
respostas pré-definidas da Sprint 1.


Como executar:

1. Instale a biblioteca oficial:
   ```bash
   pip install google-genai

2. Configure sua chave de API no código:
    client = genai.Client(api_key="SUA_CHAVE")

3. Execute o programa:
    python main.py

Explicação do Código:

1. Importação:
    from google import genai

2. Configuração do cliente:
    client = genai.Client(api_key="SUA_CHAVE")

3. System Prompt:
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

4. Entrada do usuário:
    pergunta = input("Usuário: ")

5. Chamada ao modelo:
    response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=f"{system_prompt}\n\nUsuário: {pergunta}"
)

6. Saída:
    print(response.text)

Perguntas e Respostas: 

|**PERGUNTA:**|**RESPOSTA ESPERADA:**|
|-|-|
|Quais carregadores estão disponíveis neste momento?|Os carregadores 3,4 e 7 estão disponíveis, o 6 esta prestes a ser liberado  e o 2 se encontra em manutenção. |
|Minha recarga foi interrompida, o que aconteceu?|A interrupção pode ter acontecido por:<br />- instabilidade elétrica<br />- desconexão do veículo<br />- limite de potência atingido<br />- falha temporária no carregador<br /><br />Verifique se o cabo está corretamente conectado.<br />se o problema continua , entre em contato com o suporte técnico.|
|Quanto custa a recarga?|Dependendo da potência escolhida pelo usuário e do tempo de uso , o preço pode variar , tendo um custo de R$XX.XX por hora e um aumento de R$XX.XX entre as potência disponíveis. |
|Quanto custou a minha última recarga?|Sua última recarga foi de XX kWh, com custo estimado de R$XX.XX.|
|Quanto tempo falta para terminar a minha recarga?|Sua recarga no posto 2 <br />Com carregamento rápido, esta em 81%,terminará em aproximadamente XX minutos .|
|Quais formas de pagamento estão disponíveis?|Do posto 1 ao 5 é aceito cartão (credito/debito), pix ou Apple pay<br />o posto 6 e 7 se encontra em manutenção.|
|Como iniciar uma sessão de carregamento?|Para iniciar a recarga:<br />1. conecte o cabo ao veículo<br />2. selecione o carregador no aplicativo<br />3. confirme a autenticação<br />4. aguarde o início da transferência de energia|
|Existe fila de espera para o carregador rápido?|Sim, atualmente tem dois usuários na fila para utilizar o carregador rápido 6 e 7 , o tempo médio estimado para seu uso é de XX minutos.|
|O carregador não reconheceu meu veículo, o que eu faço?|Verifique:<br />- compatibilidade do conector<br />- encaixe correto do cabo<br />- status da bateria do veículo<br /><br />Caso o problema continue,<br />o suporte técnico poderá abrir um chamado automaticamente.|
|Meu pagamento foi feito mas o carregador não funciona?|Primeiro verifique se o pagamento foi realmente realizado , <br />verifique se o seu carro foi conectado perfeitamente ou se o <br />posto se encontra em funcionamento<br /><br />Caso o problema continue,<br />entre em contato com o suporte técnico para ser atendido.|

Definição do Modelo: 

1. Tipo de modelo: Comercial
2. Interação: Usuário
3. Modelo utilizado: gemini-3.1-flash-lite