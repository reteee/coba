from pelerbot import LOAD, NO_LOAD, LOGGER


def __list_all_plugins():
    from os.path import dirname, basename, isfile
    import glob

    # This generates a list of plugins in this folder for the * in __main__ to work.
    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_plugins = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]
    if LOAD or NO_LOAD:
        to_load = LOAD
        if to_load:
            if not all(
                any(mod == module_name for module_name in all_plugins)
                for mod in to_load
            ):
                LOGGER.error("Nama Modules yang anda masukan salah.")
                sys.exit(1)
        else:
            to_load = all_modules
        if NO_LOAD:
            LOGGER.info("Modules No Load : {}".format(NO_LOAD))
            return [item for item in to_load if item not in NO_LOAD]
        return to_load
    return all_plugins


ALL_PLUGINS = sorted(__list_all_plugins())
LOGS.info("Modules To Load : %s", str(ALL_PLUGINS))
__all__ = ALL_PLUGINS + ["ALL_PLUGINS"]
