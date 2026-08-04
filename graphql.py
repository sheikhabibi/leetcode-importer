import httpx


class GraphQLClient:

    def __init__(self, cookie_header, csrf):
        self.client = httpx.Client(
            headers={
                "Cookie": cookie_header,
                "x-csrftoken": csrf,
                "Content-Type": "application/json",
                "Origin": "https://leetcode.com",
                "Referer": "https://leetcode.com/",
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/151.0.0.0 Safari/537.36"
                ),
            },
            follow_redirects=True,
        )

    def query(self, operation, query, variables):
        r = self.client.post(
            "https://leetcode.com/graphql/",
            json={
                "operationName": operation,
                "query": query,
                "variables": variables,
            },
        )

        r.raise_for_status()

        return r.json()

    def add_question(self, favorite_slug, question_slug, query):
        response = self.query(
            "addQuestionToFavoriteV2",
            query,
            {
                "favoriteSlug": favorite_slug,
                "questionSlug": question_slug,
            },
        )

        # Success
        data = response.get("data", {})
        result = data.get("addQuestionToFavoriteV2")

        if result:
            return result["ok"], result["error"]

        # GraphQL error
        errors = response.get("errors", [])

        if errors:
            return False, errors[0]["message"]

        return False, "Unknown error"

    def get_list_slug(self, list_name, query):
        response = self.query(
            "myCreatedFavoriteList",
            query,
            {
                "currentQuestionSlug": "two-sum"
            },
        )

        favorites = response["data"]["myCreatedFavoriteList"]["favorites"]

        for fav in favorites:
            if fav["name"] == list_name:
                return fav["slug"]

        return None

    def create_list(self, name, question_slug, query):
        response = self.query(
            "AddQuestionToNewFavoriteV2",
            query,
            {
                "name": name,
                "isPublicFavorite": False,
                "questionSlug": question_slug,
            },
        )

        result = response.get("data", {}).get(
            "addQuestionToNewFavoriteV2"
        )

        if result:
            return result["slug"], result["error"]

        errors = response.get("errors", [])

        if errors:
            return None, errors[0]["message"]

        return None, "Unknown error"

    def get_or_create_list(self, name, first_question, get_query, create_query):

        slug = self.get_list_slug(name, get_query)

        if slug:
            return slug

        print(f"List '{name}' not found. Creating...")

        slug, error = self.create_list(
            name,
            first_question,
            create_query
        )

        if slug:
            print("Created list:", slug)
            return slug

        print("Failed creating list:", error)
        return None