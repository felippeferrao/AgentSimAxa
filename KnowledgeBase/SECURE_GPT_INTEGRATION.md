# AXA Secure GPT integration

**Status.** This is the target integration for AXA Agent Sim. The AXA team will provide the internal API contract and provision access. The current checkout still contains the previous OpenAI adapter. Run the workspace with that adapter unconfigured until the Secure GPT integration is available. The AXA deployment must use Secure GPT and fail closed if it is unavailable.

## Information needed from AXA

| Area | Confirm with the Secure GPT team |
| --- | --- |
| Network | Approved environments and base URLs, network or gateway access, and trusted TLS certificate chain. |
| Identity | Service identity and authentication flow, required scopes, credential storage and renewal. Confirm whether the service uses a token, certificate, or another mechanism. |
| Models | Whether the service exposes model discovery or requires an approved model allowlist. Check model IDs, context size, supported options and rate limits. |
| Inference | Request and response schemas, streaming protocol, tool definitions and calls, returning a tool result by call ID, completion status, errors and usage counts. |
| Optional tools | Whether Secure GPT or a separate AXA-approved API supports image generation, reference-image editing, or web research. Confirm payload formats, limits and source citations where applicable. |
| Data handling | Which data classes may be sent, retention and audit requirements, and which fields are permitted in operational logs. |

## Application changes

1. **Server configuration and model availability.** Replace the current provider setup in [auth.py](../auth.py). Read the AXA-approved endpoint and credential configuration from the server environment or its secret store. Keep configuration names and authentication details aligned with the confirmed contract. Populate the agent profile model picker via `POST /api/models` in [server.py](../server.py) using an approved catalog or allowlist. Keep `GET /api/connection/status` and the Connection dialog in [static/app.js](../static/app.js) limited to readiness, safe status text and model metadata.
2. **Inference and delegation.** Replace [`runtime.ResponsesLLM.call()`](../runtime.py) with the Secure GPT adapter after reviewing the real contract. Map roles, inputs, model settings and tool schemas to the AXA request. Normalize replies into assistant text or structured calls with stable IDs and validated arguments. Return local tool results with the matching call ID. Preserve completion, failure and usage signals. Report missing usage as unavailable. If the AXA API is asynchronous or uses a different stream format, translate it at the adapter and keep the browser's existing execution-event contract.
3. **Tool permissions and optional APIs.** In [harness.py](../harness.py), map `ProviderTools.request()` and `ImageProvider.generate()` to approved services only when available. Disable unsupported provider tools and surface their status in the catalog before an agent runs. Preserve per-agent grants, artifact ownership checks and local PDF/chart generation. For image edits, send only authorized reference artifacts. For web research, return actual source references supported by the provider.
4. **Cutover.** Update [.env.example](../.env.example), [Compose](../compose.yaml), connection copy, deployment docs and the [architecture diagram source](../architecture/agentsim.architecture.json). Remove the direct OpenAI endpoint, OpenAI credentials and any OpenAI client path used by the app. Keep endpoint details and secrets out of the public repository. Workspace sign-in remains separate from the application service identity.

## Acceptance checks

- Start the UI with the provider unconfigured. Confirm runs fail closed, no credentials are sent to the browser, and there are no outbound calls to OpenAI.
- With an approved AXA test identity, verify model catalog, one agent response and a manager-to-worker delegation with a structured tool call and a matching result. Check Watch & run, execution history and artifact attribution.
- Exercise expired credentials, timeout, rate limit, rejected model, malformed tool arguments and interrupted streaming. Confirm safe error messages and no fallback to another provider.
- For each approved optional capability, run an end-to-end test and open the output. Verify unsupported capabilities are unavailable and local PDF and chart tools still work.
- Inspect outbound destinations and sample logs in the approved environment. Use credentials and test data provisioned by AXA and confirm request bodies, tokens and internal endpoints are absent from public artifacts.
