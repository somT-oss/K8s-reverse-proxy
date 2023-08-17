# K8s-Reverse proxy

I focus on building a reverse proxy for a Flask server in a Kubernetes Cluster.


## Architecture

In this cluster, a Flask server is deployed and is exposed with a Service object in the cluster.

A Reverse proxy server too is deployed. This proxy reverse server points to the already deployed Flask server and is exposed by a Service object as well.

When a request is made to the Reverse proxy, it forwards the request to the Flask server and returns the response to the Reverse proxy back to the client.
