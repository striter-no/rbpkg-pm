import tarfile, os

def check_package(file: tarfile.TarFile) -> tuple[bool, str]:
    _version = False
    _readme = False
    _build = False
    _install = False
    _build_dir = False
    _scripts_dir = False
    _code_dir = False

    _bin = False
    _lib = False

    for memb in file.getmembers():
        if memb.isfile():
            match memb.name:
                case 'rbpkg.version': _version = True
                case 'README': _readme = True
                case 'rbpkg.install': _install = True
                case 'rbpkg.build': _build = True
        if memb.isdir():
            match memb.name:
                case "build": _build_dir = True; continue
                case "bin": _bin = True; continue
                case "lib": _lib = True; continue
            
            if memb.path == "build/code":
                _code_dir = True
            if memb.path == "build/scripts":
                _scripts_dir = True
    
    if not _build_dir: return False, "no build directory in package's root"
    if not _version:   return False, "no rbpkg.version in package's root"
    if not _readme:    return False, "no README in package's root"
    if not _install:   return False, "no rbpkg.install in package's root"
    if not _build:     return False, "no rbpkg.build in package's root"
    if not _code_dir:  return False, "no code directory in package's build directory"
    if not _scripts_dir: return False, "no scripts directory in package's build directory"

    return True, "ok"