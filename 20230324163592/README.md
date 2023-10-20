# K8GB - A cloud native Kubernetes Global Balancer

- K8GB is a cloud-native global load balancing solution for Kubernetes clusters that focuses on load balancing traffic across geographically dispersed clusters.
- Unlike traditional DNS-based load balancing, K8GB incorporates Kubernetes native application health checks, making it more robust and reliable.
- K8GB uses the status of Liveness and Readiness probes for load balancing decisions, ensuring that its load balancing is based on the availability of Kubernetes Pods.
- K8GB can be installed in a Kubernetes cluster and provide independent GSLB capability to any Ingress or Service in the cluster without the need for handoffs and coordination between dedicated network teams.
- K8GB is a suitable alternative to traditional DNS-based load balancers in Kubernetes environments.
- K8GB provides features such as load balancing, failover, and intelligent routing, making it a powerful tool for managing global Kubernetes deployments.
- In some cases it could be used instead of cloud provider load balancer

Source: [K8gb](https://www.k8gb.io/docs/)
