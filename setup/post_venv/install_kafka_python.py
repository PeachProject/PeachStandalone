def do():
    import setup_utilities
    setup_utilities.log("Installing kafka-python...")
    import pip
    pip.main(["install", "kafka-python"])
    setup_utilities.log("Kafka-Python was installed successfully!")