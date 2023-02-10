# python-microservice-template

[![Build Status](https://travis-ci.com/alichtman/shallow-backup.svg?branch=master)](https://travis-ci.com/alichtman/shallow-backup)


`python-microservice-template` simple template with  tools, written for python microservices.

Contents
========

 * [Why?](#why)
 * [Folders?](#Folders)
 * [Installation](#installation)
 * [Configuration](#configuration)
 * [Want to contribute?](#want-to-contribute)

### Why?

I wanted a tool that allows you to:

+ Create new python-template for your microservice _from where they live on the system_.
+ Create python ecosystem with tooling and feats.
+ Facilitate setup new project with some tools already configurated.
+ Create patterns about our softwares.

And is incredibly fast.


### Folders

| domain        | details                                                                                                                   |   |
|---------------|---------------------------------------------------------------------------------------------------------------------------|---|
| exceptions.py | Here we declare every domain exceptions, used only in this context                                                        |   |
| model.py      | Here we declare every models of database connections.                                                                     |   |
| repository.py | Here we create all connections with database, queries, insertions and manipulation in data.                               |   |
| schema.py     | Here we declare every schemas of our service, and validations.                                                            |   |
| service.py    | Here we create every handlers of routes, our services should connect routers with database and domain/schemas validations |   |

### Installation

---

> **Warning**
> Be careful running this with elevated privileges. Code execution can be achieved with write permissions on the config file.
> Verify if you put corrects .envs

### Before the methods


```bash
$ git clone git@github.com:zestfy/python-microservice-template.git
$ cd python-microservice-template
```

#### Method 1: [`docker-compose`](https://docs.docker.com/compose/)

```bash
$ docker compose up
```

#### Method 2: Install From Source

```bash
$ make localdb

$ make install

$ make debug
$ make run
```

### Configuration

If you'd like to modify which files are backed up, you have to edit/create new domains and routers and add some logic in boths.

#### .gitignore

In .gitignore we will discart every `envs` `dependencies` and ``.

#### Output Structure

---

```shell
app/
├── domain
│   ├── common
│   │   └── *_base.py
│   ├── domain_1
│   │   └── ...
│   └── domain_2
│       └── ...
├── routers
│   ├── router_1.py
│   └── healthcheck.py
├── internal
│   ├── config
│   │   └── *_base.py
│   ├── kafka
│   │   └── *_base.py
│   ├── utils.py
│   └── others.py
├── 
tests/
│ all.py
└── all.txt
```

### Want to Contribute?

---

Check out `CONTRIBUTING.md` and the `docs` directory.
