import os


# Create folder if not created
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Directory Created')
        os.makedirs(directory)


# To crawl a page we need to provide a link to start, The crawler starts looking at all the links in the page and
# craws them Two text files will be created which stores the links to be crawled and the other for the links which
# are crawled

# Create queue and crawled files if not created
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.exists(queue):
        write_file(queue, base_url)  # sending base url because in the start it is not crawled
    if not os.path.exists(crawled):
        write_file(crawled, '')  # Empty String as nothing is crawled in the first stage


def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# Add data to existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data, '\n')


# Delete the contents of a file
def delete_file_contents(path):
    with open(path, 'w'):
        pass


# Read a file and add each line into a set
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# Iterate through the set and add each item to the file
def set_to_file(links, file_name):
    delete_file_contents(file_name)
    for link in sorted(links):
        append_to_file(file_name, link)
