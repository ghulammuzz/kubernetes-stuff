STEP 1  
- add cert-manager
- apply `cluster-issuer`
- apply `apps`
- apply `ingress` +
```yaml

metadata:
  name: INGRESS_NAME
  annotations:
    cert-manager.io/cluster-issuer: "$METADATA.NAME.CLUSTERISSUER"
    spec.ingressClassName: traefik

spec:
  tls:
    - hosts:
        - $SUB.$DOMAIN.com
      secretName: $SECRET
```