import os
from typing import List, Optional
from github import Github
from dotenv import load_dotenv


class GitHubSearchClient:
    def __init__(
        self,
        base_query: Optional[str] = None,
        minimal_stars: Optional[int] = None,
        minimal_forks: Optional[int] = None,
        recent_push_date: Optional[str] = None,
        topics: Optional[List[str]] = None,
        language: Optional[str] = None,
        search_in: Optional[List[str]] = None,
        sort_by: Optional[str] = None,  # 'stars', 'forks', 'help-wanted-issues', 'updated'
        sort_order: str = "desc",        # 'asc' or 'desc'
    ):
        load_dotenv()
        token = os.getenv("GITHUB_TOKEN")
        if not token:
            raise ValueError("GITHUB_TOKEN is not set in the environment.")
        self.g = Github(token)

        self.base_query = base_query
        self.minimal_stars = minimal_stars
        self.minimal_forks = minimal_forks
        self.recent_push_date = recent_push_date
        self.topics = topics or []
        self.language = language
        self.search_in = search_in or []
        self.sort_by = sort_by
        self.sort_order = sort_order.lower() if sort_order.lower() in ["asc", "desc"] else "desc"

    def build_query(self, custom_query: Optional[str] = None) -> str:
        """
        Build GitHub search query dynamically.
        Only include qualifiers if explicitly set.
        """
        parts: List[str] = []

        # base query
        if custom_query:
            parts.append(custom_query)
        elif self.base_query:
            parts.append(self.base_query)

        # search_in qualifier
        if self.search_in:
            in_fields = ",".join(self.search_in)
            parts.append(f"in:{in_fields}")

        # optional qualifiers
        if self.language:
            parts.append(f"language:{self.language}")
        if self.minimal_stars is not None:
            parts.append(f"stars:>{self.minimal_stars}")
        if self.minimal_forks is not None:
            parts.append(f"forks:>{self.minimal_forks}")
        if self.recent_push_date:
            parts.append(f"pushed:>{self.recent_push_date}")
        if self.topics:
            parts.extend([f"topic:{topic}" for topic in self.topics])

        return " ".join(parts).strip()

    def search_repositories(self, query: Optional[str] = None, max_results: int = 10):
        """
        Search repositories using the constructed query with optional sorting.
        """
        full_query = self.build_query(query)

        # perform search with sorting if specified
        if self.sort_by:
            results = self.g.search_repositories(
            query=full_query,
            sort=self.sort_by,
            order=self.sort_order
            )
        else:
            results = self.g.search_repositories(
            query=full_query
            )

        if max_results >= results.totalCount:
            print(f"Warning: Only {results.totalCount} results found, returning all.")
            return results
        else:
            print(f"Info: {results.totalCount} results found, returning top {max_results}.")
            return results[:max_results]


# if __name__ == "__main__":
#     # Example: search in name + description with sorting
#     client = GitHubSearchClient(
#         base_query="neural networks",
#         minimal_stars=500,
#         language="python",
#         search_in=["name", "description"],
#         sort_by="stars",    # sort by stars
#         sort_order="desc"   # descending
#     )

#     repos = client.search_repositories(max_results=10)
#     print("=== Search Results ===")
#     for repo in repos:
#         print(f"{repo.full_name} ⭐ {repo.stargazers_count}")
