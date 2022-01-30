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

    for repo in osgd["list"]:
        repo_split = repo.split("/")
        user = repo_split[0]
        project = repo_split[1]
    
        with open(f'repos/{project.lower()}.json', 'w') as file:
            r = requests.get(f'https://api.github.com/repos/{repo}', auth=('kiptoke',auth.get('github')))
            file.write(json.dumps(r.json(), indent=4))
  
if __name__ == "__main__":
    main()