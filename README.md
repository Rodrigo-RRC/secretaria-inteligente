---
title: Secretária Inteligente
description: Agente virtual com IA para agendamento de consultas via WhatsApp e SMS, com integração ao Google Sheets e Google Agenda.
---

# 🤖 Secretária Inteligente para Profissionais da Saúde

Este projeto apresenta uma **secretária virtual automatizada**, com **IA integrada ao WhatsApp**. Ela realiza agendamentos, envia mensagens automáticas e registra os dados do paciente — tudo sem depender de servidores pagos.

---

## 🚀 O que esta solução faz?

- **Conversa com pacientes** via WhatsApp (e futuramente por SMS)
- **Pergunta o melhor dia e horário** da consulta
- **Verifica a disponibilidade**
- **Oferece alternativas se não houver vaga**
- **Confirma a consulta**
- **Registra os dados em uma planilha (Google Sheets)**
- **Agenda automaticamente no Google Agenda**
- **Envia lembretes automáticos antes da consulta**
- **Cancela a consulta automaticamente caso o paciente não confirme**

---

## ⚙️ Tecnologias Utilizadas

- **FastAPI** – para criar a API
- **ngrok** – para disponibilizar a API local na web
- **Python** – lógica do agente
- **Google Sheets + Google Agenda API** – armazenamento e agendamento
- **UltraMsg (WhatsApp API)** – integração com o WhatsApp *(em desenvolvimento)*
- **AWS EC2 (T2.micro)** – hospedagem gratuita por 12 meses

---

## 🧠 Exemplo de Conversa

```text
Paciente: Oi, queria marcar consulta
Bot: Olá! Qual é o melhor dia e horário para você?
Paciente: Quarta de manhã às 9h
Bot: Um momento! Irei verificar a disponibilidade...

# Se estiver disponível
Bot: Perfeito! Consulta marcada para quarta-feira às 9h. Você receberá uma mensagem de confirmação.

# Se NÃO estiver disponível
Bot: Infelizmente esse horário está ocupado. Para quarta-feira tenho: 10h, 11h ou 14h.
Bot: Nenhum desses horários serve para você? Posso verificar outro dia também.

# Se o paciente recusar todos os horários
Bot: Tudo bem. Qual outro dia e horário seria melhor para você?
# Bot continua procurando até encontrar o horário mais próximo que atenda.

# Após confirmação
Bot: Ótimo! Você receberá um lembrete por WhatsApp e SMS.
```

---

## ☁️ Fluxo do Projeto

```mermaid
graph TD
A[Usuário envia mensagem] --> B[API FastAPI recebe via UltraMsg]
B --> C[Lógica do Agente em Python]
C --> D[Consulta à planilha Google Sheets]
D --> E[Confirmação de horário]
E --> F[Agendamento na Google Agenda]
F --> G[Resposta via WhatsApp]
F --> H[Disparo de SMS com lembrete]
```

---

## ✅ Status Atual

- [x] Projeto iniciado
- [x] API FastAPI funcionando na AWS (porta 8000)
- [ ] Integração com UltraMsg *(em andamento)*
- [ ] Roteiro de conversa implementado *(em progresso)*
- [ ] Integração com planilhas do Google *(próximo passo)*
- [ ] Integração com Google Agenda
- [ ] Envio de lembrete por SMS

---

## 📁 Estrutura do Projeto

```
📦 secretaria-inteligente
🔗 main.py                    # FastAPI principal
🔗 agente.py                 # (em breve) Lógica do agente
🔗 agenda.py                 # (em breve) Integração com Google APIs
🔗 requirements.txt
🔗 .env                      # Informações sensíveis (não versionar)
```

---

## 🔧 Como Executar Localmente

```bash
# 1. Criar ambiente virtual (opcional, mas recomendado)
python3 -m venv venv
source venv/bin/activate

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Executar o servidor FastAPI
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## ⏭️ Próximas Etapas

- Criar as rotas para interação com o paciente
- Integrar UltraMsg para recebimento e envio via WhatsApp
- Conectar à planilha do Google para armazenar os dados
- Sincronizar com o Google Agenda
- Adicionar envio automático de lembrete por SMS
- Implementar roteiros personalizados para dentistas, nutricionistas etc.

---

## 👨‍💼 Autor

**Rodrigo Ribeiro Carvalho**  
GitHub: [Rodrigo-RRC](https://github.com/Rodrigo-RRC)  
LinkedIn: [linkedin.com/in/rodrigo-ribeiro-datascience](https://linkedin.com/in/rodrigo-ribeiro-datascience)  
WhatsApp: [Clique aqui para conversar](https://wa.me/5547991820339)

---

## ✅ Licença

Este projeto é de uso livre e educacional. A comercialização só é permitida com autorização expressa do autor.
