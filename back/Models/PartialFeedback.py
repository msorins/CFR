class PartialFeedback:
    def __init__(self, message, points) -> None:
        super().__init__()

        self.message = message
        self.points = points

    def __str__(self) -> str:
        return self.message + " -> " + self.points

