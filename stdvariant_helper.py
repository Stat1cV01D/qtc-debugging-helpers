
# GCC std::variant debugging helper

# Copyright (c) 2020 Stat1cV01D.

# Use, modification and distribution is subject to the Boost Software License,
# Version 1.0. (See accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

from dumper import *


def qdump__std__variant(d, value):
    which = int(value["_M_index"])
    type = d.templateArgument(value.type, which)
    d.putValue("<%s:%s>" % (which, type.name))

    d.putNumChild(1)
    if d.isExpanded():
        storage = value["_M_u"]["_M_first"]["_M_storage"]
        with Children(d, 1):
            d.putSubItem("value", storage.cast(type))
