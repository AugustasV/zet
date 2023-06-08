# Exposing Services in Kubernetes

**ClusterIP (internal):**
- Default service type in Kubernetes.
- Only accessible within the cluster.
- Used for communication between different parts of an application within the cluster.

**NodePort:**
- Exposes the service on a specific port on each node.
- Allows external access to the service using the node's IP address and the specified port.
- Useful for accessing services from outside the cluster during development or testing.

**LoadBalancer:**
- Creates an external load balancer in the cloud provider's infrastructure.
- Distributes incoming external traffic to the service.
- Typically used to expose a service to the internet or handle high traffic loads.

In short, ClusterIP is for internal cluster communication, NodePort allows external access using each node's IP by spcifying port of app, and LoadBalancer creates an external load balancer for handling external traffic.

Source: [Orchestrating the Cloud with Kubernetes GCP Lab](https://www.cloudskillsboost.google/focuses/557?parent=catalog)
