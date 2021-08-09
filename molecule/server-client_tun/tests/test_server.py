import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('server')


def test_ping_client(host):
    client = host.addr("10.8.8.2")
    assert client.is_reachable


def test_client_configs_exists(host):
    file1 = host.file("/etc/openvpn/master/client01")
    file2 = host.file("/etc/openvpn/client/client01.ovpn")
    assert file1.exists
    assert file2.exists
