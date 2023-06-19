# Monitoring Alerts

Here is the provided text converted into markdown format:

- Alerts that trigger call-out should be **urgent**, **important**, **actionable**, and **real**. They should represent either ongoing or imminent problems with your service.
- Err on the side of removing noisy alerts – **over-monitoring** is a more challenging problem to solve than **under-monitoring**.
- Classify the problem into the following categories: 
    - **Availability & Basic Functionality**
    - **Latency**
    - **Correctness** (completeness, freshness, and durability of data)
    - **Feature-Specific Problems**
- Use **symptoms** to capture problems more comprehensively and robustly with less effort.
- Include **cause-based information** in symptom-based pages or on dashboards, but avoid alerting directly on causes.
- The further up your serving stack you go, the more distinct problems you catch in a single rule. However, ensure that you can sufficiently distinguish what is going on.
- If you want an on-call rotation, it's imperative to have a system for dealing with things that need a timely response but aren't imminently critical.

Source: [Reduce meaningless and non-actionable alerts](https://learn.microsoft.com/en-us/training/modules/manage-alerts-blameless-retrospectives-just-culture/7-reduce-meaningless-non-actionable-alerts)
