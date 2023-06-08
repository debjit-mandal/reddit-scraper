import praw

# Initialize the Reddit instance
reddit = praw.Reddit(client_id='6NU_L-SWNmi6u_l0ZvZhXA',
                  client_secret='ol7IU_q7o7SIejnnhuJQ0aEe49hqmg',
                     user_agent='debjit_8925')

# Define the subreddit you want to scrape
subreddit_name = 'AskReddit'

# Get the subreddit instance
subreddit = reddit.subreddit(subreddit_name)

# Define the number of posts you want to retrieve
num_posts = 10

# Create a list to store the scraped data
scraped_data = []

try:
    # Retrieve the top 'num_posts' posts from the subreddit
    top_posts = subreddit.top(limit=num_posts)

    # Iterate over the top posts and retrieve additional information
    for post in top_posts:
        title = post.title
        score = post.score
        author = post.author
        url = post.url
        num_comments = post.num_comments
        created_utc = post.created_utc

        # Retrieve the top 3 comments for each post
        post.comments.replace_more(limit=0)
        top_comments = post.comments[:3]
        comments = [comment.body for comment in top_comments]

        # Store the scraped data as a dictionary
        post_data = {
            'Title': title,
            'Score': score,
            'Author': str(author),
            'URL': url,
            'Num_Comments': num_comments,
            'Comments': comments,
            'Created_UTC': created_utc
        }

        scraped_data.append(post_data)

    # Print the scraped data
    for post in scraped_data:
        print('Title:', post['Title'])
        print('Score:', post['Score'])
        print('Author:', post['Author'])
        print('URL:', post['URL'])
        print('Number of Comments:', post['Num_Comments'])
        print('Comments:')
        for comment in post['Comments']:
            print('- ', comment)
        print('---')

except Exception as e:
    print(f"An error occurred: {str(e)}")
