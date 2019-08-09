import os

from lxml.html.soupparser import fromstring


def extract_topic():
    for dirName, subdirList, fileList in os.walk('./schemas', topdown=True, followlinks=False):
        # print(dirName, subdirList, fileList)
        for file_name in fileList[45:]:
            try:
                with open('{}/{}'.format(dirName, file_name), 'r') as f:
                    s = f.read()
                    print(type(s))
                    tree = fromstring(s)
                    ret = tree.xpath('//*[@id="topic-detail-container"]/div/div[2]/app-talk-content/div/div//text()')

                with open('./new_schemas/{}.md'.format(file_name.strip('.html')), 'a') as f:
                    for i in ret:
                        f.write(i)
            except Exception as e:
                print(e)
                print(file_name)
                print('*' * 50)
            # break
            # break
            # pass


def rename_md():
    count = 0
    for dirName, subdirList, fileList in os.walk('./new_schemas', topdown=True, followlinks=False):
        # print(dirName, subdirList, fileList)
        for file_name in fileList[:]:
            try:
                with open('{}/{}'.format(dirName, file_name), 'r') as f:
                    s = f.readline()
                    # print(s)
                    # break
                    if "#" not in s:
                        print('#', s)
                    ret = s.split("#")[2]
                    os.rename('{}/{}'.format(dirName, file_name), '{}/{}{}.txt'.format(dirName, count ,ret.strip().split('/')[0]))
                    count += 1
                    #break

            except Exception as e:
                print(e)
                print(file_name)
                print('*' * 50)
        print(count)


if __name__ == '__main__':
    rename_md()
