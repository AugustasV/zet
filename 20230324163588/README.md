# 🗣️ How Vinted uses GitOps to deploy thousands of pods to Kubernetes

* GitOps is  a DeOps process characterized by nbest practicies of deployment, managment, monitoring, fully automated pipelines
* Using git revision ctonrol system to track and approve changes to the infrastructure
* Open source backstage tool
* Gitops CI: build -> test -> Docker push -> git cone config repo -> update manifests -> git commit and push
* Only short lived git branches
* Telefonistka and Kargo, nice UI.
* ArgoCD sync waves
* GitOps good to have directories with monorepo. Different directory mean different namespace

Source: [How Vinted uses GitOps to deploy thousands of pods to Kubernetes](https://www.meetup.com/dataops-poland/events/296212282)
