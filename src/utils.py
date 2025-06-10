def format_error_message(error):
    return f"Error: {str(error)}"

def log_message(message):
    print(f"[LOG] {message}")

def validate_repo_name(repo_name):
    if not repo_name or len(repo_name) < 1 or len(repo_name) > 100:
        raise ValueError("Repository name must be between 1 and 100 characters.")