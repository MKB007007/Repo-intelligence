# GitHub Intelligence Analyzer

A Python-based command-line tool that analyzes GitHub repositories using the GitHub REST API and provides engineering insights about contributor distribution and development activity.

## Features

### Repository Information

* Repository metadata
* Owner
* Primary language
* Creation date
* Last updated date

### Contributor Analysis

* Total repository contributions
* Individual contributor statistics
* Contribution percentage for each contributor
* Top contributor share
* Top 5 contributors share

### Contributor Concentration Analysis

* Estimates contributor concentration using contribution distribution
* Calculates the number of contributors required to reach 80% of total contributions
* Classifies contributor distribution into meaningful engineering categories
* Generates human-readable insights

### Activity Analysis

* Latest commit information
* Latest commit author
* Commits in the last 30 days
* Commits in the previous 90 days
* Commit rate (commits/day)
* Activity trend detection
* Automatically identifies:

  * Accelerating development
  * Stable development
  * Declining activity
  * Revived projects
  * Dormant repositories

### Authentication

* GitHub Personal Access Token (PAT) authentication
* Secure credential management using `.env`
* Increased GitHub API rate limit

### Error Handling

* Invalid repository detection
* Invalid GitHub token detection
* GitHub API rate-limit detection

## Technologies Used

* Python
* GitHub REST API
* Requests
* python-dotenv

## Setup

1. Clone the repository.

2. Install dependencies.

```bash
pip install requests python-dotenv
```

3. Create a `.env` file.

```text
GITHUB_TOKEN=your_personal_access_token
```

4. Run the program.

```bash
python main.py
```

5. Enter the repository in the following format.

```text
owner/repository
```

Example:

```text
microsoft/vscode
```

## Future Improvements

* Issue Health Analysis
* Overall Repository Health Score
* Better performance using GitHub API filtering (`since` parameter)
* Modular project structure
* Data visualization
* Export reports to CSV/PDF
