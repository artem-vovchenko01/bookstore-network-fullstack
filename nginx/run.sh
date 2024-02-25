#!/bin/sh

# nginx config variable injection
cat nginx.conf > /etc/nginx/conf.d/default.conf

sleep 8

nginx -g "daemon off;"
