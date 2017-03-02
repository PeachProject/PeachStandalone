def adapt_config(sample_config, end_config, **kwargs):
    from shutil import copyfile
    copyfile(sample_config, end_config)
    for key in kwargs:
        print "{}: {}".format(key, kwargs[key])
        replace_in_file(end_config, "<{}>".format(key), kwargs[key])

def replace_in_file(file, search_string, replacement):
    with open(file,'r') as f:
        newlines = []
        for line in f.readlines():
            newlines.append(line.replace(search_string, replacement))
    with open(file, 'w') as f:
        for line in newlines:
            f.write(line)

