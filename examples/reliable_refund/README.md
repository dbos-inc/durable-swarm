# Durable Refund Agent

This example uses Durable Swarm to orchestrate a refund agent.
It takes in a user's name, processes a refund for that user, then applies a discount.

The function for processing refunds takes a long time!
However, thanks to **durable execution**, even if the agent is interrupted during refund processing (or at any other time), upon restart it automatically recovers, finishes processing the refund, then proceeds to the next step in its workflow.

![Durable Swarm Demo](../../assets/demo.gif)


## Try it out!

To run the demo:

```shell
python3 run.py
```

You can press `Ctrl+C` at any point while the agent is processing your refund.
If you restart the program again, you'll see DBOS automatically recovers the incomplete workflow and resumes it from its last completed step.

For example:

```shell
> python3 main.py

Connecting to Durable Refund Agent 💪🐝
What's your name: Max
[mock] Refunding for Max, item item_99, because Too expensive and I don't like its color...
[mock] Processing refund step 1... Press Control + C to quit
[mock] Processing refund step 2... Press Control + C to quit
[mock] Processing refund step 3... Press Control + C to quit
^C⏎

# Resume from where the last completed step (step 3), continuing with step 4.
> python3 main.py

Connecting to Durable Refund Agent 💪🐝
[mock] Refunding for Max, item item_99, because Too expensive and I don't like its color...
[mock] Processing refund step 4... Press Control + C to quit
[mock] Processing refund step 5... Press Control + C to quit
[mock] Refund successfully processed!
[mock] Applying discount...
Refunds Agent:
process_refund("item_id"= "item_99", "reason"= "Too expensive and I don't like its color")
apply_discount()
Refunds Agent: I've processed the refund for item 99 and also applied a discount of 11% for your next purchase. If there's anything else you need, feel free to ask!

```
