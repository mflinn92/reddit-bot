import praw

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit('doublebass')

def main():
    for post in subreddit.hot(limit=10):
        print(post.title)

if __name__ == '__main__':
    main()