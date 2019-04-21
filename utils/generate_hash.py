from werkzeug.security import generate_password_hash, check_password_hash


class GenerateHash(object):
    value = None
    originalValeu = None

    def __init__(self, value_to_hash=None, original_value=None):
        self.value = value_to_hash
        self.originalValue = original_value

    def generate(self):
        return generate_password_hash(self.value)

    def check_hash(self):
        return check_password_hash(self.originalValue, self.value)
