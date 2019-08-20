#!/usr/bin/python3
"""2-do_deploy_web_static module"""
from os.path import isfile
from fabric.api import put, run, env

env.hosts = ["35.237.54.178", "35.196.248.176"]


def do_deploy(archive_path):
    """Distributes an archive to your web servers
    archive_path: Path to archive
    Returns: True if all operations done sucessful, otherwise False
    """
    if isfile("archive_path") is False:
        return False

    try:
        apne = archive_path.split('/')[1].split('.')[0]

        put("archive_path", "/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(apne))
        run("tar -xzf /tmp/{} -C \
/data/web_static/releases/{}".format(archive_path,
            apne))
        run("rm /tmp/{}".format(archive_path))
        run("mv /data/web_static/releases/{}/web_static/* \
/data/web_static/releases/{}".format(apne, apne))
        run("rm -rf /data/web_static/releases/{}/web_static".format(apne))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} \
/data/web_static/current".format(apne))
        return True
    except Exception:
        return False
