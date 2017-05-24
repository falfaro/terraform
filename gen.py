#!/usr/bin/python3

import os
import jinja2

def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)

context = {
  'hostnames': {
    'manager1': {},
    'worker1': {},
    'worker2': {},
  }
}

with open('tf/docker.tf', 'w') as h:
  result = render('docker.tmpl', context)
  h.write(result)
