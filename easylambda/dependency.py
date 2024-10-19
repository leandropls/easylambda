#  Copyright (c) 2024 Leandro Lima
#
#  This file is part of a proprietary software system of Leandro Lima.
#  No part of this file may be copied, modified, sold, distributed, or used
#  in any way without the written permission of Leandro Lima.

from abc import abstractmethod
from typing import Any

from easylambda.aws import Event


class Dependency:
    __slots__ = ()

    @abstractmethod
    def __call__(self, event: Event) -> Any:
        raise NotImplementedError