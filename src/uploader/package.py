import tarfile, os

def extract_pkg(file: tarfile.TarFile, pkges_path: str):
    pass

def pack_pkg(env_path: str, pkg_name: str) -> tuple[bool, str]:
    dir_path = os.path.join(env_path, pkg_name)
    if not os.path.exists(dir_path):
        return False, f"pkg or enviroment does not exists (full path: {dir_path})"
    
    packed_dir = os.path.join(env_path, ".packed_pkgs")
    os.makedirs(packed_dir, exist_ok = True)
    with tarfile.open(os.path.join(packed_dir, pkg_name) + '.tar', 'w') as arch:
        for el in [
            "rbpkg.version",
            "README",
            "rbpkg.install",
            "rbpkg.build",
            "build"
        ]:
            path = os.path.join(dir_path, el)
            if not os.path.exists(path):
                print(f"[reborn] packing directory does not contain file/directory: {el}")
                exit(5)
            arch.add(path, el)
        
        for el in [
            "bin",
            "lib"
        ]:
            if os.path.exists(os.path.join(dir_path, el)):
                arch.add(os.path.join(dir_path, el), el)

    return True, os.path.join(packed_dir, pkg_name) + ".tar"