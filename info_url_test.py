import os
import time

from tiktok_downloader import info_post


# same post links but different url forms:
link1 = 'https://www.tiktok.com/@nederlandermetsnor/video/7075724233594211590'
link2 = 'https://vm.tiktok.com/ZMLcjPAuS/?k=1'

file = 'mov.mp4'

try:
    for link in [link2, link1]:
        t = time.perf_counter()

        print(f'Getting info from {link = }')
        post = info_post(url=link)

        print(f'Started download')
        post.download(file)

        print(f'Finished in {round(time.perf_counter() - t, 3)} seconds\n')

    print('Successfully finished')

finally:
    try:
        os.remove(file)
    except FileNotFoundError:
        pass
