import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

request = requests.get(url)
response_dict = request.json()



repo_dicts = response_dict['items']



names, plot_dicts = [],[]

for repo_dict in repo_dicts:

    names.append(repo_dict["name"])
    plot_dict = {"value": repo_dict["stargazers_count"],
                 "label" : repo_dict["description"] if repo_dict["description"] else "",
                 "xlink" : repo_dict['html_url']}

    plot_dicts.append(plot_dict)

    # plot_dicts.append(plot_dict)

for line in plot_dicts:
    print(line)

my_config = pygal.Config()
my_config.x_label_rotation = -45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.show_y_guides = False
my_config.width = 1000
my_style = LS('#333366', base=LCS)

chart = pygal.Bar(my_config,style = my_style)
chart.force_uri_protocol = "http"
chart._title = "Top starred python projects on Github"
chart.x_labels = names
chart.add('',plot_dicts)
chart.render_to_file("python_repos.svg")
