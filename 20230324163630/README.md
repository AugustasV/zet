# Kubernetes taint and tolereance

Taint is used to put some kind of label to node, so resources who has the same label could be created on that node
command used `k taint node arm01 this=label:NoSchedule`
To remove label add - sign at the end `k taint node arm01 this=label:NoSchedule-`

Source: [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration)
