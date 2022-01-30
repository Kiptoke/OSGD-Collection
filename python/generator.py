"""Builds a static HTML sites from a JSON file and a jinja2 HTML template."""

import sys
import pathlib
import json 
import jinja2
import os
import click

# Main Project Code

@click.command()
@click.option('-v', '--verbose', is_flag=True, help='Prints more output.')
def main(verbose):
    """Static page generator for the Open Source Game Development Collection."""
    
    osgd = []
    
    path = os.path.abspath(os.path.join(os.getcwd(), 'repos'))
    json_files = os.listdir(path)
    
    for file in json_files:
        try:
            json_file = open(f'{path}/{file}')
            repo = json.load(json_file)
            osgd.append(repo)
            json_file.close()
            if verbose:
                print(f"-- File {file} loaded")
        except FileNotFoundError:
            print(f"FileNotFoundError: {file} not found")
            sys.exit(1)
        except ValueError:
            print("JSON Error: Failed to decode json file")
            sys.exit(1)

    osgd_dict = {'osgd':osgd}

    if verbose:
        print(f"-- Writing to list_template.html ") 

    # Open template file
    try:
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader('templates'),
            autoescape=jinja2.select_autoescape(['html', 'xml']),
        )

        template = env.get_template('list_template.html')  

        if verbose:
            print(f"-- list_template.html loaded")
    except jinja2.TemplateNotFound:
            print(f"Jinja Error: list_template.html does not exist")
            sys.exit(1)

    # Open output file
    with open(f'public/list.html', 'w') as html:
        if verbose:
            print(f"-- Loaded list.html")
    
        # Fill out HTML template
        try:
            html.write(template.render(osgd_dict))
        except jinja2.TemplateError:
            print("Jinja Error: Error rendering template")
            sys.exit(1)

    if verbose:
        print("-- Rendered list.html")
    
#if __name__ == "__main__":
main()