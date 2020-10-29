# Ansible Role: openvpn
=========

[![Build Status](https://travis-ci.com/VeselaHouba/openvpn.svg?branch=master)](https://travis-ci.com/github/VeselaHouba/openvpn)

Minimalistic openvpn role with CA + client cert generation

## Requirements

None,

## Role Variables

I'm too lazy for now to explain all the variables. You can find them in `defaults/main.yml` and they are split to ones you should setup and ones which are optional.

**Note:** `openvpn_clients` variable is structured the way it can be interchanged with my bareos role. So you can easily connect this role with bareos (run this first) and have secure connection anywhere. Isn't that great?

## Example Playbook

    - hosts: servers
      roles:
         - { role: openvpn }

## License

BSD
