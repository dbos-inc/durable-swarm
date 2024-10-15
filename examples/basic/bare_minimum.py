from swarm import Agent
from durable_swarm import DurableSwarm

client = DurableSwarm()

agent = Agent(
    name="Agent",
    instructions="You are a helpful agent.",
)

messages = [{"role": "user", "content": "Hi!"}]
response = client.run(agent=agent, messages=messages)

print(response.messages[-1]["content"])
