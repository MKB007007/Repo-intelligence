# Challenges Faced & Solutions

## 1. GitHub API Pagination

**Problem:** The GitHub API returns only 30 contributors/commits per request by default, resulting in incomplete analysis for large repositories.

**Solution:** Implemented page-wise traversal, continuously fetching subsequent pages until an empty response was returned, ensuring all contributors and commits were analyzed.

---

## 2. Excessive API Requests

**Problem:** The initial implementation performed redundant API requests, making contributor analysis inefficient.

**Solution:** Refactored the logic to reuse previously fetched contributor data, significantly reducing the total number of API requests.

---

## 3. GitHub API Rate Limiting

**Problem:** Unauthenticated requests quickly exceeded GitHub's limit of 60 requests per hour.

**Solution:** Integrated GitHub Personal Access Token (PAT) authentication, increasing the request limit to 5000 requests per hour.

---

## 4. Secure Credential Management

**Problem:** Hardcoding API tokens would expose sensitive credentials if the project was shared publicly.

**Solution:** Stored the token in a `.env` file, loaded it using `python-dotenv`, and excluded it from version control through `.gitignore`.

---

## 5. Contributor Concentration Metric

**Problem:** A simple Bus Factor approximation based on contribution percentages produced misleading results for repositories with many occasional contributors.

**Solution:** Replaced the heuristic with a Contributor Concentration Analysis based on Top Contributor Share, Top 5 Contributor Share, and the number of contributors required to reach 80% of total contributions.

---

## 6. Repository Activity Analysis

**Problem:** Raw commit counts did not accurately represent whether repository activity was increasing or decreasing over time.

**Solution:** Compared commit frequency during the last 30 days against the previous 90 days, producing more meaningful activity trend classifications.

---

## 7. Activity Trend Classification Bug

**Problem:** Repositories with zero commits during the previous 90-day period were incorrectly classified because of division-by-zero logic.

**Solution:** Added explicit handling for repositories with no historical activity, introducing **Dormant** and **Revived** classifications.



