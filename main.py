from search_client import GitHubSearchClient
import json,time

repos = []
def search(query: str, max_results: int = 10):
    client = GitHubSearchClient(
        minimal_forks=500,
        minimal_stars=1000,
        language="python",
        search_in=["name", "description"],
        sort_by="stars",    # sort by stars
        sort_order="desc"   # descending        
    )

    result = client.search_repositories(query=query, max_results=max_results)
    repos.extend(list(result))
    t = time.strftime("%Y%m%d-%H%M%S")
    with open(f"repositories_{t}.json", "w", encoding="utf-8") as f:
        json.dump([repo.raw_data for repo in repos], f, indent=4)
    return result


if __name__ == "__main__":
    client = GitHubSearchClient()
    search("machine learning", max_results=10)
    search("deep learning", max_results=10)
    search("mlops", max_results=10)
    search("machine-learning", max_results=10)
    search("deep-learning", max_results=10)
    search("artificial intelligence", max_results=10)
    search("neural networks", max_results=10)
    search("transformers", max_results=10)
    search("large language models", max_results=10)
    search("llm", max_results=10)
    search("natural language processing", max_results=10)
    search("nlp", max_results=10)
    search("computer vision", max_results=10)
    search("reinforcement learning", max_results=10)
    search("graph neural networks", max_results=10)
    search("ai architecture", max_results=10)
    search("model architecture", max_results=10)
    search("ai pipeline", max_results=10)
    search("ai framework", max_results=10)
    search("ml framework", max_results=10)

    # Save results to an HTML file for better readability
    print(f"Total repositories returned: {len(list(repos))}")
    with open("repositories.html", "w", encoding="utf-8") as f:
        f.write("<html><head><title>GitHub Repositories</title></head><body>")
        f.write(f"<h2>Total repositories returned: {len(list(repos))}</h2>")
        
        for repo in repos:

            print("=== Repository ===")
            print("Full Name:", repo.full_name)
            print("Stars:", repo.stargazers_count)
            print("SVN URL:", repo.svn_url)
            print("Description:", repo.description)
            print()
            f.write("""
            <div style="
                background: #f9f9f9;
                border-radius: 8px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.07);
                margin-bottom: 24px;
                padding: 18px 24px;
                font-family: 'Segoe UI', Arial, sans-serif;
            ">
                <h3 style="margin-top:0;color:#0366d6;">Repository</h3>
                <p><strong>Full Name:</strong> <span style="color:#24292e;">{full_name}</span></p>
                <p><strong>Stars:</strong> <span style="color:#f1c40f;">&#9733; {stars}</span></p>
                <p><strong>SVN URL:</strong> <a href="{svn_url}" style="color:#0366d6;text-decoration:none;">{svn_url}</a></p>
                <p><strong>Description:</strong> <span style="color:#586069;">{description}</span></p>
            </div>
            """.format(
                full_name=repo.full_name,
                stars=repo.stargazers_count,
                svn_url=repo.svn_url,
                description=repo.description if repo.description else "No description provided."
            ))
        f.write("</body></html>")