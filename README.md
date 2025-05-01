# DMARC External DNS Record Generator 🛡️

This tool helps you identify and generate the DNS TXT records needed to authorize external domains to receive DMARC aggregate (`rua`) and forensic (`ruf`) reports on your behalf.

It is especially useful when you're using third-party DMARC monitoring services, and your DMARC record includes reporting addresses outside your main domain.

## 🌐 Live App

Try it here: [https://your-app-name.streamlit.app](https://your-app-name.streamlit.app)  
*(replace with your actual Streamlit URL)*

## ✨ Features

- Parses your DMARC record and extracts `rua`/`ruf` destinations
- Ignores trusted DMARC processors like **dmarcian**
- Identifies external domains requiring authorization
- Generates the exact DNS TXT records to publish on external domains

## 🛠️ Usage

1. Enter your **sending domain** (e.g. `example.com`)
2. Paste your **DMARC record** (e.g. `v=DMARC1; p=none; rua=mailto:dmarc@example.net`)
3. The tool will output one or more DNS TXT records like:

