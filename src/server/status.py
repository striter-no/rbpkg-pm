import enum, uuid

class ERROR_CODES(enum.Enum):
    UNDEFINED = -1
    
    # -- Failure statuses
    NO_INPUT_FILES = 0
    EMPTY_FILENAME = 1
    DISALLOWED_FILE = 2
    PACKAGE_CURRUPTED = 3
    NO_PKG_NAME = 4
    INVALID_API_KEY = 5
    NO_SUCH_PKG = 6
    INVALID_PKG_NAME = 7
    INVALID_ACTION = 8
    NO_ACTION_TYPE = 9
    NO_DISTRIBUTION = 10

    # -- Success statuses
    UPLOADED_SUCCSESFULL = 100
    CLIENT_REQUEST_OK    = 101
    CLIENT_REDIRECT      = 102

    # -- Server sc statuses
    SERVER_REQUEST_OK    = 150

class ComposeError:
    
    @staticmethod
    def by_errcode(code: ERROR_CODES, *args) -> dict:
        match code:
            case ERROR_CODES.NO_INPUT_FILES:
                return ComposeError._no_input_files(*args)
            case ERROR_CODES.EMPTY_FILENAME:
                return ComposeError._empty_filename(*args)
            case ERROR_CODES.DISALLOWED_FILE:
                return ComposeError._disallowed_file(*args)
            case ERROR_CODES.PACKAGE_CURRUPTED:
                return ComposeError._package_corrupted(*args)
            case ERROR_CODES.NO_PKG_NAME:
                return ComposeError._no_pkg_name(*args)
            case ERROR_CODES.INVALID_API_KEY:
                return ComposeError._invalid_api_key(*args)
            case ERROR_CODES.NO_SUCH_PKG:
                return ComposeError._no_such_pkg(*args)
            case ERROR_CODES.INVALID_PKG_NAME:
                return ComposeError._invalid_pkg_name(*args)
            case ERROR_CODES.INVALID_ACTION:
                return ComposeError._invalid_action(*args)
            case ERROR_CODES.NO_ACTION_TYPE:
                return ComposeError._no_action_type(*args)
            case ERROR_CODES.NO_DISTRIBUTION:
                return ComposeError._no_distribution(*args)

            case ERROR_CODES.UPLOADED_SUCCSESFULL:
                return ComposeError._uploaded_succsess(*args)
            case ERROR_CODES.CLIENT_REQUEST_OK:
                return ComposeError._client_ok(*args)
            case ERROR_CODES.CLIENT_REDIRECT:
                return ComposeError._cli_redirect(*args)

            case ERROR_CODES.SERVER_REQUEST_OK:
                return ComposeError._server_ok(*args)

            case _:
                return {
                    "display": "[reborn] undefined error on server side", 
                    "error": "UNDEFINED_ERROR",
                    "code": -1
                }

    @staticmethod
    def _no_input_files() -> dict:
        return {
            "display": "no uploaded files. This endpoint only for uploading sites",
            "error": "NO-FILES-DENIED",
            "code": ERROR_CODES.NO_INPUT_FILES.value
        }
    
    @staticmethod
    def _empty_filename() -> dict:
        return {
            "display": "uploaded file has empty filename",
            "error": "EMPTY-FILENAME-DENIED",
            "code": ERROR_CODES.EMPTY_FILENAME.value
        }
    
    @staticmethod
    def _disallowed_file(allowed: set) -> dict:
        return {
            "display": f"uploaded file is not allowed. Currently allowed files are: {", ".join([f"*.{ext}" for ext in allowed])}",
            "error": "FILE-NOT-ALLOWED",
            "code": ERROR_CODES.DISALLOWED_FILE.value
        }
    
    @staticmethod
    def _package_corrupted(reason: str) -> dict:
        return {
            "display": f"uploaded package is seems to be corrupted. Reason: {reason}",
            "error": "PACKAGE-CORRUPTED",
            "code": ERROR_CODES.PACKAGE_CURRUPTED.value
        }
    
    @staticmethod
    def _no_pkg_name() -> dict:
        return {
            "display": f"request has no package name included. Provide \"name\" field in the request",
            "error": "NO-PACKAGE-NAME",
            "code": ERROR_CODES.NO_PKG_NAME.value
        }

    @staticmethod
    def _invalid_api_key() -> dict:
        return {
            "display": f"request API key is invalid (or not provided via \"key\" field). Get API key by uploading non-existent package",
            "error": "INVALID-API-KEY",
            "code": ERROR_CODES.INVALID_API_KEY.value
        }

    @staticmethod
    def _no_such_pkg() -> dict:
        return {
            "display": f"you cannot update this package, because no such package exists",
            "error": "NO-SUCH-PKG",
            "code": ERROR_CODES.NO_SUCH_PKG.value
        }
    
    @staticmethod
    def _invalid_pkg_name(reason: str) -> dict:
        return {
            "display": f"you cannot upload package with this name; reason: {reason}",
            "error": "INVALID-PKG-NAME",
            "code": ERROR_CODES.INVALID_PKG_NAME.value
        }
    
    @staticmethod
    def _invalid_action(reason: str) -> dict:
        return {
            "display": f"you cannot use client with this action: {reason}; only allowed: \"install\" and \"check\"",
            "error": "INVALID-ACTION",
            "code": ERROR_CODES.INVALID_ACTION.value
        }

    @staticmethod
    def _no_action_type() -> dict:
        return {
            "display": f"you cannot use server p2p api without action (field \"type\" is not set)",
            "error": "NO-ACTION-TYPE",
            "code": ERROR_CODES.NO_ACTION_TYPE.value
        }

    @staticmethod
    def _no_distribution() -> dict:
        return {
            "display": f"unfortunatly, this server does not provide distributing services",
            "error": "NO-DISTRIBUTION",
            "code": ERROR_CODES.NO_DISTRIBUTION.value
        }

    # -- Succsessfull exit codes
    @staticmethod
    def _uploaded_succsess(uuid: str) -> dict:
        return {
            "api_key": uuid,
            "display": "pkg uploaded and stored",
            "error": "OK",
            "code": ERROR_CODES.UPLOADED_SUCCSESFULL.value
        }
    
    @staticmethod
    def _client_ok(metadata: None | dict) -> dict:
        return {
            "metadata": metadata,
            "display": "client request",
            "error": "OK",
            "code": ERROR_CODES.CLIENT_REQUEST_OK.value
        }
    
    @staticmethod
    def _cli_redirect(route: str) -> dict:
        return {
            "route": route,
            "display": f"client redirect to {route}",
            "error": "OK",
            "code": ERROR_CODES.CLIENT_REDIRECT.value
        }

    # -- Server side
    
    @staticmethod
    def _server_ok(metadata: None | dict) -> dict:
        return {
            "metadata": metadata,
            "display": "server request",
            "error": "OK",
            "code": ERROR_CODES.SERVER_REQUEST_OK.value
        }