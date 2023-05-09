# 0x01. NoSQL

## Resources

- [NoSQL Databases Explained](https://riak.com/resources/nosql-databases/)
- [What is NoSQL ?](https://www.youtube.com/watch?v=qUV2j3XBRHc)
- [MongoDB with Python Crash Course - Tutorial for Beginners](https://www.youtube.com/watch?v=E-1xI85Zog8)
- [MongoDB Tutorial 2 : Insert, Update, Remove, Query](https://www.youtube.com/watch?v=CB9G5Dvv-EE)
- [Aggregation](https://www.mongodb.com/docs/manual/aggregation/)
- [Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)
- [mongo Shell Methods](https://www.mongodb.com/docs/manual/reference/method/)
- [The mongo Shell](https://www.mongodb.com/docs/404/)

## More Info

Install MongoDB 4.2 in Ubuntu 18.04

[Official installation guide](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/)

--------------------------------

    $ wget -qO - <https://www.mongodb.org/static/pgp/server-4.2.asc> | apt-key add -
    $ echo "deb [ arch=amd64,arm64 ] <https://repo.mongodb.org/apt/ubuntu> bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
    $ sudo apt-get update
    $ sudo apt-get install -y mongodb-org
    ...
    $  sudo service mongod status
    mongod start/running, process 3627
    $ mongo --version
    MongoDB shell version v4.2.8
    git version: 43d25964249164d76d5e04dd6cf38f6111e21f5f
    OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
    allocator: tcmalloc
    modules: none
    build environment:
        distmod: ubuntu1804
        distarch: x86_64
        target_arch: x86_64
    $
    $ pip3 install pymongo
    $ python3
    >>> import pymongo
    >>> pymongo.__version__
    '3.10.1'

## Use “container-on-demand” to run MongoDB

- Ask for container Ubuntu 18.04 - MongoDB
- Connect via SSH
- Or via the WebTerminal
- In the container, you should start MongoDB before playing with it:

------------------------------------------------
    $ service mongod start
    - Starting database mongod                                              [ OK ]
    $
    $ cat 0-list_databases | mongo
    MongoDB shell version v4.2.8
    connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
    Implicit session: session { "id" : UUID("70f14b38-6d0b-48e1-a9a4-0534bcf15301") }
    MongoDB server version: 4.2.8
    admin   0.000GB
    config  0.000GB
    local   0.000GB
    bye
    $

## Solutions for mandatory and advanced tasks...