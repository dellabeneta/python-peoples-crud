resource "digitalocean_vpc" "vpc" {
  name     = "python-peoples-crud-vpc"
  region   = "nyc3"
  ip_range = "10.10.10.0/24"
}