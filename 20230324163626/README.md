# Kubernetes resources quotas

  - For optimization on a K8s cluster, selecting resource quotas is essential.
  - Resource Quotas restrict resource usage per namespace, including CPU, memory, and other objects.
  - Create a ResourceQuota object to set memory and CPU quotas.
  - Limit memory requests, memory limits, CPU requests, and CPU limits for pods[2].
  - Pod quotas restrict the total number of pods in a namespace.
  - Control pod creation to optimize resources and prevent overloading[4].
  - Resource quotas are crucial in shared environments to prevent resource contention.
  - They ensure fair resource allocation among different tenants for cluster stability[3].

- **Best Practices**
  - Define quotas based on actual resource needs.
  - Monitor resource usage regularly and adjust quotas for optimal performance.

Sources:
[Resource Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/)
[Quota memory cpu namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/)
[Quota pod namespac](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/quota-pod-namespace/)
