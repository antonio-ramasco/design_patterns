from __future__ import annotations
from structural.adapter import Target, Adapter, client_code


def test_adapter_target():
    target = Target()
    res = client_code(target)
    assert res == "Target request"


def test_adapter_adaptee():
    adapter = Adapter()
    res = client_code(adapter)
    assert "Adaptee request" in res


class UsbC:
    def connect(self) -> str:
        return "USB C"


class UsbB:
    def connect_to_usb_b(self) -> str:
        return "USB B"


class UsbC_to_UsbB(UsbC, UsbB):
    def connect(self) -> str:
        return f"{self.connect_to_usb_b()}"


def usb_connect(usbc: UsbC) -> str:
    return usbc.connect()


def test_adapter_usbc():
    res = usb_connect(UsbC())
    assert res == "USB C"


def test_adapter_adaptee():
    adapter = UsbC_to_UsbB()
    res = usb_connect(adapter)
    assert res == "USB B"
