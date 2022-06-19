import os


class Config:
    LOGGER = True
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH", None)
    MAX_MESSAGE_LENGTH = 4096
    COMMAND_HANDLER = os.environ.get("COMMAND_HANDLER", ["~", "!", "*"])
    TMP_DOWNLOAD_DIRECTORY = os.environ.get(
        "TMP_DOWNLOAD_DIRECTORY", "/root/pelerbot/Downloads"
    )
    OFFICIAL_UPSTREAM_REPO = os.environ.get(
        "OFFICIAL_UPSTREAM_REPO", None
    )
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    OWNER_ID = int(os.environ.get("OWNER_ID", "5372076947"))
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
    TG_MAX_SELECT_LEN = int(os.environ.get("TG_MAX_SELECT_LEN", "100"))
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    OWNER_NAME = os.environ.get("OWNER_NAME", "Gaclexxx")
    PRIVATE_GROUP_ID = int(os.environ.get("PRIVATE_GROUP_ID", "-1001773996149"))
    LOG_GROUP = os.environ.get("LOG_GROUP", "-1001773996149")
    PM_PERMIT = bool(os.environ.get("PM_PERMIT", False))
    REMBG_API_KEY = os.environ.get("REMBG_API_KEY", None)
    MEGANZ_PASSWORD = os.environ.get("MEGANZ_PASSWORD", None)
    MEGANZ_EMAIL = os.environ.get("MEGANZ_EMAIL", None)
    STRING_SESSION1 = os.environ.get("STRING_SESSION1", "BQCLtn1qIG49DC4xEzYfRBsNEEcLKuWjDIb4N4tZWh50ZhDzeLzQQ7x0Sgo3oLBhP168PRah-IhE1R01vITMs74qvUnoJ_SXwIDOxb3U3c9PJlX4en6JTt2WfZfq15cPUx9lDVEA-bTbMedYyC08-b83IFp0ls1nd3xph00hn3ztopvjvsjOFystEaLYTaYtNuFerrIRghjuR0uKz9Nc6CuH34Xmx2XLiwtvzvfPzaH-weUcPYOxPpXETNy6cyyuf_Y9fkdTOhVG7_ibWXCx_KoT-kDgCgwf_Xr_fNeUZpoSkK1Xd7NfLirpvHKxD2iMb7sFx9NiC0zHVaIbTRwFV2OiAAAAAUAzY5MA")
    STRING_SESSION2 = os.environ.get("STRING_SESSION2", "BQBCHpVUdfkP7lydbY9g_fekagIleM4Pwyg_nkDf6gjz4VCvX7q26xMr0qwLdrd5v1BF_x1zyR_7MJkEoaAB7L5uOTaGhBQweFv1gkQDo5d3m2C2igU1flY7asBx0ge3S0SAnyLfG0DaqM5dPnj7NaIT_LubAAgq7RJRJ7LVk5-INtBuGJu8kIDFCGBvhbnYU4EMn-vLrIplYi434D0kWyJeXy_wjYKjvsexA9j4NZ0JAbmsl3IUDWuV4AK4YaeTIeGiLF1Ywi-YGQ1Ggsuia0MMyL-V69vqVlN3W5aq3Ts2QU7iD5EnkERUXsQu-0GJq5CfvHBKFSLXZFiKSEDvGOwWAAAAATOJJRMA")
    STRING_SESSION3 = os.environ.get("STRING_SESSION3", "BQBdDdorx7074SzDFDCqRmgmXsGnjUnTxyjhHrFrotuuitLRupgOkF1u_6QZLVSvWCK0c3OA7zpUVbXcwpeHH8uR-PU5HfSBK6xB2sbWxAVJhNJtdbkYeGxQZr-81b-6yU4r5QGYBzcQiXAr-aglm_ZllPsWgoQKjP1mjJ68h4j3CXVakbqr36ZvSIKOKUtbI8Sj87rzrSbTFump5SdSQpnjsORxqqtsJgE8c_dxeN4aFetYBlsE-YCMZTs6jBIk0cMggM6pGys9dOV5SWtua5rBiD5QG-1mThj_tOF5xI9MozPRiq1VfK3iOPtbQVprmIpp3JelLj0qmnwV1HFoizNRAAAAAUYtUcsA")
    STRING_SESSION4 = os.environ.get("STRING_SESSION4", "")
    STRING_SESSION5 = os.environ.get("STRING_SESSION5", "")
    STRING_SESSION6 = os.environ.get("STRING_SESSION6", "")
    STRING_SESSION7 = os.environ.get("STRING_SESSION7", "")
    STRING_SESSION8 = os.environ.get("STRING_SESSION8", "")
    STRING_SESSION9 = os.environ.get("STRING_SESSION9", "")
    STRING_SESSION10 = os.environ.get("STRING_SESSION10", "")
    STRING_SESSION11 = os.environ.get("STRING_SESSION11", "")
    STRING_SESSION12 = os.environ.get("STRING_SESSION12", "")
    STRING_SESSION13 = os.environ.get("STRING_SESSION13", "")
    STRING_SESSION14 = os.environ.get("STRING_SESSION14", "")
    STRING_SESSION15 = os.environ.get("STRING_SESSION15", "")
    STRING_SESSION16 = os.environ.get("STRING_SESSION16", "")
    STRING_SESSION17 = os.environ.get("STRING_SESSION17", "")
    STRING_SESSION18 = os.environ.get("STRING_SESSION18", "")
    STRING_SESSION19 = os.environ.get("STRING_SESSION19", "")
    STRING_SESSION20 = os.environ.get("STRING_SESSION20", "")
    STRING_SESSION21 = os.environ.get("STRING_SESSION21", "")
    STRING_SESSION22 = os.environ.get("STRING_SESSION22", "")
    STRING_SESSION23 = os.environ.get("STRING_SESSION23", "")
    STRING_SESSION24 = os.environ.get("STRING_SESSION24", "")
    STRING_SESSION25 = os.environ.get("STRING_SESSION25", "")
    STRING_SESSION26 = os.environ.get("STRING_SESSION26", "")
    STRING_SESSION27 = os.environ.get("STRING_SESSION27", "")
    STRING_SESSION28 = os.environ.get("STRING_SESSION28", "")
    STRING_SESSION29 = os.environ.get("STRING_SESSION29", "")
    STRING_SESSION30 = os.environ.get("STRING_SESSION30", "")
    STRING_SESSION31 = os.environ.get("STRING_SESSION31", "")
    STRING_SESSION32 = os.environ.get("STRING_SESSION32", "")
    STRING_SESSION33 = os.environ.get("STRING_SESSION33", "")
    STRING_SESSION34 = os.environ.get("STRING_SESSION34", "")
    STRING_SESSION35 = os.environ.get("STRING_SESSION35", "")
    STRING_SESSION36 = os.environ.get("STRING_SESSION36", "")
    STRING_SESSION37 = os.environ.get("STRING_SESSION37", "")
    STRING_SESSION38 = os.environ.get("STRING_SESSION38", "")
    STRING_SESSION39 = os.environ.get("STRING_SESSION39", "")
    STRING_SESSION40 = os.environ.get("STRING_SESSION40", "")
    STRING_SESSION41 = os.environ.get("STRING_SESSION41", "")
    STRING_SESSION42 = os.environ.get("STRING_SESSION42", "")
    STRING_SESSION43 = os.environ.get("STRING_SESSION43", "")
    STRING_SESSION44 = os.environ.get("STRING_SESSION44", "")
    STRING_SESSION45 = os.environ.get("STRING_SESSION45", "")
    STRING_SESSION46 = os.environ.get("STRING_SESSION46", "")
    STRING_SESSION47 = os.environ.get("STRING_SESSION47", "")
    STRING_SESSION48 = os.environ.get("STRING_SESSION48", "")
    STRING_SESSION49 = os.environ.get("STRING_SESSION49", "")
    STRING_SESSION50 = os.environ.get("STRING_SESSION50", "")

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
