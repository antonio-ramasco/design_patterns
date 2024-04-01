class Singleton(type):
    __instances = {}
    _DEBUG = True

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            if Singleton._DEBUG:
                print(f"Singleton __call__ {cls.__name__} new instance")
            instance = super().__call__(*args, **kwargs)
            cls.__instances[cls] = instance
        else:
            if Singleton._DEBUG:
                print(f"Singleton __call__ {cls.__name__} get existing instance")
            instance = cls.__instances[cls]

        if Singleton._DEBUG:
            print(
                f"Singleton __call__ {cls.__name__} returning instance id {id(instance)}"
            )
            print(f"cls.__instances={cls.__instances}")
        return instance
