from data.scripts.collections_manager import Collections


class ScriptsManager:
    def __init__(self):
        self.collections = Collections()

    def get_collections(self):
        return self.collections