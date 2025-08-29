# Reborn Package Manager

> or rbpkg

is a project for package managment, written in python3, and it has features like:

- Distributed package storing
- Uses minimal privileges on both (server and client) sides, therefore does not require root
- Can be installed via 1 HTTP GET request
- By design have `wiper` script after installing for wipping all data that was installed

## Server's work principle

Server requests `probe` file to create a network of the servers. Main idea is:

When client requests a package, server will check its existence in his DB, if it's not presented there, server will ask other servers for this package and other servers do the same, until all network will be checked. 

## Packages structure

RBPKG Package contains:

- `rbpkg.install` - main script; it is called right after extracting all package data at a client machine
- `rbpkg.build` - script that provides build (transforming code into binary/executable scripts) instrutions for package
- `rbpkg.version` - text file, that contains branch and version of the package (in format `branch:major.minor.patch`) 
- `README` - text file with commentary to the package
- `build/` - directory with all files, necessary for build
  - `code/` - directory with sub-dirs and files with code
  - `scripts/` - direcotry with scripts focused for building parts of the project
- `bin/` - unnecessary directory; may contain pre-built binaries
- `lib/` - unnecessary directory; may contain pre-built libraries (static and dynamic)

## Installing and distributing

You can _distribute_ all programs via existent server of the rbpkg-pm (if it allows the distribution) by this simple commands:

> WARNING: Installer will do all installation process in current working directory 

```sh
# Will fetch installation script for the CLIENT
curl -s http://domain:port/scripts/client | bash
# after it there will be rbpkg, update.rbcli, wiper.rbcli

# Will fetch installation script for the SERVER
curl -s http://domain:port/scripts/server | bash
# after it there will be rbpkg-serv, update.rbserv, wiper.rbserv

# Will fetch installation script for the UPLOADER
curl -s http://domain:port/scripts/upload | bash
# after it there will be rbpkg-upl, update.rbupl, wiper.rbupl
```

**Wiper** - script, that will _wipe_ all installed data (client, server or upload part remains on the suffix of the wiper script)

**Update** - script, that will wipe data and than download it again from the same server as it was, when part of the rbpkg system was downloaded

## RBPKG sub-systems

### Client

Usage:

```sh
usage: rbpkg [-h] [-e ENVIRON] [-i INSTALL] [-c CHECK] [-u UPDATE] [-s SYM]
```

- `-e`/`--environ` - directory, where all files of the client will be
- `-i`/`--install` - will try install specified package
- `-c`/`--check` - will check, if package exists and if so, will print his `version`, `branch` and `README`
- `-u`/`--update` - will lookup current version and server's version of the package, if they differ - will install new version
- `-s`/`--sym` - will create symbolic link in current directory for specified binary file (they appear in `package/bin/` after `rbpkg.build` will be complited and moved to `ENV/.bin`)

### Uploader

Usage:

```sh
usage: rbpkg-upl [-h] [-b] -e ENVIRON -p PACKAGE [-u URL] [-k KEY]
```

- `-b`/`--blank` - will create in enviroment empty (hello-world) package with all necessary files
- `-e`/`--environ` - directory, where all files of the uploader will be
- `-p`/`--package` - specifies name of the package (charset is a-Z 0-9 and '_-')
- `-u`/`--url` - url of the server to upload the package
- `-k`/`--key` - usually you will not use this param, but it can specify update-api-key for the upload request

### Server

Usage:

```sh
usage: rbpkg-serv [-h] -l LOCAL -p PUBLIC [-d] -e ENVIRON [-b PROBE]
```

- `-l`/`--local` - specifies local address to bind the HTTP server (in format of `IP:PORT`)
- `-p`/`--public` - specifies publicly accessable address of the server (in format of `http://IP:PORT`)
- `-d`/`--no-distro` - if presented, disallows to distribute any program from this server
- `-e`/`--environ` - directory, where all files of the server will be
- `-b`/`--probe` - specifies path to the file with known servers. If such file does not exists, but probing requested - server will ask you to enter known hosts

## Installing from github

If you want to fresh version of the server, client or the uploader, you can install all components via:

```sh
git clone https://github.com/striter-no/rbpkg-pm
cd ./rbpkg-pm

python -m venv venv
source ./venv/bin/activate
pip install -r ./requirements.txt
```

Now you can run `rbpkg` (client), `rbpkg-upl` (uploader) or `rbpkg-serv` (server) as they were downloaded via distribution system