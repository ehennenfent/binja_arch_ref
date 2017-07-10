# binja_arch_ref
A simple Binary Ninja plugin to display a cheat sheet with information about the current architecture

## Features
* Address Size
* Integer Size
* Endianness
* Link register
* Stack pointer
* Calling conventions
    - Caller-saved registers
    - Argument registers
    - Return register
* Flags
* Full-width registers

## Usage
With a binary view open, open the tools menu and click "Show Architecture Reference"

## Contributing
This plugin generates an HTML report via a Mako template. To add information or make stylistic changes, simply modify template.mhtml

## Dependencies
* Mako
* Binary Ninja
