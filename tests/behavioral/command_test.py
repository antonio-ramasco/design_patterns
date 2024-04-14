from behavioral.command import Reicever, ConcreteCommand, Invoker

def test_command():
    receiver=Reicever()
    command=ConcreteCommand(Reicever())

    #invoker without command
    invoker = Invoker()
    assert invoker.execute() is None

    #invoker with command
    invoker.store_command(command)
    assert invoker.execute()=="ConcreteCommand."+receiver.action()
