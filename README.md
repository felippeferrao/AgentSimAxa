# AXA Agent Sim

An insurance workflow demonstration built on AgentSim and CrewAI. Configure agents and teams, grant tools and skills, attach Markdown knowledge through Brain, and follow each delegation in Watch & run. Motor Coach demonstrates simulated vehicle pricing and quote PDFs.

## Run locally

Run `./start.sh` and open [the local workspace](http://127.0.0.1:8080/). For loopback access, leave `AGENTSIM_PUBLIC_URL` blank. The dashboard, agent profiles and saved configurations are available with the AI provider unconfigured.

The planned AXA deployment uses **Secure GPT**. The [Secure GPT integration guide](KnowledgeBase/SECURE_GPT_INTEGRATION.md) describes the required API contract, application changes and acceptance checks. This checkout still contains the previous OpenAI adapter. Keep `OPENAI_API_KEY` unset for AXA use until Secure GPT is integrated.

SQLite and generated artifacts are created at runtime. Use [the Docker deployment guide](deploy/README.md) for a protected HTTPS installation. For integration details see [KnowledgeBase](KnowledgeBase/README.md).

Run the automated tests with `.venv/bin/python -m unittest discover -s tests`.

## Attribution

AXA Agent Sim is an adaptation by Felippe da Silva Ferrão of WABIX AgentSim. Created in 2026 by Felippe da Silva Ferrão - felippeferrao@wabix.net. Powered By Wabix.

Visual reference and logo source are [AXA Belgium e‑Auto](https://www.fo.axa.be/eauto/). AXA branding belongs to its respective owner. The automotive photographs are generated examples. The portal is a demonstration workspace and its quote outputs are simulated.
