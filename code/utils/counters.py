class Counter:
    def __init__(self, max: int, min: int, start: int) -> None:
        self.max = max
        self.min = min
        self.val = start

    def increment(self, step: int = 1) -> int | bool:
        if self.val + step > self.max:
            return False
        else:
            self.val += step
            return self.val

    def decrement(self, step: int = 1) -> int | bool:
        if self.val - step < self.min:
            return False
        else:
            self.val -= step
            return self.val

    def value(self) -> int:
        return self.val

class RolloverCounter:
    def __init__(self, max: int, min: int, start: int) -> None:
        "counter, but rolls over to min when it reaches max"
        self.max = max
        self.min = min
        self.val = start

    def increment(self, step: int = 1) -> int | str:
        if self.val + step > self.max:
            self.val = self.min
            return "rollover"
        else:
            self.val += step
            return self.val

    def value(self) -> int:
        return self.val