# Blue-green deployment

Blue-green deployment is a strategy where two environments, blue and green, are utilized for application deployment.

* Blue environment represents the live production environment, while green environment serves as an idle state.
* During a new deployment, traffic is switched from blue to green, allowing testing and validation.
* If the green environment performs well, the blue environment is decommissioned; otherwise, rollback is performed.
Source: [Implement blue-green deployment](https://learn.microsoft.com/en-us/training/modules/implement-blue-green-deployment-feature-toggles/2-what-blue-green-deployment)
