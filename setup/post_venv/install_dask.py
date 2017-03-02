def do():
    import setup_utilities
    setup_utilities.log("Installing dask...")
    setup_utilities.pip_install("dask[complete]")
    setup_utilities.log("Dask was installed successfully!")