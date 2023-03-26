LOG = 0
MINOR = 1
NORMAL = 2
MAJOR = 3
CRITICAl = 4


class Goof:
    def __init__(self, message: str, severity: int = NORMAL):
        self.message = message
        self.severity = severity

    @property
    def severity_str(self):
        return {
            0: 'Info',
            1: 'Minor',
            2: 'Problem',
            3: 'PROBLEM',
            4: 'CRITICAL'
        }[self.severity]

    def __str__(self):
        return f'{self.severity_str}: {self.message}'

    def __lt__(self, other):
        if hasattr(other, 'severity'):
            return self.severity < other.severity
        else:
            return self.severity < other
