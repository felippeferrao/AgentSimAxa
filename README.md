# AXA Agent Sim

An insurance workflow demonstration built on AgentSim and CrewAI. Configure agents and teams, grant tools and skills, attach Markdown knowledge through Brain, and follow each delegation in Watch & run. Motor Coach demonstrates simulated vehicle pricing and quote PDFs.

## Run locally

1. Copy `.env.example` to `.env`. Set `OPENAI_API_KEY` to a key from your OpenAI API project. For local loopback use, leave `AGENTSIM_PUBLIC_URL` blank.
2. Run `./start.sh` and open [the local workspace](http://127.0.0.1:8080/).
3. Open **Connection** to check access. In **Agents → Profile → Model & settings**, select an available Responses-compatible model. Optionally set `OPENAI_MODEL` before first launch to seed models for the starter profiles.
4. For the Motor Coach demo, open **Brain** and install the example with an available model. Then open **Watch & run → Motor Coach**.

The same server key powers model discovery, Responses, web research, and image generation. Set `OPENAI_IMAGE_MODEL` to change the Images API model. Restart the application after changing `.env`. The browser receives connection status and model names. The API key is server-side.

SQLite and generated artifacts are created at runtime. Use [the Docker deployment guide](deploy/README.md) for a protected HTTPS installation. For integration details see [KnowledgeBase](KnowledgeBase/README.md).

Run the automated tests with `.venv/bin/python -m unittest discover -s tests`.

## Attribution

AXA Agent Sim is an adaptation by Felippe da Silva Ferrão of WABIX AgentSim. Created in 2026 by Felippe da Silva Ferrão - felippeferrao@wabix.net. Powered By Wabix.

Visual reference and logo source are [AXA Belgium e‑Auto](https://www.fo.axa.be/eauto/). AXA branding belongs to its respective owner. The automotive photographs are generated examples. The portal is a demonstration workspace and its quote outputs are simulated.
