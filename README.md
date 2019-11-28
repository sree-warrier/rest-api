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

### Infra Deployment

      Building the infra using terraform commands, following steps will walk you through the process:

1. Clone the repo:

      git clone `https://github.com/sree-warrier/rest-api.git`

2. Following should be created before terraform file execution:

    - Create a keypair
    - Update key pair under respective locations of main.tf
    - Configure aws credentials, update the access and secret keys in variable.tf
    - Update the local public IP in the 'jump-ssh' and 'app-elb-sg' sec-grp section

3. infra-tf directory conatins the terraform file for infra setup, use the following steps:

      ```
      cd infra-tf
      terraform init
      terraform plan
      terraform apply
      ```

### App Deployment

1. Login to the instance using the key-pair

2. Create DB schema

      ```
      create table posts (id int NOT NULL AUTO_INCREMENT UNIQUE, text varchar(255) NOT NULL, date_posted varchar(255) NOT NULL);
      ```

2. Create docker-compose.yml file:

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

   Update the DB environment variables which are prompted during the terraform execution

3. Run docker using the docker-compose file (docker components are installed using the user-data in terraform file)

      docker-compose up

4. Public facing ELB created, use the ELB endpoint for accessing the app.

      UI : http://elb-endpoint:8080

5. API's

  * POST new message

    Messages are posted via UI http://elb-endpoint:8080 , which are stored to the mysql DB.

  * GET all message

    Retrived all messages from the DB using the api URL /api/message

      ```
      curl request - curl -X GET http://elb-endpoint:8080/api/message
      UI - http://elb-endpoint:8080/api/message
      ```

  * GET a specific message

    Retrived a specific message from the DB using the api URL /api/message/msg_id

      ```
      curl request - curl -X GET http://elb-endpoint:8080/api/message/msg_id
      UI - http://elb-endpoint:8080/api/message/msg_id
      ```

  * DELETE a specific message

    Delete a specific message from the DB using the api URL /api/message/msg_id

      ```
      curl request - curl -X DELETE http://elb-endpoint:8080/api/message/msg_id
      ```

## Credits

* Flask DB queries https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/
