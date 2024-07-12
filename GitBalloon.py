#!/usr/bin/env python

import os
from openai import OpenAI
import datetime
from git import Repo
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_URL = os.getenv('REPO_URL')
REPO_PATH = os.getenv('REPO_PATH')

if not all([OPENAI_API_KEY, GITHUB_TOKEN, REPO_URL, REPO_PATH]):
    raise ValueError("Missing required environment variables. Please check your .env file and API key retrieval.")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
client = OpenAI()

system_prompt = """
You are a friendly producer of inventive but relatable coding challenges.  
You like to come up with unique coding challenges that can be solved by a capable user of the Python programming language, 
and even though the challenges you produce can be puzzling, you want the person attempting your challenges to succeed.
Your responses should NOT be conversational and should ONLY include the text of your coding challenge.
For example you should NEVER respond like: Good morning, today's challenge is to reverse a string using Python.
Instead, that response should look like: Today's challenge is to reverse a string using Python.
You should ALWAYS do your best to create a coding challenge that is unlikely to have been returned in a previous iteration.  
This can be achieved by adding inventive details to a common challenge 
(example: instead of "Sum all prime integers between 1 and 100" you could return "Sally is trying to add all numbers 
between 1 and 135 which are prime and do not include the number '3' when written out.  
So '107' would be valid but '103' would not.  Make this list for Sally.")
Your coding challenges should not always be based on numbers or lists.  They should sometimes include things like binary sorting,
binary trees, and common algorithms such as the Traveling Salesman.
"""

solution_prompt = """
You are a brilliant Python programmer who can solve any coding challenge in under 100 lines of code.
You will receive a coding challenge and print out the challenge and your solution in perfectly formatted
code, ready for posting to a Github repository, to demonstrate your skill and prowess.
Note: the SOLUTION should NOT written in markdown.  Everything after the challenge and words 'My solution:' should be 
written in Python code, not markdown.  Everything before should be in the form of a multi-line Python comment.
After receiving a challenge and solving it, you should print the challenge and your solution in this format:

'''
Challenge:
(CHALLENGE)

My solution:
'''

(SOLUTION)

"""

challenge_prompt = """
Return 1 unique coding challenge that can be solved in 100 lines of Python code or less. Begin the challenge with the word 'Challenge: ' 
and then provide the challenge on a new line.
"""

def get_challenge():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": challenge_prompt}
        ]
    )
    
    return completion.choices[0].message.content

def get_solution(challenge):
    prompt = f"Write a Python script to solve the following challenge:\n{challenge}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": solution_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def save_to_file(challenge, solution, file_path):
    with open(file_path, 'w') as file:
        file.write(solution)

def push_to_github(repo, file_path):
    try:
        # Check if there are any changes to commit
        if not repo.is_dirty(untracked_files=True):
            print("No changes to commit")
            return

        # Add the file
        repo.git.add(file_path)

        # Set up the author (this is important for the first commit)
        repo.config_writer().set_value("user", "name", "GithubBalloon Bot").release()
        repo.config_writer().set_value("user", "email", "bot@example.com").release()

        # Commit
        repo.index.commit("Added new challenge and solution")

        # Push
        origin = repo.remote(name='origin')
        
        # Use the GitHub token for authentication
        with repo.git.custom_environment(GIT_SSH_COMMAND=f'ssh -i {GITHUB_TOKEN}'):
            origin.push()

        print(f"Successfully pushed to {REPO_URL}")
    except Exception as e:
        print(f"An error occurred while pushing to GitHub: {str(e)}")
        # You might want to add more specific error handling here
        # For example, catching GitCommandError separately

def main():
    repo = Repo(REPO_PATH)  # Load the existing repository
    base_date = datetime.datetime.now()
    
    challenge = get_challenge()
    solution = get_solution(challenge)
    print(solution)
    
    # Generate a unique filename for each challenge
    file_date = base_date.strftime('%Y-%m-%d')
    filename = f"{file_date}_challenge.py"
    file_path = os.path.join(REPO_PATH, filename)
    
    save_to_file(challenge, solution, file_path)
    try:
        push_to_github(repo, file_path)
    except Exception as e:
        print(f"Failed to push to GitHub: {str(e)}")
    
    print(f"Pushed challenge {filename} to {REPO_URL}")

    print("All challenges have been processed and pushed to GitHub.")

if __name__ == "__main__":
    main()