## Service mesh 

* There is service mesh layer, every service send request to service mesh layer, and service mesh redirects where it's needed.
* One of key things is telemetry. 
* Traffic routes, rerouting requests and how long it took to reach destination.
* Istio add Proxy container (sidecar). Proxy is needed to run service mesh logic in every pod (microservice).
* Those proxies in Istio are called "Data Plane".
* There should be no changes for containers only on service plane level.
* It gives service additional metrics about throttling, requests. Good to know kubernetes metrics.
* To monitor services from one container to another
