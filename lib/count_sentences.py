#!/usr/bin/env python3
class MyString:
    def __init__(self, value=""):  # Assuming an __init__ method to set initial value
        self.value = value

    def get_value(self):
        return self._value

    def set_value(self, string):
        if type(string) == str:
            self._value = string
        else:
            print("The value must be a string.")

    value = property(get_value, set_value)

    def is_sentence(self):
        return self._value[-1] == "."

    def is_question(self):
        return self._value[-1] == "?"   

    def is_exclamation(self):
        return self._value[-1] == "!"

    def count_sentences(self) -> int:
        """
        Count the number of sentences in a given string.

        Returns:
            The number of sentences in the given string.
        """
        value = self.value.replace('!', '.').replace('?', '.')
        sentences = [sentence for sentence in value.split('.') if sentence]
        return len(sentences)
