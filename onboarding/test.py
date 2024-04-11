import requests


def post_user_profile(lambda_url, user_data):
    """Make an HTTP POST request to the Lambda function URL."""
    try:
        response = requests.post(lambda_url, json=user_data)
        response.raise_for_status()  # This will raise an HTTPError for bad responses
        return response.json(), None
    except requests.HTTPError as http_err:
        return None, f"HTTP error occurred: {http_err} - {response.text}"
    except Exception as err:
        return None, f"Other error occurred: {err}"


def get_user_profile(lambda_get_url, user_id):
    """Make an HTTP GET request to the Lambda function URL."""
    query_params = {'UserID': user_id}
    try:
        response = requests.get(lambda_get_url, params=query_params)
        response.raise_for_status()
        return response.json(), None
    except requests.HTTPError as http_err:
        return None, f"HTTP error occurred: {http_err} - {response.text}"
    except Exception as err:
        return None, f"Other error occurred: {err}"


def main():
    post_lambda_url = "https://dwn5lgy7tpuzsb3an6bysf2bgy0oeotw.lambda-url.us-east-1.on.aws/"
    user_data = {
        "Username": "shirashko",
        "FullName": "Shir Rashkovits",
        "Bio": "This is a test bio",
        "ProfilePictureURL": "https://example.com/profile.jpg"
    }

    # POST user profile and attempt to extract UserID from the response
    post_result, post_error = post_user_profile(post_lambda_url, user_data)
    if post_error:
        print("POST Error:", post_error)
        return
    else:
        print("POST successful:", post_result)

    # Extracting the UserID from the POST response
    user_id = post_result.get('user_profile', {}).get('UserID')
    if not user_id:
        print("UserID not found in POST response")
        return

    print("-----")
    get_lambda_url = "https://dqkg2mzishx74kdmp7ua4urppu0rltum.lambda-url.us-east-1.on.aws/"

    # GET user profile using the extracted UserID
    get_result, get_error = get_user_profile(get_lambda_url, user_id)
    if get_error:
        print("GET Error:", get_error)
    else:
        print("GET successful:", get_result)


if __name__ == "__main__":
    main()
