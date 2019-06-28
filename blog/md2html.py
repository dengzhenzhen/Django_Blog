import markdown
import os

def md2html(md_text):
    html_text = markdown.markdown(md_text, 
                                  extensions = ['markdown.extensions.extra',
                                                'markdown.extensions.codehilite',
                                                'markdown.extensions.toc',
                                                ])
    return html_text


if __name__ == "__main__":
    path = 'C:\\Users\\BENCH\Documents\\GitHubPage\\dengzhenzhen.github.io\\_posts'
    file_name = '2018-09-05-LogisticRegression.md'
    path = path.replace('\\','/')
    file_path = '{0}/{1}'.format(path, file_name)

    print(file_path)
    print('\n\n\n')

    with open(file_path,'r',errors = 'ignore') as fp:
        md_text = fp.read()


    html_text = markdown.markdown(md_text, extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])

    with open(file_path.replace('.md', '.html'), 'w') as fp:
        fp.write(html_text)
