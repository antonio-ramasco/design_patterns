from structural.proxy import RealSubject, Proxy

def test_proxy_real_subject():

    real_subject = RealSubject()
    assert real_subject.request()=="RealSubject.request"

    proxy = Proxy(real_subject)
    proxy.request()
    assert proxy.request()==real_subject.request()

