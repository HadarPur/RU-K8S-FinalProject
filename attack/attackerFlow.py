from typing import Type
from locust.env import Environment
from locust import User


class AttackerFlow(object):
    def __init__(self, user: Type[User], count: int, spawn_rate: int) -> None:
        # setup Environment and Runner
        self.env = Environment(user_classes=[user])
        self.env.create_local_runner()
        self.count = count
        self.spawn_rate = spawn_rate

    def start(self):
        # start the test
        self.env.runner.start(self.count, spawn_rate=self.spawn_rate)

    def stop(self):
        self.env.runner.quit()
        self.env.runner.greenlet.join()
