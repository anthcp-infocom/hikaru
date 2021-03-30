#
# Copyright (c) 2021 Incisive Technology Ltd
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""
DO NOT EDIT THIS FILE!

This module is automatically generated using the hikaru.build program that turns
a Kubernetes swagger spec into the code for the hikaru.model module.
"""


from hikaru.meta import HikaruBase, HikaruDocumentBase
from typing import Optional, List, Dict
from dataclasses import dataclass, field


@dataclass
class RawExtension(HikaruBase):
    r"""
    RawExtension is used to hold extensions in external versions. To use this, make a
    field which has RawExtension as its type in your external, versioned struct, and
    Object in your internal struct. You also need to register your various plugin types.
    // Internal package: type MyAPIObject struct { runtime.TypeMeta `json:",inline"`
    MyPlugin runtime.Object `json:"myPlugin"` } type PluginA struct { AOption string
    `json:"aOption"` } // External package: type MyAPIObject struct { runtime.TypeMeta
    `json:",inline"` MyPlugin runtime.RawExtension `json:"myPlugin"` } type PluginA struct
    { AOption string `json:"aOption"` } // On the wire, the JSON will look something like
    this: { "kind":"MyAPIObject", "apiVersion":"v1", "myPlugin": { "kind":"PluginA",
    "aOption":"foo", }, } So what happens? Decode first uses json or yaml to unmarshal the
    serialized data into your external MyAPIObject. That causes the raw JSON to be stored,
    but not unpacked. The next step is to copy (using pkg/conversion) into the internal
    struct. The runtime package's DefaultScheme has conversion functions installed which
    will unpack the JSON stored in RawExtension, turning it into the correct object type,
    and storing it in the Object. (TODO: In the case where the object is of an unknown
    type, a runtime.Unknown object will be created and stored.)

    Full name: io.k8s.apimachinery.pkg.runtime.RawExtension

    Attributes:
    """


class IntOrString(str):
    r"""
    IntOrString is a type that can hold an int32 or a string. When used in JSON or YAML
    marshalling and unmarshalling, it produces or consumes the inner type. This allows you
    to have, for example, a JSON field that can accept a name or number.

    Full name: io.k8s.apimachinery.pkg.util.intstr.IntOrString
    """


class Quantity(str):
    r"""
    Quantity is a fixed-point representation of a number. It provides convenient
    marshaling/unmarshaling in JSON and YAML, in addition to String() and AsInt64()
    accessors. The serialization format is: <quantity> ::= <signedNumber><suffix> (Note
    that <suffix> may be empty, from the "" case in <decimalSI>.) <digit> ::= 0 | 1 | ...
    | 9 <digits> ::= <digit> | <digit><digits> <number> ::= <digits> | <digits>.<digits> |
    <digits>. | .<digits> <sign> ::= "+" | "-" <signedNumber> ::= <number> |
    <sign><number> <suffix> ::= <binarySI> | <decimalExponent> | <decimalSI> <binarySI>
    ::= Ki | Mi | Gi | Ti | Pi | Ei (International System of units; See:
    http://physics.nist.gov/cuu/Units/binary.html) <decimalSI> ::= m | "" | k | M | G | T
    | P | E (Note that 1024 = 1Ki but 1000 = 1k; I didn't choose the capitalization.)
    <decimalExponent> ::= "e" <signedNumber> | "E" <signedNumber> No matter which of the
    three exponent forms is used, no quantity may represent a number greater than 2^63-1
    in magnitude, nor may it have more than 3 decimal places. Numbers larger or more
    precise will be capped or rounded up. (E.g.: 0.1m will rounded up to 1m.) This may be
    extended in the future if we require larger or smaller quantities. When a Quantity is
    parsed from a string, it will remember the type of suffix it had, and will use the
    same type again when it is serialized. Before serializing, Quantity will be put in
    "canonical form". This means that Exponent/suffix will be adjusted up or down (with a
    corresponding increase or decrease in Mantissa) such that: a. No precision is lost b.
    No fractional digits will be emitted c. The exponent (or suffix) is as large as
    possible. The sign will be omitted unless the number is negative. Examples: 1.5 will
    be serialized as "1500m" 1.5Gi will be serialized as "1536Mi" Note that the quantity
    will NEVER be internally represented by a floating point number. That is the whole
    point of this exercise. Non-canonical values will still parse as long as they are well
    formed, but will be re-emitted in their canonical form. (So always use canonical form,
    or don't diff.) This format is intended to make it difficult to use these numbers
    without writing some sort of special handling code in the hopes that that will cause
    implementors to also use a fixed point implementation.

    Full name: io.k8s.apimachinery.pkg.api.resource.Quantity
    """


@dataclass
class Info(HikaruBase):
    r"""
    Info contains versioning information. how we'll want to distribute that information.

    Full name: io.k8s.apimachinery.pkg.version.Info

    Attributes:
    buildDate:
    compiler:
    gitCommit:
    gitTreeState:
    gitVersion:
    goVersion:
    major:
    minor:
    platform:
    """

    buildDate: str
    compiler: str
    gitCommit: str
    gitTreeState: str
    gitVersion: str
    goVersion: str
    major: str
    minor: str
    platform: str


globs = dict(globals())
__all__ = [c.__name__ for c in globs.values()
           if type(c) == type]
del globs
