def do():
    # Install virtual env, create virtual environment
    import setup_utilities

    from subprocess import call
    call(["virtualenv", "venv"])

    setup_utilities.log("Successfully created virtual environment in /venv")

if __name__ == '__main__':
    create_venv()