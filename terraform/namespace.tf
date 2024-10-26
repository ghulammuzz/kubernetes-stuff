resource "kubernetes_namespace" "muzz" {
  metadata {
    name = "muzz"
  }
}