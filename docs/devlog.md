## Challenges Faced & Solutions

### 1. GitHub API Pagination
**Problem:** Only the first 30 contributors/commits were returned by the API.

**Solution:** Implemented page-wise traversal until an empty response was received, ensuring all contributors and commits were analyzed.

---

### 2. Excessive API Requests
**Problem:** Initial contributor analysis required 2N API requests, making the program inefficient.

**Solution:** Refactored the logic to reuse fetched contributor data, reducing the complexity to N requests.

---

### 3. GitHub API Rate Limit
**Problem:** Anonymous API requests quickly exceeded GitHub's 60 requests/hour limit.

**Solution:** Integrated GitHub Personal Access Token (PAT) authentication, increasing the limit to 5000 requests/hour.

---

### 4. Secure Credential Management
**Problem:** Hardcoding API tokens would expose credentials if pushed to GitHub.

**Solution:** Stored the token in a `.env` file, loaded it using `python-dotenv`, and excluded it from version control via `.gitignore`.

---

### 5. Activity Metric Accuracy
**Problem:** A single recent commit could incorrectly classify an inactive repository as active.

**Solution:** Redesigned the metric to compare commit frequency over the last 30 days against the previous 90 days, producing meaningful activity trends.

---

### 6. Trend Classification Bug
**Problem:** Repositories with no commits in the previous 90 days were incorrectly marked as "Declining" due to division logic.

**Solution:** Added special handling for zero historical activity, introducing "Dormant" and "Revived" classifications.

---

### 7. Debugging Environment Variables
**Problem:** The application could not read the GitHub token, causing authentication to fail.

**Solution:** Identified an empty `.env` file and verified the working directory before successfully loading environment variables.
