# pygeppetto

Home of the Geeppetto Python API.
The API allows to create a Geppetto Model from Python.

## Installation

Until pygeppetto is still in development, it is highly recommended to use a
virtualenv in order to deploy it. Once you have a dedicated virtualenv, you
can simply install pygeppetto:

```bash
$ python setup.py install
```

## Pygeppetto API Basic Usage

First, import the pygeppetto API:

```Python
import model as pygeppetto
```

This will load the pygeppetto API and name it `pygeppetto`. Then, you can create
instances and handle them:

```Python
root = pygeppetto.GeppettoModel()  # We create a GeppettoModel instance
root.name = 'MyGeppettoModel'  # We set a name
flib = pygeppetto.GeppettoLibrary()  # We create a new lib
flib.name = 'mylib'
root.libraries.append(flib)  # We add the new lib to the created root
```

If you wan to open an existing XMI, you need to register first all the
`EPackages` from the pygeppetto API:

```Python
# We import the class that will be used to read the XMI from PyEcore
from pyecore.resources import ResourceSet, URI

# We create a new resource set (not required, but better)
rset = ResourceSet()

# Register all the EPackages of pygeppetto inside the ResourceSet
rset.metamodel_registry[pygeppetto.nsURI] = pygeppetto
for subpack in pygeppetto.eSubpackages:
    rset.metamodel_registry[subpack.nsURI] = subpack
```

Then, we are able to read Geppetto XMI:

```Python
model_url = URI('tests/xmi-data/MediumNet.net.nml.xmi')  # The model URI
resource = rset.get_resource(model_url)  # We load the model
geppettomodel = resource.contents[0]  # We get the root
```

At the end of this script, `geppettomodel` contains the model root.

In order to serialize a new version of the modified model, there is two options.
The first one is to serialize onto the existing resource (_i.e_: in the same
file), or to serialize in a new one:

```Python
# Using the first option
resource.save()

# Using the second option
resource.save(output=URI('my_new_file.xmi'))
```

## Dependencies

* Python >= 3.3
* `pyecore` >= 0.1.2

## Contributions

If the `geppettoModel.ecore` evolves, the static metamodel must be regenerated.
The process of adding a new version is the following:

1. Copy the of the new `geppettoModel.ecore` inside `ecore/` (in order to keep a
version from which the static metamodel is generated).
1. Generate the new version of the static metamodel.
1. Manually merge modifications between the current and the new version (if
there is manual modifications in the current version).
1. Run the tests


### How to Generate a New Version

The pygeppetto API is generated from the
[`geppettoModel.ecore`](https://github.com/openworm/org.geppetto.model/blob/development/src/main/resources/geppettoModel.ecore)
using the PyEcore Acceleo generator
([`ecore2pyecore.mtl`](https://github.com/aranega/pyecore/blob/develop/generator/ecore2pyecore.mtl)).
The `.ecore` is a copy of the `geppettoModel.ecore` from
[org.geppetto.model](https://github.com/openworm/org.geppetto.model/blob/development/src/main/resources/geppettoModel.ecore)
(`development` branch). The script can be directly used in Eclipse as a simple
Acceleo generator. The generated code had been directly placed inside the
repository without manual modification.

If manual modifications have been introduced in the version of the static
Geppetto metamodel (_e.g_: implementation of some methods or technical method
additions), this version must be manually merged with the new generated one
(_e.g_: using meld or other tool).


### Run the Tests

Tests are written using `pytest` and are run using `tox`. To launch all the
tests the following command is enough:

```bash
$ tox
```

Currently, the tests are only related to the ability to read/write tests models.
