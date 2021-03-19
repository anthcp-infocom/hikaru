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
from hikaru.meta import (HikaruBase, CatalogEntry, TypeWarning)
from hikaru.generate import (get_python_source, get_clean_dict, get_yaml, get_json,
                             load_full_yaml, get_processors)
from hikaru.model import *

model_classes = [k for k, v in globals().items()
                 if type(v) == type and
                 k != HikaruBase]

__version__ = "v0.1.1a0"

__all__ = ["HikaruBase", "CatalogEntry", "get_json", "get_yaml", "get_python_source",
           "get_clean_dict", "load_full_yaml", "get_processors", "TypeWarning"]
__all__.extend(model_classes)
del model_classes
