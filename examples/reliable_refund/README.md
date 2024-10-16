# Reliable Refund Agent

This example is a Durable Swarm containing a refund agent, which takes in user name, processes a refund, and then apply a discount.

What's unique about this example is that each refund is processed exactly once, so even if you crash the application, it can always resume from the last step and proceed to completion.


## Try it out!

To run the triage agent Durable Swarm:

```shell
python3 run.py
```

You can press `Ctrl+C` at any point while the agent is processing your refund.
If you restart the program again, you'll see DBOS automatically recovers the incomplete workflow and resumes from the last step.