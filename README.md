# binja_arch_ref
A simple Binary Ninja plugin to display a cheat sheet with information about the current architecture

## Origins
This project is a product of [NCC Group](https://www.nccgroup.trust/us/)'s 2017 summer internship program. **Further updates will be tracked at [https://github.com/ehennenfent/binja_arch_ref](https://github.com/ehennenfent/binja_arch_ref).** NCC Group is not responsible for any further changes made to the repository after August 18th, 2017.

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
