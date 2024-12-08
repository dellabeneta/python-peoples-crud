resource "digitalocean_ssh_key" "ssh_key" {
  name       = "python-peoples-crud-ssh-key"
  public_key = file("~/.ssh/id_ed25519.pub")
}