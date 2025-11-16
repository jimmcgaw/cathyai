# Chatty Cathy.AI

I am a software engineer who is currently focused on securing AI systems, via MLSecOps.

This repo contains a simple chatbot application that serves as a playground for testing various AI & LLM security tools.

I'm also using this to test out new models on Hugging Face that have specific text classification purposes, like checking if
a text input is a question or not.

## What's in Here

I'm using FastAPI Python package as the framework for creating endpoints, which I haven't used before.

Usually, in "hello world" apps, too many things are handled at the application level, like rate limiting and auth token validation.
I've used nginx in the past, but I'm toying around with using Kong Gateway as a sidecar, to handle these things.

Authorization is via Google accounts. JWT tokens are signed and verified using RS256 public-private keypair.

Redis is used as the backend to track rate-limiting, handled on a per-auth token basis.

Some LLM security things I'm doing (or plan to do) in here (including but not limited to):

* Sanitize the prompt through a data transform, guard classifier, backtranslation, etc. (See: <a target="_blank" href="https://arxiv.org/abs/2410.15236">Jailbreaking and Mitigation of Vulnerabilities in Large Language Models</a>)
* Scan model files for vulnerabilities, using the `modelscan` package.
* Check model output before returning, against a series of text classifier models.
* Build model pipelines to automate deployment and security check steps
* Set up model testing in a staging environment, feeding the model known testing prompts.