import pytest
from pyecore.resources import ResourceSet, URI
import model as pygeppetto


@pytest.fixture(scope='module')
def rset():
    rset = ResourceSet()
    rset.metamodel_registry[pygeppetto.nsURI] = pygeppetto
    for subpack in pygeppetto.eSubpackages:
        rset.metamodel_registry[subpack.nsURI] = subpack
    return rset


def test_read_mediumXMI(rset):
    resource = rset.get_resource(URI('tests/xmi-data/MediumNet.net.nml.xmi'))
    root = resource.contents[0]
    assert root  # The root exists


def test_read_BigXMI(rset):
    resource = rset.get_resource(URI('tests/xmi-data/BigCA1.net.nml.xmi'))
    root = resource.contents[0]
    assert root  # The root exists


def test_read_LargeXMI(rset):
    resource = rset.get_resource(URI('tests/xmi-data/LargeConns.net.nml.xmi'))
    root = resource.contents[0]
    assert root  # The root exists


def test_readwrite_mediumXMI(tmpdir, rset):
    resource = rset.get_resource(URI('tests/xmi-data/MediumNet.net.nml.xmi'))
    root = resource.contents[0]
    f = tmpdir.mkdir('pyecore-tmp').join('medium.xmi')
    resource.save(output=URI(str(f)))


def test_readwrite_BigXMI(tmpdir, rset):
    resource = rset.get_resource(URI('tests/xmi-data/BigCA1.net.nml.xmi'))
    root = resource.contents[0]
    f = tmpdir.mkdir('pyecore-tmp').join('big.xmi')
    resource.save(output=URI(str(f)))


def test_readwrite_LargeXMI(tmpdir, rset):
    resource = rset.get_resource(URI('tests/xmi-data/LargeConns.net.nml.xmi'))
    root = resource.contents[0]
    f = tmpdir.mkdir('pyecore-tmp').join('large.xmi')
    resource.save(output=URI(str(f)))


def test_roundtrip_mediumXMI(tmpdir, rset):
    resource = rset.get_resource(URI('tests/xmi-data/MediumNet.net.nml.xmi'))
    root = resource.contents[0]

    # We change the root name
    root.name = 'mediumTestModel'

    # We serialize the modifications
    f = tmpdir.mkdir('pyecore-tmp').join('medium.xmi')
    resource.save(output=URI(str(f)))

    # We read again the file
    resource = rset.get_resource(URI(str(f)))
    root = resource.contents[0]
    assert root
    assert root.name == 'mediumTestModel'


def test_roundtrip_BigXMI(tmpdir, rset):
    resource = rset.get_resource(URI('tests/xmi-data/BigCA1.net.nml.xmi'))
    root = resource.contents[0]

    # We change the root name
    root.name = 'bigTestModel'

    # We serialize the modifications
    f = tmpdir.mkdir('pyecore-tmp').join('big.xmi')
    resource.save(output=URI(str(f)))

    # We read again the file
    resource = rset.get_resource(URI(str(f)))
    root = resource.contents[0]
    assert root
    assert root.name == 'bigTestModel'


def test_roundtrip_LargeXMI(tmpdir, rset):
    resource = rset.get_resource(URI('tests/xmi-data/LargeConns.net.nml.xmi'))
    root = resource.contents[0]

    # We change the root name
    root.name = 'largeTestModel'

    # We serialize the modifications
    f = tmpdir.mkdir('pyecore-tmp').join('large.xmi')
    resource.save(output=URI(str(f)))

    # We read again the file
    resource = rset.get_resource(URI(str(f)))
    root = resource.contents[0]
    assert root
    assert root.name == 'largeTestModel'
