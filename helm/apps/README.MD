### step by step apply helm package

- Make sure `helm` installed properly
- add `helm` repo 
    ```
    helm repo add apps https://ghulammuzz.github.io/kubernetes-stuff/helm/apps/charts
    ```
- update repo cache
    ```
    helm repo update

    ```
- find chart
    ```
    helm search repo apps/backend-app-stack 
    ```
- apply chart with my `values.yaml`
    ```
    helm install my-backend-release apps/backend-app-stack --namespace flexmaster -f values.yaml
    ```