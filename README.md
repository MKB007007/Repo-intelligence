# GitHub Intelligence Analyzer

A Python-based command-line tool that analyzes GitHub repositories and extracts meaningful contributor insights using the GitHub REST API.

## Features

* Fetch repository metadata
* Fetch contributor data
* Handle GitHub API pagination
* Calculate total contributions
* Calculate contributor contribution percentages
* Calculate Top Contributor Share
* Calculate Top 5 Contributor Share

## Example Output

```text
Repository Name: vscode
Repository Owner: microsoft

Total Contributions: 110284

Top Contributor Share: 11.59%
Top 5 Contributor Share: 46.34%
```

## Installation

```bash
pip install requests
```

## Usage

```bash
python main.py
```

Then enter:

```text
owner/repository
```

Example:

```text
microsoft/vscode
```

## Technologies Used

* Python
* Requests
* GitHub REST API

## Roadmap

* [x] Repository metadata analysis
* [x] Contributor analysis
* [x] Pagination support
* [x] Top contributor share
* [x] Top 5 contributor share
* [ ] Bus factor estimation
* [ ] Contributor concentration analysis
* [ ] Activity trend analysis
* [ ] Issue health analysis
* [ ] Insight generation

## Motivation

GitHub provides large amounts of repository data, but many useful insights remain hidden. This project aims to transform raw repository information into actionable engineering metrics that help understand contributor concentration, project risk, and repository health.
