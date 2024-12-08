output "droplet_ip" {
    value = digitalocean_droplet.droplet.ipv4_address  
}

output "postgres_private_uri" {
  value = digitalocean_database_cluster.postgres.private_uri
  sensitive = true
}
