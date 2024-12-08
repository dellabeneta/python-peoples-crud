resource "digitalocean_droplet" "droplet" {
  image   = "ubuntu-24-04-x64"
  name    = "python-peoples-crud-droplet"
  region  = "nyc3"
  size    = "s-2vcpu-2gb"
  backups = true
  ssh_keys = [ digitalocean_ssh_key.ssh_key.fingerprint ]
}