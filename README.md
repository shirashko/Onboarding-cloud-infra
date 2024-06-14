# onboarding-cloud-infra

This project is designed to set up the infrastructure for a serverless application using AWS services including Lambda functions, API Gateway, and DynamoDB.

<table>
  <tr>
    <td><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJemIicUKQjp5Cvw0T2Pgp_NbJBLSq5Ij63Q&s" width="300"/></td>
    <td><img src="https://www.rogerperkin.co.uk/wp-content/uploads/2021/02/terraform-logo.png" width="300"/></td>
  </tr>
</table>

## Description

`onboarding-cloud-infra` provides the necessary Terraform configurations to provision an AWS environment capable of handling user profile creation and retrieval through REST API endpoints.

## Features

- AWS Lambda functions for adding and getting user profiles.
- An Amazon DynamoDB table to store user profiles.
- API Gateway to expose the Lambda functions as HTTP endpoints.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Terraform v0.14+.
- You have an AWS account with the necessary permissions to create the resources described in the Terraform configurations.
- You have configured your AWS credentials locally or have the necessary environment variables set.

## Installation

To install `onboarding-cloud-infra`, follow these steps:

1. Clone the repository to your local machine: git clone git@github.com:shirrashko/onboarding-cloud-infra.git

2. Navigate to the Terraform directory: cd onboarding-cloud-infra/terraform

3. Initialize Terraform: terraform init


## Usage

To deploy the infrastructure, run the following command from the Terraform directory: terraform apply

Make sure to review the plan before applying. Once applied, your infrastructure will be set up on AWS.

## Development

To work on the project, you can make changes to the Terraform configuration files or the Lambda function code located in the `lambda_functions` directory. After making changes, re-run `terraform apply` to update the infrastructure.

## Testing

This project contains a test suite for the Lambda functions. To run the tests, navigate to the `tests` directory and execute: pytest
