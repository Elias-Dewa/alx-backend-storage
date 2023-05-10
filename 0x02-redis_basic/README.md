# 0x02. Redis basic
![image](<https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/1/40eab4627f1bea7dfe5e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230510%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230510T071231Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=02cdd63f9c59894a4fbab62fcf578591935b00af35d69fba4ea1b02c67d28640>
)

## Resources

- [Redis commands](https://redis.io/commands/)
- [Redis python client](https://redis-py.readthedocs.io/en/stable/)
- [How to Use Redis With Python](https://realpython.com/python-redis/)
- [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)

## Install Redis on Ubuntu 18.04

    $ sudo apt-get -y install redis-server
    $ pip3 install redis
    $ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
## Use Redis in a container

Redis server is stopped by default - when you are starting a container, you should start it with: <b>service redis-server start</b>

## Solutions for mandatory and advanced tasks...