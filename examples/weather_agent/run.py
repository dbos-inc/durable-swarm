from durable_swarm import run_demo_loop
from agents import weather_agent

if __name__ == "__main__":
    # Note: stream=False because DurableSwarm does not support streaming yet.
    run_demo_loop(weather_agent, stream=False)
