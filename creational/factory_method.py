class FactoryMethod(object):

    def register(self, name_id, cls):

        if name_id in self._map_id_class and \
                cls != self._map_id_class[name_id]:
            raise Exception(
                f"name_id = {name_id} alredy registered "
                f"as class = {self._map_id_class[name_id].__name__}"
                f" different from class = {cls.__name__}")
        else:
            self._map_id_class[name_id] = cls

    def __init__(self):
        self._map_id_class = {}

    def create_instance(self, name_id, *args, **kwargs):
        if name_id not in self._map_id_class:
            raise Exception(
                f'name_id = {name_id} was not registered.'
                f' Please call register("{name_id}", Class{name_id}).')
        return self._map_id_class[name_id](*args, **kwargs)
