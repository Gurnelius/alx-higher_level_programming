#!/usr/bin/python3
'''
    LockedClass with no class or object attribute.
'''


class LockedClass:
    '''
    LockedClass with no class or object attribute, that prevents
    the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.
    '''
    __slots__ = ('first_name',)

    def __setattr__(self, name, value):
        if name != 'first_name':
            err_msg = f"'{self.name}' object has no attribute '{name}'"
            raise AttributeError(err_msg)
        super().__setattr__(name, value)
