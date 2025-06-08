```markdown
# Reddit Post Fetcher

A simple Python script that fetches recent posts from a specified subreddit within the last 24 hours, including post titles, content, and comments. This project utilizes the Reddit API to retrieve data in JSON format.

## Features

- Fetches recent posts from a specified subreddit.
- Retrieves post titles, content, and comments.
- Structures the output in a clear JSON format.
- Easy to modify for different subreddits.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ssmangat/reddit_scraper.git
   ```

2. Navigate to the project directory:

   ```bash
   cd reddit_scraper
   ```

3. Install the required libraries (if not already installed):

   ```bash
   pip install requests
   ```

## Usage

1. Open the script file (`main.py`) in a text editor.
2. Replace `subreddit` with the desired subreddit name.
3. Run the script:

   ```bash
   python main.py
   ```

4. The output will be printed in JSON format, showing the recent posts and their comments.

## Example Output

```json
{
    "subreddit": "example_subreddit",
    "total_posts": 5,
    "posts": [
        {
            "title": "Post Title 1",
            "content": "This is the content of the post.",
            "url": "https://www.reddit.com/example_post_1",
            "comments": [
                {
                    "author": "commenter1",
                    "body": "This is a comment.",
                    "score": 10
                },
                {
                    "author": "commenter2",
                    "body": "This is another comment.",
                    "score": 5
                }
            ]
        },
        ...
    ]
}
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Reddit API Documentation](https://www.reddit.com/dev/api)
```


