- add repo
```sh
helm repo add jetstack https://charts.jetstack.io --force-update
```

- install cert-manager
```sh
helm install \
  cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --version v1.16.1 \
  --set crds.enabled=true
```

- uninstall cert-manager
```sh
helm uninstall cert-manager -n cert-manager
```
