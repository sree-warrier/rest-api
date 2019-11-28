variable "access_key" {
	default = ""
}
variable "secret_key" {
	default = ""
}
variable "region" {
    default = ""
}
variable "rds_name" {
  description = "Name of RDS database"
}

variable "rds_user" {
  description = "Name of RDS user"
}

variable "rds_password" {
  description = "RDS Password"
}

variable "rds_port" {
  description = "RDS port"
  default = 3306
}