""" Module of custom meta class """

class CustomMeta(type):
    """ CustomMeta """

    def __new__(cls, class_name, parents, attributes):

        def __setattr__(self, attr_name, value):
            self.__dict__[f'custom_{attr_name}'] = value

        custom_attr = {'__setattr__': __setattr__}
        for name, val in attributes.items():
            if not name.startswith('__'):
                custom_attr[f'custom_{name}'] = val
            else:
                custom_attr[name] = val

        return super(CustomMeta, cls).__new__(cls, class_name, parents, custom_attr)
