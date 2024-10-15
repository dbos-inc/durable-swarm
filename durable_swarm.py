from swarm import Swarm, Agent
from typing import List
from swarm import Swarm, Agent
from dbos import DBOS, DBOSConfiguredInstance
from swarm.types import AgentFunction, ChatCompletionMessage, ChatCompletionMessageToolCall, Response

@DBOS.dbos_class()
class DurableSwarm(Swarm, DBOSConfiguredInstance):
    def __init__(self, client=None):
        Swarm.__init__(self, client)
        DBOSConfiguredInstance.__init__(self, "openai-client")
    
    @DBOS.step()
    def get_chat_completion(
        self,
        agent: Agent,
        history: List,
        context_variables: dict,
        model_override: str,
        stream: bool,
        debug: bool,
    ) -> ChatCompletionMessage:
        return super().get_chat_completion(agent, history, context_variables, model_override, stream, debug)

    @DBOS.step()
    def handle_tool_calls(
        self,
        tool_calls: List[ChatCompletionMessageToolCall],
        functions: List[AgentFunction],
        context_variables: dict,
        debug: bool,
    ) -> Response:
        return super().handle_tool_calls(tool_calls, functions, context_variables, debug)
    
    @DBOS.workflow()
    def run(
        self,
        agent: Agent,
        messages: List,
        context_variables: dict = {},
        model_override: str = None,
        stream: bool = False,
        debug: bool = False,
        max_turns: int = float("inf"),
        execute_tools: bool = True,
    ) -> Response:
        return super().run(agent, messages, context_variables, model_override, stream, debug, max_turns, execute_tools)
