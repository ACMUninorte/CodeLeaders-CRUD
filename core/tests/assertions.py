""" copy from https://github.com/sunscrapers/djet/blob/master/djet/assertions.py """


class InstanceAssertionsMixin:
    """
    ORM-related assertions for testing instance creation and deletion.
    """

    def assert_instance_exists(self, model_class, **kwargs):
        try:
            obj = model_class._default_manager.get(**kwargs)
            self.assertIsNotNone(obj)
        except model_class.DoesNotExist:
            raise AssertionError(
                "No {0} found matching the criteria.".format(
                    model_class.__name__,
                )
            )

    def assert_instance_does_not_exist(self, model_class, **kwargs):
        try:
            instance = model_class._default_manager.get(**kwargs)
            raise AssertionError(
                "A {0} was found matching the criteria. ({1})".format(
                    model_class.__name__,
                    instance,
                )
            )
        except model_class.DoesNotExist:
            pass
