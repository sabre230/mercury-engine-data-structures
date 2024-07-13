import construct
from construct import (
    Array,
    Const,
    Hex,
    Construct,
    Float32l,
    Int16ul,
    Check,
    Int32ul,
    Struct,
)

from mercury_engine_data_structures.common_types import StrId, make_vector
from mercury_engine_data_structures.formats import BaseResource
from mercury_engine_data_structures.game_check import Game

BMSEM = Struct(
    _magic=Const(b"MSEM"),
    _version=Const(0x00030001, Hex(Int32ul)),
    groups=make_vector(Struct(
            "group_name" / StrId,
            "layers" / make_vector(Struct(
                "layer_name" / StrId,
                "entries" / make_vector(Struct(
                    "collision_camera" / StrId,
                    "song" / StrId,             # Is empty if cc is "default".
                    "unk1" / Float32l,          # Always either 2.0 or 1.5
                    "unk2" / Float32l,          # Always same number as unk1
                    "unk3" / Int32ul,           # Always 1
                    "unk4" / Int32ul            # Always 0
                ))
            ))
    )),
    rest=construct.GreedyBytes,
)

class Bmsem(BaseResource):
    @classmethod
    def construct_class(cls, target_game: Game) -> Construct:
        return BMSEM
