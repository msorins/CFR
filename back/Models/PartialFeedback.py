class PartialFeedback:
    def __init__(self, message, points, evaluator) -> None:
        super().__init__()

        self.message = message
        self.points = points
        self.evaluator = evaluator

    def __str__(self) -> str:
        return self.message + " \nPoint -> " + str(self.points)
