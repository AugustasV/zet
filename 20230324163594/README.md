# Building Self-Provisioned Runtimes with Serverless Java on AWS
## Workshop

* Lambda Gateway: A pivotal component in AWS's serverless ecosystem, Lambda functions enable cost-effective execution of code in response to events. The pay-as-you-go pricing model makes them highly efficient, especially for sporadically used workloads.
* ALB: While Lambda functions offer cost-efficiency, ALB provides a fixed-cost solution for distributing incoming application traffic across multiple targets. This predictability is valuable when managing workloads with consistent traffic patterns.
* REST API Gateway: When building serverless applications, the REST API Gateway simplifies integration into existing API networks. Its compatibility with RESTful interfaces makes it a natural choice for developers familiar with HTTP.
* HTTP API Gateway: In contrast, the HTTP API Gateway shines when the goal is to make serverless applications publicly accessible in the cloud. It streamlines the process of exposing your services to the world, ensuring seamless scalability and high availability.
* Control Plane: It's important to note that the architecture and infrastructure of the control plane vary significantly between AWS and Azure. AWS and Azure have their unique paradigms and services for managing the control plane of your applications, and understanding these differences is crucial for making informed architectural decisions.

Source: [InfoShare Dev Workshop](https://dev.infoshare.pl/warsztaty/#agenda_34)
