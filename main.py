import praw
import os
from dotenv import load_dotenv
load_dotenv()

def get_reddit_instance():

    client_id = os.getenv('REDDIT_CLIENT_ID')
    client_secret = os.getenv('REDDIT_CLIENT_SECRET')
    user_agent = os.getenv('REDDIT_USER_AGENT')
    print (client_id,client_secret,user_agent)
    # Create Reddit instance using environment variables
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent=user_agent)
    return reddit

def get_subreddit_rules(subreddit_name):
    reddit = get_reddit_instance()
    subreddit = reddit.subreddit(subreddit_name)
    try:
        rules = subreddit.rules()
        print("Subreddit Rules:")
        print("-----------------")
        for rule in rules['rules']:
            print(f"Rule {rule['kind']}: {rule['description']}")
            print(f"   Short Name: {rule['short_name']}")
            print(f"   Violation Reason: {rule['violation_reason']}")
            print(f"   Created UTC: {rule['created_utc']}")
            print(f"   Priority: {rule['priority']}")
            print()

        print("\nSite Rules:")
        print("-----------")
        for site_rule in rules['site_rules']:
            print(f"- {site_rule}")

        print("\nSite Rules Flow:")
        print("----------------")
        for flow_rule in rules['site_rules_flow']:
            print(f"{flow_rule.get('nextStepHeader', '')}: {flow_rule['reasonTextToShow']}")
            if 'nextStepReasons' in flow_rule:
                for next_reason in flow_rule['nextStepReasons']:
                    print(f"   - {next_reason.get('reasonTextToShow', '')}: {next_reason['reasonText']}")
            print()

    except praw.exceptions.RedditAPIException as e:
        print("An error occurred while fetching subreddit rules:")
        print(e)
    except Exception as e:
        print("An unexpected error occurred:")
        print(e)

def get_top_posts(subreddit_name):
    reddit = get_reddit_instance()
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

def main():
    subreddit_name = input("Enter the subreddit name: ")
    choice = input("Do you want to fetch rules (R) or top posts (P)? ").upper()

    if choice == 'R':
        get_subreddit_rules(subreddit_name)
    elif choice == 'P':
        get_top_posts(subreddit_name)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
