import os

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
network_name = os.environ['DOCKER_NETWORK_NAME']
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_IMAGE']
c.DockerSpawner.network_name = network_name
c.JupyterHub.hub_ip = os.environ['HUB_IP']
#c.JupyterHub.hub_ip = 'jupyterhub'
#c.JupyterHub.hub_ip = public_ips()[0]
#c.DockerSpawner.hub_ip_connect = public_ips()[0]
#network fix?
c.DockerSpawner.use_internal_ip = True
# Pass the network name as argument to spawned containers
c.DockerSpawner.extra_host_config = { 'network_mode': network_name }
c.DockerSpawner.extra_start_kwargs = { 'network_mode': network_name }
c.PAMAuthenticator.open_sessions = False


# default 

c.Spawner.default_url = '/lab'

#user data persistence tester...

notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/work'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }


# Service

c.JupyterHub.services = [
    {
        'name': 'cull_idle',
        'admin': True,
        'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
    },
]
