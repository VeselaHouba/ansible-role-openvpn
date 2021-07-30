import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('client02')


def test_ping_server(host):
    server = host.addr("10.8.8.1")
    assert server.port(7130).is_reachable
    assert server.is_reachable


def test_custom_route(host):
    routes = host.run("ip r")
    assert "1.1.1.1" in routes.stdout
