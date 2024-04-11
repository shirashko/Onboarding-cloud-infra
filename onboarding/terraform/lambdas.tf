resource "aws_lambda_function" "add_user_profile" {
  filename      = data.archive_file.add_user_profile.output_path
  function_name = "add_user_profile"
  role          = aws_iam_role.lambda_exec.arn
  handler       = "add_user_profile.add_user_profile"

  runtime       = "python3.8"
  source_code_hash = filebase64sha256(data.archive_file.add_user_profile.output_path)

  environment {
    variables = {
      STAGE = "dev"
    }
  }
}

resource "aws_lambda_function" "get_user_profile" {
  filename      = data.archive_file.get_user_profile.output_path
  function_name = "get_user_profile"
  role          = aws_iam_role.lambda_exec.arn
  handler       = "get_user_profile.get_user_profile"
  runtime       = "python3.8"
  source_code_hash = filebase64sha256(data.archive_file.get_user_profile.output_path)

  environment {
    variables = {
      STAGE = "dev"
    }
  }
}


resource "aws_iam_role" "lambda_exec" {
  name = "custom_lambda_exec_role"

  assume_role_policy = jsonencode({
    Version   = "2012-10-17",
    Statement = [{
      Action   = "sts:AssumeRole",
      Effect   = "Allow",
      Principal = {
        Service = "lambda.amazonaws.com"
      },
    }],
  })
}

# Add the necessary permissions for Lambda functions to log to CloudWatch
resource "aws_iam_policy_attachment" "lambda_logs" {
  name       = "lambda_logs"
  roles      = [aws_iam_role.lambda_exec.name]
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}


resource "aws_iam_policy" "lambda_dynamodb_access" {
  name        = "cp-onboarding-lambda-dynamodb-access"
  description = "IAM policy for Lambda functions to access DynamoDB"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect   = "Allow",
        Action   = [
          "dynamodb:GetItem",
          "dynamodb:PutItem",
          "dynamodb:Query",
          "dynamodb:UpdateItem",
          "dynamodb:DeleteItem"
        ],
        Resource = "${aws_dynamodb_table.user_profiles.arn}"
      },
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_dynamodb_access_attachment" {
  role       = aws_iam_role.lambda_exec.name
  policy_arn = aws_iam_policy.lambda_dynamodb_access.arn
}
