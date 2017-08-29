def django_enum(cls):
    cls.do_not_call_in_templates = True
    return cls