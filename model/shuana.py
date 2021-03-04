import os, subprocess

from errors import PornHubRequestError


class Shuana:
    def __init__(self):
        self.watching_porn = True
        self.horny = (
            "https://kekers.dev/z4LfpuiA.png",
            "https://kekers.dev/WByc28oF.png",
            "https://kekers.dev/rTjGglBb.png",
            "https://cdn.discordapp.com/attachments/801072847770091550/801073830821888010/fsaJJrbK.png",
            "https://kekers.dev/fX4JEy8q.png",
            "https://kekers.dev/KmVd4tMe.png",
            "https://kekers.dev/zLu2Mpen.png",
            "https://kekers.dev/CI6iXTg8.png"
        )

    def film_worldbot_porn(self):
        raise PornHubRequestError("At film limit")

    def download_world(self, directory = "world"):
        path = os.path.join(os.getcwd(), directory)
        
        subprocess.run(f'git clone https://github.com/shuanaongithub/World {path}', shell=True)
        print(f'Done! {path}')