from dbos import DBOS
from swarm import Agent
import time

def process_refund(context_variables, item_id, reason="NOT SPECIFIED"):
    """Refund an item. Refund an item. Make sure you have the item_id of the form item_... Ask for user confirmation before processing the refund."""
    user_name = context_variables.get("user_name", "user")
    print(f"\033[33mRefunding for {user_name}, item {item_id}, because {reason}...\033[0m")
    for i in range(1, 6):
        refund_step(i)
    print("Refund successfully processed!")
    return "Success!"

@DBOS.step()
def refund_step(step_id):
    time.sleep(1)
    print(f"Processing refund step {step_id}... Press Control + C to quit")

@DBOS.step()
def apply_discount():
    """Apply a discount to the user's cart."""
    print("Applying discount...")
    return "Applied discount of 11%"

refunds_agent = Agent(
    name="Refunds Agent",
    instructions="Help the user with a refund. If the reason is that it was too expensive, offer the user a refund code. If they insist, then process the refund.",
    functions=[process_refund, apply_discount],
)
