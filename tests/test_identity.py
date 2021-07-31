from identity import id 

def test_identity():
    for n, v in enumerate([0,1,2,3,4]):
        assert id(n) == v
