import requests
import json
import sys
from variables import auth

def main():
    try:
        json_file = open(f'list.json')
        osgd = json.load(json_file)
        json_file.close()
    except ValueError:
        print("JSON Error: Failed to decode json file")
        sys.exit(1)

    for cat in osgd["list"]:
        for repo in osgd["list"][cat]:
            repo_split = repo.split("/")
            user = repo_split[0].replace(" ", "")
            project = repo_split[1].replace(" ", "")
        
            print(f"Fetching {user}/{project}")
            
            with open(f'repos/{project.lower()}.json', 'w') as file:
                r = requests.get(f'https://api.github.com/repos/{user}/{project}', auth=('kiptoke',auth.get('github')))
                category = r.json()
                category.update({"category":cat}) 
                file.write(json.dumps(category, indent=4))
  
if __name__ == "__main__":
    main()