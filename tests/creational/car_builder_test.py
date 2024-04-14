from creational.car_builder import JeepLayoutBuilder, HondaDirector


def test_car_builder():
    #check director create the same car of the direct JeepLayoutBuilder
    jeep_builder = JeepLayoutBuilder()
    honda_director = HondaDirector()
    honda_director.create_car(jeep_builder)
    jeep_honda = jeep_builder.get_car()

    jeep_builder2 = JeepLayoutBuilder()
    jeep_builder2.build_body("Honda")
    jeep_honda2 = jeep_builder2.get_car()

    assert str(jeep_honda) == str(jeep_honda2)
