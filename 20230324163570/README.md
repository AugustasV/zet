# 🗣️ Man vs Machine - Exploring the Benefits of a Cloud-Native Approach

**Design Rules:**
- **Scalability:** The application is designed to scale infinitely.
- **Resilience:** The application is built to handle sudden termination gracefully.
- **Dependency Flexibility:** The application is designed to coexist with other applications that might fail unpredictably.
- **Managed Services:** All components are stored within managed services.
- **Cost Efficiency:** Utilizing spot instances to reduce costs by 50-80%.

**RDS vs VMs:**
- **VM Update Scenario:**
  - Updating 60 VMs with MySQL took approximately 1 month, involving 3 engineers and causing partial downtime for 14 hours.
- **RDS Update Scenario:**
  - Updating 300 RDS instances took 1 day, required 2 engineers for PR review, and led to only 6 minutes and 50 seconds of partial downtime.
- Utilizing DB replication and GCP services resulted in significant savings.

**Secrets Management:**
- Secrets management is a crucial aspect of the architecture.

**Source:** [Virtual Exclusive Pro Talk - Man vs Machine: What’s the Real Gain of a Cloud-Native Approach](https://developerweekcloudx2023.sched.com/event/1PF9C/virtual-exclusive-pro-talk-man-vs-machine-whats-the-real-gain-of-a-cloud-native-approach)
