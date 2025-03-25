# 🤖 Secretaria Inteligente no WhatsApp (via IA)

Este projeto é uma aplicação real de Inteligência Artificial com automação no WhatsApp. Ele simula uma **secretária virtual inteligente**, ideal para profissionais autônomos como médicos, dentistas, optometristas, terapeutas e outros que precisam organizar consultas, enviar mensagens automáticas e reduzir faltas — **sem depender de servidores pagos**.

---

## 🚀 Funcionalidades da Secretaria Inteligente

✅ Atendimento automático via WhatsApp  
✅ Armazena dados em planilha (Google Sheets)  
✅ Envia mensagens de confirmação via **WhatsApp e SMS**  
✅ Cancela agendamentos automaticamente se o paciente não confirma  
✅ Integração futura com **Google Agenda**

---

## 🧰 Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/) — Criação da API em Python  
- [Ngrok](https://ngrok.com/) — Geração de link público para testes  
- [Google Sheets API](https://developers.google.com/sheets/api) — Registro de agendamentos  
- [UltraMsg](https://ultramsg.com/) — Envio e recebimento de mensagens no WhatsApp  
- [Twilio](https://www.twilio.com/) — Envio de SMS (futuramente)  
- Hospedagem gratuita usando [AWS Free Tier (t2.micro)](https://aws.amazon.com/free/)

---

## 📌 Como Funciona

1. O cliente envia uma mensagem no WhatsApp com solicitação de consulta  
2. A IA entende a mensagem, responde automaticamente e registra os dados em uma planilha  
3. O sistema envia uma **mensagem de confirmação automática** (WhatsApp ou SMS)  
4. Se o cliente **não confirmar** até X horas antes da consulta, ela é cancelada  
5. Agenda sincronizada (em desenvolvimento)

---

## 🧠 Modelo de IA

Utilizamos um modelo de linguagem (GPT-2 inicialmente) com memória contextual.  
Nosso objetivo é migrar futuramente para modelos mais avançados ou personalizados.

---

## 📁 Estrutura do Projeto

```
secretaria-inteligente/
├── app/
│   ├── main.py         # Código principal com FastAPI
│   ├── sheets.py       # Integração com Google Sheets
│   └── whatsapp.py     # Conexão com UltraMsg (WhatsApp)
├── requirements.txt    # Bibliotecas necessárias
├── README.md
└── .env                # Variáveis de ambiente (tokens, senhas)
```

---

## 🔐 Segurança

- As chaves de API (UltraMsg, Google Sheets, Twilio) são armazenadas em `.env`
- Recomendado uso de variáveis de ambiente também na AWS

---

## 💬 Exemplo de Conversa

```
Paciente: Oi, queria marcar consulta
Bot: Olá! Qual é o melhor dia e horário para você?
Paciente: Quarta de manhã
Bot: Perfeito! Vamos registrar aqui. Você receberá uma mensagem de confirmação em breve.
```

---

## 📈 Diferenciais da Solução

✨ Funciona sem servidor pago (Google Colab ou AWS Free Tier)  
✨ Fácil de personalizar por profissional  
✨ Simples de testar com Insomnia ou Postman  
✨ Pronto para expandir com funcionalidades como lista de espera, reagendamento e muito mais!

---

## 🎯 Público-Alvo

- Médicos e clínicas
- Dentistas
- Optometristas
- Psicólogos
- Qualquer profissional que agende atendimentos

---

## 📌 Status

🟢 **Em desenvolvimento ativo**  
🎯 Versão 1: Atendimento + Armazenamento + Mensagens automáticas  
🔜 Versão 2: Integração com Google Agenda + Histórico + Aprendizado

---

## 🧑‍💻 Autor

**Rodrigo Ribeiro Carvalho**  
Corretor de imóveis e Analista de Dados em transição para IA aplicada no dia a dia  
📍 João Pessoa – PB  
[GitHub: Rodrigo-RRC](https://github.com/Rodrigo-RRC)  
[LinkedIn: rodrigo-ribeiro-datascience](https://www.linkedin.com/in/rodrigo-ribeiro-datascience)  
[WhatsApp](https://wa.me/5547991820339)

---

## 📸 Demonstrações (futuras)

Em breve: vídeos e imagens do agente funcionando no WhatsApp, conversando, agendando, enviando mensagens automáticas e respondendo em tempo real.

---

## 🧩 Personalizações Futuras

✅ Agendamento por horário fixo  
✅ Respostas automáticas com imagens (ex: mapa da clínica)  
✅ Diferentes tipos de secretária para cada especialidade  
✅ Dashboard com painel dos agendamentos

---

## 🔗 Clonagem e Execução

```bash
git clone https://github.com/Rodrigo-RRC/secretaria-inteligente.git
cd secretaria-inteligente
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 📞 Vamos Conversar?

Se quiser transformar sua ideia em um robô funcional que responde via WhatsApp, envia lembretes, confirma agendamentos e muito mais — **entre em contato!**

