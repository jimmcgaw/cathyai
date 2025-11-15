# Chatty Cathy.AI

I am a software engineer who is currently focused on securing AI systems, via MLSecOps.

This repo contains a simple chatbot application that serves as a playground for testing various AI & LLM security tools.

Some things I'm doing in here (initial list):

* Sanitize the prompt through a data transform, guard classifier, backtranslation, and others <a href="https://arxiv.org/abs/2410.15236">Jailbreaking and Mitigation of Vulnerabilities in Large Language Models</a>
* Scan model files for vulnerabilities
* Check model output before returning
* Build model pipelines to automate deployment and security check steps
* Set up model testing in a staging environment

Eventually I'll fine-tune a foundation model of my own, and deploy it onto hugging face with an SBOM detailing its supply chain.