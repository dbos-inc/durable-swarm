# Durable Swarm basic

This folder contains basic examples from the original [Swarm repo](https://github.com/openai/swarm/tree/main/examples/basic).
These examples show how to enhance Swarm with DBOS to be **durable** ([`durable_swarm.py`](./durable_swarm.py)), and how to use `DurableSwarm` as a drop-in replacement for `Swarm`.

### Examples

1. **agent_handoff.py**

   - Demonstrates how to transfer a conversation from one agent to another.
   - **Usage**: Transfers Spanish-speaking users from an English agent to a Spanish agent.

2. **bare_minimum.py**

   - A bare minimum example showing the basic setup of an agent.
   - **Usage**: Sets up an agent that responds to a simple user message.

3. **context_variables.py**

   - Shows how to use context variables within an agent.
   - **Usage**: Uses context variables to greet a user by name and print account details.

4. **function_calling.py**

   - Demonstrates how to define and call functions from an agent.
   - **Usage**: Sets up an agent that can respond with weather information for a given location.

5. **simple_loop_no_helpers.py**
   - An example of a simple interaction loop without using helper functions.
   - **Usage**: Sets up a loop where the user can continuously interact with the agent, printing the conversation.

## Running the Examples

To run any of the examples, use the following command:

```shell
python3 <example_name>.py
```
