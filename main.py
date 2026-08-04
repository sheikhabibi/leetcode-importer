from leetcode import LeetCodeClient
from graphql import GraphQLClient
from github_csv import GitHubCSV
import time
from queries import GET_LISTS, ADD_QUESTION, CREATE_LIST
import argparse
from tqdm import tqdm
from progress import Progress

parser = argparse.ArgumentParser(
    description="Import LeetCode questions into a collection"
)

parser.add_argument(
    "--list",
    required=True,
    help="LeetCode collection name"
)

parser.add_argument(
    "--csv",
    required=True,
    help="GitHub CSV URL"
)

args = parser.parse_args()

# Connect to LeetCode
lc = LeetCodeClient()
lc.connect()

try:
    gql = GraphQLClient(
        lc.get_cookie_header(),
        lc.csrf()
    )

    list_name = args.list

    csv = GitHubCSV(args.csv)

    questions = csv.get_questions()[:20]

    print(f"Loaded {len(questions)} questions")

    first_question = questions[0]["slug"]

    temp_slug = gql.get_or_create_list(
        list_name,
        first_question,
        GET_LISTS,
        CREATE_LIST
    )

    if temp_slug is None:
        exit()

    print("Found temp:", temp_slug)


    print(f"Loaded {len(questions)} questions")

    added = 0
    skipped = 0

    progress = Progress(list_name)
    progress = Progress(list_name)

    print("Progress file:", progress.filename)

    completed = progress.load()

    # If this is a new list, the first question was already added during creation
    if len(completed) == 0:
        completed.add(questions[0]["slug"])
        progress.save(completed)

    print(f"Already completed: {len(completed)}")

    for question in tqdm(questions, desc=f"Importing {list_name}"):

        if question["slug"] in completed:
            continue

        success, error = gql.add_question(
            temp_slug,
            question["slug"],
            ADD_QUESTION
        )

        if success:
            added += 1
            completed.add(question["slug"])
            progress.save(completed)

        else:
            skipped += 1

        time.sleep(0.25)

    print("\nDone!")
    print(f"Added: {added}")
    print(f"Skipped: {skipped}")
finally:
    lc.close()