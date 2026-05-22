## Describe how DLP policy decisions work together

A data loss prevention (DLP) policy is not a blanket rule for every data problem. It is a targeted decision that answers a specific question: what should happen when a user tries to move sensitive data in a risky way?

That framing matters because it keeps the policy focused. If you start with the intent, you can make better choices about detection, scope, and enforcement instead of building a policy that is too broad to use well.

## Define the intent first

Every DLP policy should start with the risk you want to reduce. You might want to stop accidental sharing, provide user guidance, or block the most sensitive actions outright. Each goal leads to a different policy shape.

When the intent is clear, the rest of the design becomes easier. You know what signal matters, which users or locations matter, and how strict the response should be.

That is the first test of a good policy: it should be easy to explain in one sentence. If it is not, the scope is probably too wide.

## Match the policy to real work

The same data can create different risk depending on the action around it. A document shared with a trusted team is not the same as the same document sent outside the organization. DLP works best when it recognizes that difference.

That is why scope matters. If the policy covers too much, it starts blocking normal work. When that happens, people look for ways around it, and the policy becomes less effective.

A better approach is to align the policy with the workflow people actually use. That keeps the protection visible without making every task feel like a hurdle.

## Choose the right response

Once the policy knows what to look for, it still needs a response. Some policies only alert or inform users. Others limit actions. The strictest policies block the risky move completely.

The best choice depends on the risk and the confidence you have in the detection rule. If you are still validating the policy, start with visibility. If the scenario is clear and high risk, use enforcement.

| Response type | Best when |
| --- | --- |
| Alert or inform | You want visibility without interrupting work. |
| Limit actions | You want to reduce risk while keeping the workflow moving. |
| Block | The action is clearly risky and should not proceed. |

This sequence helps you avoid over-enforcement. You begin with intent, narrow the scope, and then choose the response that matches the real risk.

Now the policy has a job, a boundary, and a response. That makes it easier to maintain and easier for users to understand.
