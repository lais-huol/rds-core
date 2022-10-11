import importlib


def get_class(full_class_name, *args, **kwargs):
    module_name, class_name = full_class_name.rsplit(".", 1)
    return getattr(importlib.import_module(module_name), class_name)


def instantiate_class(full_class_name, *args, **kwargs):
    Klass = get_class(full_class_name, *args, **kwargs)
    return Klass(*args, **kwargs)


def get_variable_by_pathname(full_class_name, *args, **kwargs):
    module_name, class_name = full_class_name.rsplit(".", 1)
    return getattr(importlib.import_module(module_name), class_name)
