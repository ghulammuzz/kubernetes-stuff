- If u want default install (without adjust values)
```shell
helm install prometheus prometheus-community/kube-prometheus-stack -f values.yaml --namespace monitoring
```
- grab values
```shell
helm show values prometheus-community/kube-prometheus-stack > values.yaml
```

- Modify node-exporter port (if faced prometheus conflict port 9100 )
```yaml
prometheus-node-exporter:
  ...
  service:
    port: 9101
```

- Modify grafana annotation
```yaml
grafana:
    ...
    ingress:
        ...
        annotations: 
            cert-manager.io/cluster-issuer: "letsencrypt-prod"
            spec.ingressClassName: traefik
```

- Apply Helm chart
```shell
helm install prometheus prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  -f values.yaml
```

- eat :v