resource "digitalocean_database_cluster" "postgres" {
  name       = "python-peoples-crud-postgres"
  engine     = "pg"
  version    = "15"
  size       = "db-s-1vcpu-1gb"
  region     = "nyc3"
  node_count = 1
}