from search_client import GitHubSearchClient
import json,time

repos = []
t = time.strftime("%Y%m%d-%H%M%S")
def search(query: str, max_results: int = 10):
    client = GitHubSearchClient(
        minimal_forks=500,
        minimal_stars=1000,
        language="python",
        search_in=["name", "description", "readme"],
        sort_by="stars",    # sort by stars
        sort_order="desc",   # descending     
        topics=["machine-learning", "deep-learning", "mlops", "ai", "artificial-intelligence", "neural-networks", "transformers", "llm", "large-language-models", "nlp", "computer-vision", "reinforcement-learning", "graph-neural-networks", "ai-architecture", "model-architecture", "ai-pipeline", "ai-framework", "ml-framework","machine-learning-framework","deep-learning-framework","xgboost","lightgbm","catboost","tensorflow","pytorch","keras","scikit-learn","huggingface","transformers","openai","stable-diffusion","diffusers","whisper","gpt","bert","gpt-3","gpt-4","llama","llama2","vicuna","falcon","dolly","mistral","gemini","bard","claude","anthropic","chatgpt","chatgpt-plugins","langchain","lora","peft","qwen","qwen-7b","qwen-14b","internlm","internlm-chat","baichuan","baichuan-2","mistral-7b","mistral-7b-instruct","mistral-7b-chat","mistral-13b","mistral-13b-instruct","mistral-13b-chat","mistral-30b","mistral-30b-instruct","mistral-30b-chat"]

    )

    result = client.search_repositories(query=query, max_results=max_results)
    repos.extend(list(result))
    with open(f"repositories_{t}.json", "w", encoding="utf-8") as f:
        json.dump([{
            "full_name": repo.full_name,
            "stars": repo.stargazers_count,
            "svn_url": repo.svn_url,
            "description": repo.description,
            "topics": repo.get_topics(),
            "owner": "https://github.com/"+repo.owner.login
        } for repo in repos], f, indent=4)
    return result


if __name__ == "__main__":
    client = GitHubSearchClient()
    # Basic searches
    # search("machine learning", max_results=10)
    # search("deep learning", max_results=10)
    # search("mlops", max_results=10)
    # search("machine-learning", max_results=10)
    # search("deep-learning", max_results=10)
    # search("artificial intelligence", max_results=10)
    # search("neural networks", max_results=10)
    # search("transformers", max_results=10)
    # search("large language models", max_results=10)
    # search("llm", max_results=10)
    # search("natural language processing", max_results=10)
    # search("nlp", max_results=10)
    # search("computer vision", max_results=10)
    # search("reinforcement learning", max_results=10)
    # search("graph neural networks", max_results=10)
    # search("ai architecture", max_results=10)
    # search("model architecture", max_results=10)
    # search("ai pipeline", max_results=10)
    # search("ai framework", max_results=10)
    # search("ml framework", max_results=10)

    #Fieled specific searches
    # search("finance", max_results=10)
    # search("healthcare", max_results=10)
    # search("education", max_results=10)
    # search("gaming", max_results=10)
    # search("robotics", max_results=10)
    # search("autonomous vehicles", max_results=10)
    # search("cybersecurity", max_results=10)
    # search("e-commerce", max_results=10)
    # search("social media", max_results=10)
    # search("recommendation systems", max_results=10)
    # search("fraud detection", max_results=10)
    # search("predictive maintenance", max_results=10)
    # search("virtual assistants", max_results=10)
    # search("chatbots", max_results=10)
    # search("image recognition", max_results=10)
    # search("speech recognition", max_results=10)
    # search("drug discovery", max_results=10)
    # search("genomics", max_results=10)
    # search("climate modeling", max_results=10)
    # search("supply chain optimization", max_results=10)

    # Github Awesome lists
    # search("awesome", max_results=10)
    # search("awesome-machine-learning", max_results=10)
    # search("awesome-deep-learning", max_results=10)
    # search("awesome-mlops", max_results=10)
    # search("awesome-artificial-intelligence", max_results=10)
    # search("awesome-neural-networks", max_results=10)
    # search("awesome-transformers", max_results=10)
    # search("awesome-llm", max_results=10)
    # search("awesome-large-language-models", max_results=10)
    # search("awesome-nlp", max_results=10)
    # search("awesome-computer-vision", max_results=10)
    # search("awesome-reinforcement-learning", max_results=10)
    # search("awesome-graph-neural-networks", max_results=10)
    # search("awesome-ai-architecture", max_results=10)
    # search("awesome-model-architecture", max_results=10)
    # search("awesome-ai-pipeline", max_results=10)
    # search("awesome-ai-framework", max_results=10)
    # search("awesome-ml-framework", max_results=10)
    # search("awesome-machine-learning-framework", max_results=10)
    # search("awesome-deep-learning-framework", max_results=10)
    # search("awesome-xgboost", max_results=10)

    # Search for repos related to kaggle or huggingface
    search("kaggle", max_results=10)
    search("huggingface", max_results=10)
    search("transformers", max_results=10)
    search("kaggle competition", max_results=10)
    search("kaggle notebooks", max_results=10)
    search("kaggle datasets", max_results=10)
    search("kaggle kernels", max_results=10)
    search("huggingface datasets", max_results=10)
    search("huggingface models", max_results=10)
    search("huggingface transformers", max_results=10)
    search("huggingface spaces", max_results=10)
    search("huggingface tokenizers", max_results=10)
    search("huggingface peft", max_results=10)
    search("huggingface accelerate", max_results=10)

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