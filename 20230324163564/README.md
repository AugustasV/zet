# Istio deployment approach, virtual services

Istio, a service mesh solution, has made a decision not to use an operator for managing its deployments due to potential security threats that could arise from injections into deployments. Istio relies on mutual TLS (mTLS) for secure communication between its proxies. Within Istio, virtual services serve as virtual representations of services, allowing fine-grained control over traffic routing and other network-related features. To ensure smoother integration, it is important to avoid overcomplication and focus on maintaining simplicity and small test scopes.

- Istio avoids using an operator in deployments to mitigate potential security threats from injections.
- Mutual TLS (mTLS) is used for secure communication between Istio proxies.
- Virtual services in Istio are virtual representations of services within the service mesh.
- Virtual services enable precise control over traffic routing and other network-related features.
- It is crucial to maintain simplicity and avoid overcomplication during Istio deployments.
- Keeping test scopes small facilitates integration, reduces risks, and supports effective testing.

Source: [SERVICE MESH WORKSHOP: CREATE, MANAGE, AND TEST A JAVA SERVICE MESH WITH ISTIO](https://devopscon.io/microservices-software-architecture/service-mesh-workshop-create-manage-and-test-a-java-service-mesh-with-istio/)
