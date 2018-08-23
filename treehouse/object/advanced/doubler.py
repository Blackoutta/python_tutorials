class Double(int):
    def __new__(*args, **kwargs):
        instance = int.__new__(*args, **kwargs)
        instance = instance * 2
        return instance
