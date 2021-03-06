from fabric.api import env

host1 = 'root@10.204.216.35'

ext_routers = [('mx1', '10.204.216.253')]
router_asn = 64512
public_vn_rtgt = 10003
public_vn_subnet = "10.204.219.16/28"

host_build = 'stack@10.204.216.37'

env.roledefs = {
    'all': [host1],
    'cfgm': [host1],
    'openstack': [host1],
    'control': [host1],
    'compute': [host1],
    'collector': [host1],
    'webui': [host1],
    'database': [host1],
    'build': [host_build],
}

env.hostnames = {
    'all': ['nodeb4']
}

env.passwords = {
    host1: 'c0ntrail123',
    host_build: 'contrail123',
}

env.ostypes = {
   host1 : 'fedora'
}

env.test_repo_dir='/home/stack/single_node/test'
env.mail_from='vjoshi@juniper.net'
env.mail_to='dl-contrail-sw@juniper.net'
env.log_scenario='Fedora Openstack Single-Node Sanity'
multi_tenancy=True

env.interface_rename = True
