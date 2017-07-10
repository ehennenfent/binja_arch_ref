from binaryninja import show_html_report, PluginCommand, user_plugin_path, log_error, show_plain_text_report
from mako.template import Template
from mako import exceptions

template = Template(filename=(user_plugin_path + '/binja_arch_ref/template.mhtml'))

def render(bv):
    try:
        show_html_report(bv.arch.name + " Architecture Reference", template.render(arch=bv.arch, platform=bv.platform))
    except:
        show_plain_text_report(bv.arch.name + ": Error in Rendering", exceptions.text_error_template().render())

PluginCommand.register("Show Architecture Reference", \
    "Displays a reference for the architecture based on the architecture object available in the binary view.", render)
