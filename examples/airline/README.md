# Airline customer service

This example demonstrates a multi-agent setup for handling different customer service requests in an airline context using the Swarm framework. The agents can triage requests, handle flight modifications, cancellations, and lost baggage cases.

This example uses the helper function `run_demo_loop`, which allows us to create an interactive Swarm session.

In this example, we enhance Swarm with DBOS to be **durable**, using [`durable_swarm.py`](./durable_swarm.py) as a drop-in replacement for `Swarm`.


## Agents

1. **Triage Agent**: Determines the type of request and transfers to the appropriate agent.
2. **Flight Modification Agent**: Handles requests related to flight modifications, further triaging them into:
   - **Flight Cancel Agent**: Manages flight cancellation requests.
   - **Flight Change Agent**: Manages flight change requests.
3. **Lost Baggage Agent**: Handles lost baggage inquiries.

## Setup

Once you have installed dependencies and Swarm, run the example using:

```shell
python3 main.py
```
