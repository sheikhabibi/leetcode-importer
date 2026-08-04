# LeetCode CSV Importer 🚀

A Python automation tool that imports LeetCode problems from CSV datasets into LeetCode Collections automatically.

Instead of manually opening hundreds of LeetCode problems and adding them one by one, this tool:

- Reads problem lists from GitHub CSV files
- Creates LeetCode Collections automatically
- Adds problems using LeetCode GraphQL API
- Tracks progress and resumes interrupted imports
- Supports multiple companies/lists

---

# ✨ Features

## 📂 Import from any CSV source

The tool can read LeetCode problem lists from GitHub CSV files.

Example sources:

- Company-wise problem lists
- Custom problem lists
- Personal CSV datasets

---

## 📋 Automatic Collection Creation

If the requested LeetCode Collection does not exist, the tool creates it automatically.

Example:

```bash
python main.py --list TCS --csv https://raw.githubusercontent.com/snehasishroy/leetcode-companywise-interview-questions/refs/heads/master/tcs/all.csv
```

If `TCS` collection does not exist:

```
Create TCS Collection
        |
        ↓
Import questions
```

---

## 🔄 Resume Support

Large imports can be interrupted safely.

Progress is stored separately:

```
progress_TCS.json
progress_Amazon.json
progress_Google.json
```

If the program stops:

```
Importing TCS: 120/300
```

Running it again continues from where it stopped.

---

## 📊 Progress Display

Uses a progress bar while importing:

```
Importing TCS:
██████████████████░░░░ 75%
```

---

# 🛠 Installation

## Requirements

- Python 3.10+
- Brave Browser / Chromium based browser
- A logged-in LeetCode account

---

## 1. Clone the repository

```bash
git clone https://github.com/sheikhabibi/leetcode-importer

cd leetcode-importer
```

---

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Install Playwright browsers

```bash
playwright install
```

---

# 🔐 Authentication Setup

This project uses your existing browser session instead of storing your LeetCode password.

The tool connects to an already-open Brave browser using Chrome Remote Debugging.

This avoids:

- CAPTCHA issues
- Cloudflare login blocks
- storing passwords/session tokens in code

---

# 🌐 Start Brave with Remote Debugging

Close all Brave windows first.

Open PowerShell:

```powershell
"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" --remote-debugging-port=9222
```

A Brave window will open.

---

# 🔑 Login to LeetCode

Open:

```
https://leetcode.com
```

Login normally.

Make sure:

- You can access your profile
- Collections are visible
- You are not on a login page

---

# 🔌 Verify Browser Connection

Open:

```
http://localhost:9222/json/version
```

You should see something like:

```json
{
 "Browser": "Chrome/...",
 "webSocketDebuggerUrl": "ws://localhost:9222/..."
}
```

This means Playwright can connect to your browser.

---

# ▶️ Usage

Run:

```bash
python main.py --list <collection_name> --csv <csv_url>
```

Example:

```bash
python main.py \
--list TCS \
--csv https://raw.githubusercontent.com/example/problems.csv
```

---

# 📄 Getting a GitHub CSV URL

GitHub normally gives a webpage URL:

```
https://github.com/user/repository/blob/main/problems.csv
```

The program needs the raw file URL:

```
https://raw.githubusercontent.com/user/repository/main/problems.csv
```

To get it:

1. Open the CSV file on GitHub
2. Click **Raw**
3. Copy the URL
4. Use that URL with `--csv`

---

# 📁 Project Structure

```
leetcode-importer/

│
├── main.py          # Main CLI program
├── leetcode.py      # Browser connection and cookies
├── graphql.py       # LeetCode GraphQL operations
├── queries.py       # GraphQL queries/mutations
├── github_csv.py    # CSV parser
├── progress.py      # Resume tracking
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ How It Works

The workflow:

```
GitHub CSV
     |
     ↓
CSV Parser
     |
     ↓
Question Slugs
     |
     ↓
LeetCode GraphQL API
     |
     ↓
LeetCode Collection
```

The program:

1. Reads question names/slugs
2. Finds or creates the requested Collection
3. Adds questions one by one
4. Saves completed questions
5. Continues safely after interruptions

---

# 🐛 Troubleshooting

## "Question already in list"

This means the problem was already added.

The importer skips it safely.

---

## Browser connection failed

Make sure Brave was started with:

```powershell
--remote-debugging-port=9222
```

and:

```
http://localhost:9222/json/version
```

opens successfully.

---

## Cloudflare login problems

Do not login through Playwright.

Instead:

1. Open Brave normally with debugging enabled
2. Login manually
3. Let Playwright attach to the existing session

---

# 🔒 Security Notes

This project does NOT store:

- Passwords
- LeetCode session tokens
- Cookies

Authentication is taken from your existing browser session.

Never commit:

```
LEETCODE_SESSION
csrftoken
cf_clearance
```

values to GitHub.

---

# 📌 Future Improvements

Possible additions:

- Retry failed imports automatically
- Better CSV format detection
- GUI interface
- Support more coding platforms
- Cloud deployment

---

# License

MIT License