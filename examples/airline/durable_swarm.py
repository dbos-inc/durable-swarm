from swarm import Swarm
from dbos import DBOS, DBOSConfiguredInstance
from swarm.repl.repl import process_and_print_streaming_response, pretty_print_messages

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

#####################################
# Util function to run the CLI loop, modified for Durable Swarm
# Original code: https://github.com/openai/swarm/blob/main/swarm/repl/repl.py
#####################################

def run_demo_loop(
    starting_agent, context_variables=None, stream=False, debug=False
) -> None:
    if stream:
        # If streaming, we need to use the non-durable client
        client = Swarm()
        print("Streaming not supported with Durable Swarm, using regular Swarm CLI 🐝")
    else:
        client = DurableSwarm()
        print("Starting Durable Swarm CLI 💪🐝")

    messages = []
    agent = starting_agent

    while True:
        user_input = input("\033[90mUser\033[0m: ")
        messages.append({"role": "user", "content": user_input})

        response = client.run(
            agent=agent,
            messages=messages,
            context_variables=context_variables or {},
            stream=stream,
            debug=debug,
        )

        if stream:
            response = process_and_print_streaming_response(response)
        else:
            pretty_print_messages(response.messages)

        messages.extend(response.messages)
        agent = response.agent
