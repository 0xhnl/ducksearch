#!/usr/bin/env python3

import argparse
import time
import random
from duckduckgo_search import DDGS
from duckduckgo_search.exceptions import DuckDuckGoSearchException

# Function to perform the search
def perform_search(query, output_file, max_pages=3):
    # Open the output file in append mode (to avoid overwriting)
    with open(output_file, 'a') as f:
        # Use DuckDuckGo to perform the search
        with DDGS() as ddgs:
            page_count = 0
            while page_count < max_pages:
                try:
                    # Perform the search and fetch one page of results
                    results = list(ddgs.text(query))
                    
                    if not results:
                        print("No more results found.")
                        break
                    
                    # Write URLs to the output file
                    for result in results:
                        url = result.get('href', None)
                        if url:
                            f.write(url + '\n')
                    
                    # Increment the page counter
                    page_count += 1
                    print(f"Fetched page {page_count} successfully.")
                
                except DuckDuckGoSearchException as e:
                    # Handle rate limit errors
                    print(f"Rate limit hit: {e}. Waiting for 60 seconds before retrying...")
                    time.sleep(60)
                    continue
                
                # Add a random delay between requests (5–10 seconds)
                delay = random.uniform(5, 10)
                print(f"Waiting for {delay:.2f} seconds before fetching the next page...")
                time.sleep(delay)

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Perform a DuckDuckGo search and save URLs to a file.")
    parser.add_argument('-s', '--search', required=True, help='Search query')
    parser.add_argument('-o', '--output', required=True, help='Output file to save URLs')
    parser.add_argument('-p', '--pages', type=int, default=3, help='Maximum number of pages to fetch')

    # Parse arguments
    args = parser.parse_args()

    # Perform the search and save results
    perform_search(args.search, args.output, args.pages)

if __name__ == "__main__":
    main()
