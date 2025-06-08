import requests
import time
import json

def fetch_recent_posts(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/new.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return []

    data = response.json()
    posts = data['data']['children']
    recent_posts = []

    for post in posts:
        post_data = post['data']
        created_time = post_data['created_utc']
        if time.time() - created_time <= 86400:  # 86400 seconds in 24 hours
            post_info = {
                'title': post_data['title'],
                'content': post_data['selftext'],  # Post content
                'url': post_data['url'],
                'comments': fetch_comments(post_data['id'], headers)  # Fetch comments
            }
            recent_posts.append(post_info)

    return recent_posts

def fetch_comments(post_id, headers):
    url = f"https://www.reddit.com/comments/{post_id}.json"
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error fetching comments for post {post_id}: {response.status_code}")
        return []

    comments_data = response.json()
    comments = []
    
    # The comments are in the second element of the returned JSON array
    for comment in comments_data[1]['data']['children']:
        comment_data = comment['data']
        comments.append({
            'author': comment_data['author'],
            'body': comment_data['body'],
            'score': comment_data['score']
        })

    return comments

if __name__ == "__main__":
    subreddit = "subreddit"  # Replace with your subreddit
    posts = fetch_recent_posts(subreddit)
    
    # Structure the output
    structured_output = {
        'subreddit': subreddit,
        'total_posts': len(posts),
        'posts': posts
    }
    
    # Convert the structured output to JSON format
    json_output = json.dumps(structured_output, indent=4)
    print(json_output)

