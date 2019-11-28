# rest-api

Deploy a dockerized Flask Application to AWS in a VPC using Terraform

Includes
--------

* VPC
* Internal DNS
* RDS
* EC2 instances
* ELB
* Security groups
* docker & docker-compose
* Docker Registry
* Python

Prerequisites
-------------

* Terraform should be installed. Get it from `https://www.terraform.io/downloads.html` to grab the latest version.
* An AWS account http://aws.amazon.com/

Usage
-----

Building the infra using terraform commands

The following steps will walk you through the process:

1. Clone the repo::

      git clone `https://github.com/sree-warrier/rest-api.git`

2. Following should be created before terraform file execution::

    - Create a keypair
    - Update key pair under respective locations of main.tf
    - Configure aws credentials, update the access and secret keys in variable.tf

3. infra-tf directory conatins the terraform file for infra setup, use the following steps::

      ```cd infra-tf
      terraform init
      terraform plan
      terraform apply```

4. Login to the cluster instance using the keys::

5. Create docker-compose.yml file::

    ```touch docker-compose.yml```

        version: '3.3'
        services:
          django-ha:
              image: sreewarrier24/rest-api:04
              environment:
                DB_NAME: *******
                DB_USER: *******
                DB_PASS: *******
                DB_SERVICE: *******
                DB_PORT: *******
              ports:
                  - "8000:8000"

   Update the environment variables which are prompted during the terraform execution

6. Run docker using the docker-compose file::

      docker-compose up

7. Use the ELB CNAME record to access via browser

## Credits

* Flask DB queries https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/
