# Desafio - Estacionamento
> Um parque temático precisa de ajuda quanto um software para gestão do seu estacionamento.

1. O estacionamento possui um total de 80 vagas;

2. O preço cobrado na entrada é fixo e dá direito a ficar enquanto o parque estiver aberto. Caso o veículo saia do pátio, é necessário pagar novamente. O estacionamento não tem tolerância, entrou, pagou.

3. Deste total de 80 vagas:
- 20 vagas são exclusivas de motos e custam R$5;
- 30 vagas são reservadas a carros R$15;
- 20 vagas são reservadas a caminhonetes, vans abaixo de 15 lugares, micro-ônibus ou pequenos caminhões, e custam 20 reais;
- 10 vagas são reservadas a ônibus de até 40 passageiros e caminhões grandes e custam 50 reais.

4. Todas as vagas são numeradas
- As vagas de 1 a 20 são destinadas as motos;
- As vagas de 21 a 50 são destinadas a carros;
- As vagas de 51 a 70 são destinadas a caminhonetes, vans, micros e pequenos caminhões etc;
- As vagas de 71 as 80 são destinadas aos ônibus e caminhões grandes.

5. O software é aberto no início do dia e fechado ao termino do expediente
- Imediatamente o sistema indica quantas vagas existem para cada veículo e a soma de dinheiro no caixa. (lembrando que o dia inicia com o caixa em 0 e as vagas todas livres.

6. O atendente de estacionamento, assim que o veículo se aproxima da cancela ele informa o tipo ao sistema (1 para motos, 2 para carros, 3 para classe de camionetes e vans e etc, 4 para ônibus e caminhões grandes.

7. Após a entrada deste dado, o sistema retorna:
- Qual o número da vaga que este veículo deve estacionar, se houver vaga.
- Se a capacidade estiver esgotada, deve emitir um alerta informado sobre a falta de vagas. Neste caso o estacionamento não é cobrado

8. Se houver a vaga, o sistema deve registrar o pagamento pelo estacionamento, deve mostrar: quantas vagas disponíveis por tipo, quantos veículos por tipo entraram no estacionamento durante o dia e a soma de dinheiro no caixa.

9. Quando o veículo sair,  o motorista deve informar ao atendente de qual vaga ele está saindo. O sistema libera a vaga.

10. o sistema novamente carrega as informações: quantas vagas disponíveis por tipo, quantos veículos por tipo entraram no estacionamento durante o dia e a soma de dinheiro no caixa.

11. As vagas sempre terão o status livre/ocupada
