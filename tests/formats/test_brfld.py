from tests.test_lib import parse_and_build_compare

from mercury_engine_data_structures.formats.brfld import BRFLD
from mercury_engine_data_structures.game_check import Game


def test_compare_dread(dread_path):
    parse_and_build_compare(
        BRFLD, Game.DREAD, dread_path.joinpath("packs/maps/s090_skybase/s090_skybase.brfld")
    )
