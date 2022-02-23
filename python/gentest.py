"""Gathers JSON data from the GitHub API and generates a static site from a jinja2 HTML template."""

import sys
import json 
import jinja2
import click
import requests
import os
from variables import auth

# Main Project Code

@click.command()
@click.option('-v', '--verbose', is_flag=True, help='Prints more output.')
@click.option('-r', '--repos', is_flag=True, help='Generates output files for all repositories.')
@click.option('-f', '--final', is_flag=True, help='Creates a file of the final JSON sent to the template.')
@click.option('-u', '--update', required=True, type=bool, help='Calls the GitHub API while building the site.')
def main(verbose, repos, final, update):
    """The site generator for the Open Source Game Development Collection.
    
        NOTICE: In order to build without an update, 'full_repos.json' must exist in your repository.
    """
    token = ''
    
    if not update:
        with open(f'full_repos.json', 'r', encoding="utf-8") as reps:
            osgd = json.load(reps)
            build(osgd, verbose, final)
            sys.exit(0)
    
    osgd = {}
    
    if verbose:
        print("Building site...")
        print("---------- GATHERING DATA ----------")
        
    try:
        json_file = open(f'list.json')
        repo_list = json.load(json_file)
        json_file.close()
    except ValueError:
        print("JSON Error: Unable to decode OSGD JSON list")
        sys.exit(1)

    full_repos = {}
    
    for cat in repo_list["list"]:
        cat_list = []
        for repo in repo_list["list"][cat]:
            repo_split = repo.split("/")
            user = repo_split[0].replace(" ", "")
            project = repo_split[1].replace(" ", "")
        
            if verbose:
                print(f"- Fetching {user}/{project}")

            request = requests.get(f'https://api.github.com/repos/{user}/{project}', auth=('kiptoke', os.getenv('token'))).json()
            
            if "message" in request:
                print(f"JSON Error: Unable to fetch {user}/{project}")
                sys.exit(1)
                
            # TODO: Is there a way to handle this without having to keep an empty "repos" file around?
            if repos:
                with open(f'repos/{project.lower()}.json', 'w', encoding="utf-8") as file:
                    file.write(json.dumps(request, indent=4))
                    
            cat_list.append(request)
        
        full_repos.update({cat: cat_list})
    
    osgd = {"osgd":full_repos}
    
    build(osgd, verbose, final)
    
def build(osgd, verbose, final):
    if verbose:
        print("---------- GENERATING SITE ----------")
        
    if final:
        with open(f'full_repos.json', 'w', encoding="utf-8") as json_file:
            json_file.write(json.dumps(osgd, indent=4))
    
    # Open template file
    try:
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader('templates'),
            autoescape=jinja2.select_autoescape(['html', 'xml']),
        )

        template = env.get_template('list_template.html')  

        if verbose:
            print(f"- list_template.html loaded")
    except jinja2.TemplateNotFound:
            print(f"Jinja Error: list_template.html does not exist")
            sys.exit(1)

    # Open output file
    with open(f'index.html', 'w', encoding="utf-8") as html:
        if verbose:
            print(f"- Loaded list.html")
    
        # Fill out HTML template
        try:
            html.write(template.render(osgd))
        except jinja2.TemplateError:
            print("Jinja Error: Error rendering template")
            sys.exit(1)

    if verbose:
        print("- Rendered list.html")
        
#if __name__ == "__main__":
main()