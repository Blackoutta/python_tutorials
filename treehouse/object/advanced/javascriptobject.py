class JavaScriptObject(dict):
    fake = {'fake': True}
    def __getattribute__(self, item):
        try:
            return self[item]
        except KeyError:
            return super().__getattribute__(item)
#When getting a local instance attribute, a KeyError may be raised if
#the attribute is not found. In this situation, instead of raising the
#error, the code calls the parent class's __getattribute__ to access the
#class attributes.

jso = JavaScriptObject({'name': 'Yang'})
jso.language = 'Python'

# this will cause error
