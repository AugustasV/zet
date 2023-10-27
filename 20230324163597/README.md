# 🗣️ Cluster Traffic with Service Mesh and Native Network Policies

* **K8s Network Policy**: Kubernetes Network Policies play a critical role in securing network traffic within a cluster. However, they have limitations when it comes to certain aspects of network security.

* **Limitations of K8s Network Policy**:
  * **No Internal Cluster Traffic Manipulation**: Kubernetes Network Policies are not designed for manipulating internal cluster traffic; they primarily focus on controlling it.

  * **No Possibility to Select a Particular Node**: Network Policies do not provide the ability to select specific nodes for network policy enforcement; they operate at the pod level.

  * **Cannot Target Services by Name, Only Pods**: Network Policies target pods based on labels and selectors, making it essential to consider pods, not services, in policy enforcement.

  * **Logging Security Policy Blocks**: Network Policies do not inherently provide traffic logging; additional solutions are required to log which security policies block traffic.

* **How Linkerd Works**:
  * **Control Plane for TLS Certs**: Linkerd, a service mesh solution, manages secure communication within a Kubernetes cluster. Its control plane is responsible for handling TLS certificates and encryption for secure traffic.

  * **Annotations for Linkerd Integration**: To incorporate Linkerd into Kubernetes, you need to add annotations like `linkerd.io/inject: enable` to your deployments and pods. This indicates that Linkerd should be injected into the resources for secure communication.

  * **Enhancing Kubernetes Security**: For a more comprehensive approach to securing Kubernetes internal cluster traffic, it is advisable to combine native Network Policies with service mesh solutions like Linkerd. This combination provides robust network security and communication management.

* **Source**: [InfoShare Dev Agenda - Securing Kubernetes Internal Cluster Traffic](https://dev.infoshare.pl/agenda/#talk57-10)

