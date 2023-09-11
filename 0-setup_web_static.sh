#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo 'Holberton School' > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
loc="
location \/hbnb_static {
	alias \/data\/web_static\/current\/;
}"
line="server_name _;"
sed -i "s/$line/$line\n$loc/" /etc/nginx/sites-available/default
service nginx restart
