import signal
import sys

from dbos import DBOS, DBOSConfiguredInstance, SetWorkflowID
from swarm import Swarm
from swarm.repl.repl import pretty_print_messages
from agents import refunds_agent

DBOS()

@DBOS.dbos_class()
class DurableSwarm(Swarm, DBOSConfiguredInstance):
    def __init__(self, client=None):
        Swarm.__init__(self, client)
        DBOSConfiguredInstance.__init__(self, "openai_client")

    @DBOS.step()
    def get_chat_completion(self, *args, **kwargs):
        return super().get_chat_completion(*args, **kwargs)

    @DBOS.workflow()
    def run(self, *args, **kwargs):
        response = super().run(*args, **kwargs)
        pretty_print_messages(response.messages)
        return response

DBOS.launch()

def main():
    client = DurableSwarm()
    print("Connecting to Durable Refund Agent 💪🐝")

    user_name = input("\033[90mWhat's your name\033[0m: \n")
    if user_name.strip() == "":
        return  # Exit if user doesn't provide a name

    query = "I want to refund item 99 because it's too expensive and I don't like its color! I want to proceed with the refund and also get a discount for my next purchase!"
    context_variables = {"user_name": user_name}

    # SetWorkflowID is used to ensure that user is refunded exactly once.
    with SetWorkflowID(user_name):
        client.run(
            agent=refunds_agent,
            messages=[{"role": "user", "content": query}],
            context_variables=context_variables,
        )

signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))  # Exit gracefully on Ctrl+C

if __name__ == "__main__":
    main()
