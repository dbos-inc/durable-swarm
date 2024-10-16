# Durable Swarm: Durable Multi-Agent Orchestration

This repo contains tutorials on how to make [OpenAI Swarm](https://github.com/openai/swarm/tree/main) **durable** with 6 lines of DBOS code in Python, and how to use it to as a drop-in replacement for Swarm to build reliable applications.

> [!NOTE]
> DurableSwarm currently doesn't support streaming

## Install Dependencies

Install [Swarm](https://github.com/openai/swarm/tree/main) and [DBOS](https://github.com/dbos-inc/dbos-transact-py). Requires Python 3.10+
```
pip install -r requirements.txt
```

## Make Swarm Durable!

You can make Swarm durable by simply overriding the original class and add DBOS decorators.
Create a `durable_swarm.py` file:

```python
from swarm import Swarm
from dbos import DBOS, DBOSConfiguredInstance

DBOS()

@DBOS.dbos_class()
class DurableSwarm(Swarm, DBOSConfiguredInstance):
    def __init__(self, client=None):
        Swarm.__init__(self, client)
        DBOSConfiguredInstance.__init__(self, "openai_client")

    @DBOS.step()
    def get_chat_completion(self, *args, **kwargs):
        return super().get_chat_completion(*args, **kwargs)

    @DBOS.step()
    def handle_tool_calls(self, *args, **kwargs):
        return super().handle_tool_calls(*args, **kwargs)

    @DBOS.workflow()
    def run(self, *args, **kwargs):
        return super().run(*args, **kwargs)

DBOS.launch()
```

Under the hood, `@DBOS.workflow()` starts a reliable workflow composed of steps (functions decorated with `@DBOS.step()`).
DBOS persists the input of a workflow and the outputs of its steps in a Postgres database.
Therefore, if your workflow is ever interrupted, DBOS can correctly resume it from the last completed step!

Now, you can use `DurableSwarm` as a drop-in replacement for `Swarm`.

## Usage

Create `main.py` and put this script in the same folder as `durable_swarm.py`:

```python
from swarm import Agent
from durable_swarm import DurableSwarm

client = DurableSwarm()

def transfer_to_agent_b():
    return agent_b


agent_a = Agent(
    name="Agent A",
    instructions="You are a helpful agent.",
    functions=[transfer_to_agent_b],
)

agent_b = Agent(
    name="Agent B",
    instructions="Only speak in Haikus.",
)

response = client.run(
    agent=agent_a,
    messages=[{"role": "user", "content": "I want to talk to agent B."}],
)

print(response.messages[-1]["content"])
```

Then, create a DBOS config file:
```
dbos init --config
```

If you already have a Postgres server, you can modify `dbos-config.yaml` to config the connection info.
Otherwise, you could start one locally:
```
python3 start_postgres_docker.py
```

Finally, run this script:
```
> python3 main.py

Agent B is here,
Ready to help you today,
What do you need, friend?
```

## Overview

DBOS is a lightweight durable execution library. All you need is a Postgres database.

## Examples

Updating your existing Swarm apps to use DurableSwarm is simple:
1. Add the `durable_swarm.py` file
2. Change your app to use `DurableSwarm` instead
3. Run `dbos init --config` in your app folder

Learn more about each example in its README. Durable Swarm supports all original examples, plus a modified agent to demonstrate durable workflows.

- [`basic`](examples/basic/): Simple examples of fundamentals like setup, function calling, handoffs, and context variables
- [`triage_agent`](examples/triage_agent/): Simple example of setting up a basic triage step to hand off to the right agent
- [`weather_agent`](examples/weather_agent/): Simple example of function calling
- [`airline`](examples/airline/): A multi-agent setup for handling different customer service requests in an airline context.
- [`support_bot`](examples/support_bot/): A customer service bot which includes a user interface agent and a help center agent with several tools
- [`personal_shopper`](#): ~~A personal shopping agent that can help with making sales and refunding orders~~ (the original demo is broken)