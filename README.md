# GitHub Repository Creator

This project provides
a GitHub Actions workflow that utilizes Python to create repositories using GitHub Apps. It allows users to automate the process of repository creation directly from their GitHub account.

## Project Structure

```
github-repo-creator
├── .github
│   └── workflows
│       └── create_repo.yml
├── src
│   ├── create_repo.py
│   ├── config.py
│   └── utils.py
├── tests
│   ├── __init__.py
│   └── test_create_repo.py
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/github-repo-creator.git
   cd github-repo-creator
   ```

2. **Install Dependencies**
   Make sure you have Python installed, then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
   Copy the `.env.example` file to `.env` and fill in the necessary environment variables, such as your GitHub App credentials.

4. **Using the GitHub Actions Workflow**
   The workflow defined in `.github/workflows/create_repo.yml` will trigger on specific events (e.g., push, pull request). Ensure that your GitHub App has the necessary permissions to create repositories.

5. **Running Tests**
   To ensure everything is working correctly, run the tests located in the `tests` directory:
   ```bash
   pytest
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
