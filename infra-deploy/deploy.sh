# #!/bin/bash

helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx

helm repo update

helm install quickstart ingress-nginx/ingress-nginx

helm upgrade --install trino trino/trino -f trino/values.yaml