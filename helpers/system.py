import os
import importlib
from pathlib import Path
import sys

this_file = sys.modules[__name__]

def import_configs(file_name, prelix, in_app=''):
    # Root path
    root_path = os.path.dirname(Path(__file__).resolve().parent)

    # Import configs file
    if in_app != '':
        root_path = os.path.join(root_path, in_app)
        in_app += '.'
        
    configs_path = os.path.join(root_path, file_name+'s')
    configs_name = [f[:-3] for f in os.listdir(configs_path) if f.endswith('.py')]

    configs = {}
    
    for module_name in configs_name:
        module_path = in_app + file_name + 's.' + module_name
        module = importlib.import_module(module_path)
        setattr(this_file, module_name + '_' + prelix, module)
        # if os.getenv('APP_ENV', 'local'):
        #     print('from {}{}s import {} as {}'.format(in_app, file_name, module_name, module_name + '_' + prelix))
    
    return configs


def content_file_import(file_name, prelix, in_app=''):
    # Root path
    root_path = os.path.dirname(Path(__file__).resolve().parent)

    # Import configs file
    if in_app != '':
        root_path = os.path.join(root_path, in_app)
        in_app += '.'
        
    configs_path = os.path.join(root_path, file_name+'s')
    configs_name = [f[:-3] for f in os.listdir(configs_path) if f.endswith('.py')]

    configs = ''
    
    for module_name in configs_name:
        configs += 'from {}{}s import {} as {}\n'.format(in_app, file_name, module_name, module_name + '_' + prelix)
    
    return configs


def create_file(
        configs, 
        file = '/auto_import.py', 
        root_path = os.path.join(str(Path(__file__).resolve().parent.parent), 'my_app', 'views')
    ):
    f = open(str(root_path) + file, "w")
    f.writelines(configs)
    f.close()