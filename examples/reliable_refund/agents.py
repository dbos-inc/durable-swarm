from swarm import Agent
from dbos import DBOS

def process_refund(context_variables, item_id, reason="NOT SPECIFIED"):
    """Refund an item. Refund an item. Make sure you have the item_id of the form item_... Ask for user confirmation before processing the refund."""
    user_name = context_variables.get("user_name", "user")
    print(f"[mock] Refunding for {user_name}, item {item_id}, because {reason}...")
    for i in range(1, 6):
        refund_step(i)
        DBOS.sleep(1)
    print("[mock] Refund successfully processed!")
    return "Success!"

@DBOS.step()
def refund_step(step_id):
    print(f"[mock] Processing refund step {step_id}... Press Control + C to quit")

@DBOS.step()
def apply_discount():
    """Apply a discount to the user's cart."""
    print("[mock] Applying discount...")
    return "Applied discount of 11%"

triage_agent = Agent(
    name="Triage Agent",
    instructions="Determine which agent is best suited to handle the user's request, and transfer the conversation to that agent.",
)

refunds_agent = Agent(
    name="Refunds Agent",
    instructions="Help the user with a refund. If the reason is that it was too expensive, offer the user a refund code. If they insist, then process the refund.",
    functions=[process_refund, apply_discount],
)


def transfer_back_to_triage():
    """Call this function if a user is asking about a topic that is not handled by the current agent."""
    return triage_agent

def transfer_to_refunds():
    """Transfer the user to the refunds agent."""
    return refunds_agent


triage_agent.functions = [transfer_to_refunds]
refunds_agent.functions.append(transfer_back_to_triage)
