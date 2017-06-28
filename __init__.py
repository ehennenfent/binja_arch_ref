from binaryninja import show_markdown_report, PluginCommand

def build_markdown(markdown, new_markdown, newline='\n\n'):
    return markdown + new_markdown + newline

def render(bv):
    markdown = ""

    arch = bv.arch

    markdown = build_markdown(markdown, "# {} Cheat Sheet".format(arch.name))
    markdown = build_markdown(markdown, "#### Address Size: {}".format(arch.address_size))
    markdown = build_markdown(markdown, "#### Endianness: {}".format(arch.endianness))

    markdown = build_markdown(markdown, "#### Link Register: {}".format(arch.link_reg))
    markdown = build_markdown(markdown, "#### Stack Pointer: {}".format(arch.stack_pointer))

    markdown = build_markdown(markdown, "## Calling Conventions")
    for convention in bv.arch.calling_conventions:
        convention = bv.arch.calling_conventions[convention]
        markdown = build_markdown(markdown, "### {}".format(convention.name))

        markdown = build_markdown(markdown, "#### Caller-Saved Registers:")
        for reg in convention.caller_saved_regs:
            markdown = build_markdown(markdown, '    ' + reg)

        markdown = build_markdown(markdown, "#### Integer Argument Registers:")
        for reg in convention.int_arg_regs:
            markdown = build_markdown(markdown, '    ' + reg)

        markdown = build_markdown(markdown, "#### Integer Return Register: {}".format(convention.int_return_reg), newline="\n\n \n")

        markdown = build_markdown(markdown, "#### Float Argument Registers:")
        for reg in convention.float_arg_regs:
            markdown = build_markdown(markdown, '    ' + reg)

        markdown = build_markdown(markdown, "#### Float Return Register: {}".format(convention.float_return_reg), newline="\n\n----------\n\n")

    markdown = build_markdown(markdown, "## Flags and Registers")

    markdown = build_markdown(markdown, "#### Flags:")
    for flag in bv.arch.flags:
        markdown = build_markdown(markdown, "    {flag} - {name}".format(flag=flag, name=bv.arch.flag_roles[flag].name.replace("Role","")))

    markdown = build_markdown(markdown, "#### Full width registers:")
    for reg in bv.arch.full_width_regs:
        markdown = build_markdown(markdown, '    ' + reg)

    show_markdown_report(bv.arch.name + " Architecture Reference", markdown)

PluginCommand.register("Show Architecture Reference", "Displays a reference for the architecture based on the architecture object available in the binary view.", render)
