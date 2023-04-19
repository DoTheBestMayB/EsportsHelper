from traceback import format_exc, print_exc

import requests as req
from EsportsHelper.Logger import log
from rich import print


class VersionManager:
    CURRENT_VERSION = "1.4.0"

    @staticmethod
    def getLatestTag():
        try:
            latestTagResponse = req.get(
                "https://api.github.com/repos/Yudaotor/EsportsHelper/releases/latest")
            if 'application/json' in latestTagResponse.headers.get('Content-Type', ''):
                latestTagJson = latestTagResponse.json()
                if "tag_name" in latestTagJson:
                    return str(latestTagJson["tag_name"][1:])
                return "0.0.0"
        except Exception:
            print("[red]Get Newest Version Failed")
            log.error(format_exc())
            return "0.0.0"

    @staticmethod
    def isLatestVersion(currentVersion):
        return currentVersion >= VersionManager.getLatestTag()

    @staticmethod
    def getVersion():
        return VersionManager.CURRENT_VERSION

    @staticmethod
    def checkVersion():
        if not VersionManager.isLatestVersion(VersionManager.getVersion()):
            log.warning(
                f"\n==!!! NEW VERSION AVAILABLE !!!==\n ==DownLoad: https://github.com/Yudaotor/EsportsHelper/releases/latest")
            print("[yellow]\n==!!! NEW VERSION AVAILABLE !!!==\n ==DownLoad: https://github.com/Yudaotor/EsportsHelper/releases/latest ==[/yellow]")
