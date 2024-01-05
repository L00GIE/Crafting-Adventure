class Scene:

    def __init__(self):
        self.objects = []

    def loop(self):
        for obj in self.objects:
            if hasattr(obj, "loop"):
                obj.loop()

    def add(self, obj, behindplayer=False):
        if behindplayer:
            playerindex = self.objects.index(self.core.player)
            self.objects.insert(playerindex, obj)
        else:
            self.objects.append(obj)

    def remove(self, obj):
        if obj in self.objects:
            self.objects.remove(obj)
