resource "aws_dynamodb_table" "user_profiles" {
  name           = "cp-onboarding-user-profiles" # Prefixing as per guidelines
  billing_mode   = "PAY_PER_REQUEST"             # Using on-demand billing for simplicity
  hash_key       = "UserID"

  attribute {
    name = "UserID"
    type = "S" # String type for the UserID
  }

  attribute {
    name = "Username"
    type = "S" # Assuming Username might be used as a GSI for querying
  }

  # Global Secondary Index for Username to ensure uniqueness and allow querying
  global_secondary_index {
    name               = "UsernameIndex"
    hash_key           = "Username"
    projection_type    = "ALL"
  }

  tags = {
    "lt:owning-team" = "content-platform"
  }
}
