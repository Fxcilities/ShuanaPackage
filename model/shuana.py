import os, subprocess
from random import choice
from errors import PornHubRequestError


class Shuana:
    def __init__(self):
        """ Horny person """
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
    
    def proof_of_being_horny(self) -> str:
        """ Sends a proof of shuana being horny. """
        return choice(self.horny)
    
    def __repr__(self) -> str:
        return "<Shuana is_horny=True watching_porn=True>"
        
    @property
    def is_horny(self) -> bool:
        """ Checks if the current state is horny or not. """
        return True
    
    @property
    def watching_porn(self) -> bool:
        """ Checks if the current state is watching porn or not. """
        return True
        
    def film_worldbot_porn(self) -> None:
        """ Films world bot porn. """
        raise PornHubRequestError("At film limit") # smh

    def download_world(self, directory: str = None) -> None:
        """ Downloads World from the official world bot repository. """
        path = os.path.join(os.getcwd(), directory or "world")
        subprocess.run(f'git clone https://github.com/shuanaongithub/World {path}', shell=True)
        print(f'Done! {path}')
