def create_github_repo(repo_name, description='', private=False):
    import requests
    import os

    # Load GitHub App credentials from environment variables
    GITHUB_APP_ID = os.getenv('GITHUB_APP_ID')
    GITHUB_APP_PRIVATE_KEY = os.getenv('GITHUB_APP_PRIVATE_KEY')
    INSTALLATION_ID = os.getenv('INSTALLATION_ID')

    # Generate a JWT token for authentication
    def generate_jwt():
        from datetime import datetime, timedelta
        import jwt

        now = datetime.utcnow()
        payload = {
            'iat': now,
            'exp': now + timedelta(minutes=10),
            'iss': GITHUB_APP_ID
        }
        return jwt.encode(payload, GITHUB_APP_PRIVATE_KEY, algorithm='RS256')

    # Create a new repository
    def create_repo():
        url = f'https://api.github.com/app/installations/{INSTALLATION_ID}/repositories'
        headers = {
            'Authorization': f'Bearer {generate_jwt()}',
            'Accept': 'application/vnd.github.v3+json'
        }
        data = {
            'name': repo_name,
            'description': description,
            'private': private
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()

    return create_repo()

def create_repository(name, description, private=True):
    if not name:
        raise ValueError("Repository name cannot be empty.")
    
    # Simulate a GitHub API response for repository creation
    return {
        "name": name,
        "description": description,
        "private": private
    }