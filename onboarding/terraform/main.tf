provider "aws" {
  region  = "us-east-1"
  profile = "AdministratorAccess-588736812464"
}

data "archive_file" "add_user_profile" {
  type        = "zip"
  source_file = "${path.module}/../lambda_functions/add_user_profile.py"
  output_path = "${path.module}/../deployment/add_user_profile_deploy.zip"
}

data "archive_file" "get_user_profile" {
  type        = "zip"
  source_file = "${path.module}/../lambda_functions/get_user_profile.py"
  output_path = "${path.module}/../deployment/get_user_profile_deploy.zip"
}
