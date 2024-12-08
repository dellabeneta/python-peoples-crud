terraform {
  backend "s3" {
    bucket         = "terraformstates.dellabeneta.tech"
    key            = "peoples.dellabeneta.tech/terraform.tfstate"
    region         = "sa-east-1"
    encrypt        = true
    dynamodb_table = "terraformstates-lock"
  }
}