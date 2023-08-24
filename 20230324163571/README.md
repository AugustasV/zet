# 🗣️ Observability-Driven Development with OpenTelemetry
**Challenges with Microservices:**
- Tracking and monitoring microservices can be complex and challenging.
- **Observability-Driven Development (ODD):** Focuses on distributed tracing to enhance understanding and monitoring.

**Distributed Tracing:**
- **Definition:** Method of tracking requests as they move through distributed systems.
- Helps understand the flow of requests and responses in complex architectures.

**Pain Points of Traditional Testing (TDD):**
- Integration tests often require access to various services and infrastructure.
- Need to propagate environments and monitor message queues.
- Difficult to trace failures within a chain of microservices.
- A significant portion (90%) of code written to make tests work, only 10% for actual testing.

**Observability-Driven Development (ODD):**
- Testing involves real data and traces from actual environments.
- Leverages OpenTelemetry, an open-source tool for collecting trace data.
- "tracetest" tool, compatible with any system using OpenTelemetry.
- ODD does not use mocks; it tests against real data to understand actual system behavior.
- Provides insights into the functioning of each microservice.

**Source:** [Virtual Exclusive Pro Talk - Observability-Driven Development with OpenTelemetry](https://developerweekcloudx2023.sched.com/event/1PF8V/virtual-exclusive-pro-talk-observability-driven-development-with-opentelemetry)
