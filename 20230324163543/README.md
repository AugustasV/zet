# Creating and Managing Cloud Resources Challenge on GCP

I recently completed a challenging lab that tested my ability to manage a cloud environment on Google Cloud Platform (GCP). The lab required me to perform several tasks without step-by-step guidance. Due to time constraints, I used CLI commands to speed up the process. Here's a summary of what I accomplished:

1. **Creating an Instance:** I successfully created an instance using an instance template provided by GCP.

2. **Setting up a 3-Node Kubernetes Cluster:** I created a Kubernetes cluster with three nodes and deployed a simple service on it.

3. **Configuring an HTTP(s) Load Balancer:** To ensure high availability and distribute traffic efficiently, I set up an HTTP(s) load balancer. This load balancer evenly distributed incoming requests across two web servers.

To achieve this, I completed the following steps:

- **Instance Template:** I defined the configuration for the instances in the cluster by creating an instance template.
- **Target Pool:** I created a target pool to distribute traffic among the instances in the cluster.
- **Firewall Rule:** I set up a firewall rule to allow incoming traffic to reach the load balancer.
- **Health Check:** I created a health check to monitor the instances' health and ensure they could handle requests.
- **Instance Groups:** I organized the instances into instance groups for easier management and scalability.
- **URL Map:** I configured a URL map to direct incoming requests to the appropriate backend services.
- **Target Proxy:** Finally, I created a target proxy to handle incoming traffic and distribute it to the instances in the target pool.

Overall, this lab challenged me to demonstrate my ability to create and manage cloud resources on GCP. I successfully completed the tasks by using CLI commands and configuring the necessary components.

Source: [Create and Manage Cloud Resources](https://www.cloudskillsboost.google/quests/120)
