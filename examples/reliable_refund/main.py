import sys
import signal

from agents import refunds_agent
from durable_swarm import DurableSwarm
from dbos import SetWorkflowID

client = DurableSwarm()

def main():
    print("Connecting to Durable Refund Agent 💪🐝")

    user_name = input("\033[90mWhat's your name\033[0m: ")
    if user_name.strip() == "":
        return  # Exit if user doesn't provide a name

    query = "I want to refund item 99 because it's too expensive and I don't like its color! I want to proceed with the refund and also get a discount for my next purchase!"
    context_variables = {"user_name": user_name}

    # SetWorkflowID is used to ensure that user is refunded exactly once.
    # If a workflow was interrupted and restarted, then it'll resume from where it left off.
    with SetWorkflowID(user_name):
        client.run(
            agent=refunds_agent,
            messages=[{"role": "user", "content": query}],
            context_variables=context_variables,
        )

signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))  # Exit gracefully on Ctrl+C

if __name__ == "__main__":
    main()
