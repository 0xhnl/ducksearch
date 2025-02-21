# DuckDuckGo Search Tool

This Python-based tool allows you to perform DuckDuckGo searches programmatically and save the resulting URLs to a file. It supports pagination, random delays between requests, and error handling for rate limits.

### Features

- Perform DuckDuckGo searches with customizable queries.
- Save search results (URLs) to an output file.
- Supports multiple pages of search results.
- Handles rate limits gracefully by waiting and retrying.
- Adds random delays between requests to avoid triggering anti-bot mechanisms.

### Requirement

- The duckduckgo_search Python package:

```bash
pip3 install duckduckgo-search
```

### Installation

- Clone the Repository:

```bash
git clone https://github.com/0xhnl/ducksearch.git
cd ducksearch
python3 duck.py
```

### Usage

- The tool accepts the following arguments:
  - -s or --search: The search query (required).
  - -o or --output: The output file to save the URLs (required).
  - -p or --pages: The maximum number of pages to fetch (default: 3).
 
```bash
$ python3 duck.py 
usage: duck.py [-h] -s SEARCH -o OUTPUT [-p PAGES]
duck.py: error: the following arguments are required: -s/--search, -o/--output
```

- After running the tool, the output file (output.txt) will contain the URLs of the search results. You can sort and deduplicate the results using standard Unix tools:

```bash
$ python3 duck.py -s "apt phishing campaign collection" -p 2 -o output.txt
Fetched page 1 successfully.
Waiting for 9.97 seconds before fetching the next page...
Fetched page 2 successfully.
Waiting for 9.80 seconds before fetching the next page..

$ cat output.txt | sort -u
https://cloud.google.com/blog/topics/threat-intelligence/apt29-evolving-diplomatic-phishing
https://cloud.google.com/blog/topics/threat-intelligence/not-so-cozy-an-uncomfortable-examination-of-a-suspected-apt29-phishing-campaign
https://cloud.google.com/blog/topics/threat-intelligence/tracking-apt29-phishing-campaigns
https://cybersectools.com/tools/apt-and-cybercriminals-campaign-collection
https://cybersecuritynews.com/apt-attack/
https://freyxfi.github.io/posts/APT29/
https://github.com/CTI-Driven/Advanced-Threat-Hunting-KQL-General-Campaigns/blob/main/APT29-Midnight-Blizzard/APT29+large-scale+spear-phishing+campaign+using+RDP+files.md
https://github.com/blackorbird/APT_REPORT
https://github.com/wddadk/Phishing-campaigns
```

### Notes

- Rate Limits : DuckDuckGo may impose rate limits on automated queries. If the tool hits a rate limit, it will wait for 60 seconds before retrying.
- Random Delays : To mimic human behavior, the tool adds a random delay (5–10 seconds) between requests.
- Error Handling : The tool gracefully handles errors such as network issues or empty result sets.

### Contributing

Contributions are welcome! If you find a bug or want to add a new feature, feel free to open an issue or submit a pull request. Please follow the contribution guidelines .
