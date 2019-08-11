import stk
import pytest


@pytest.fixture
def tmp_macrocycle(tmp_bromine2, tmp_bromine2_alt1):
    return stk.ConstructedMolecule(
        building_blocks=[tmp_bromine2, tmp_bromine2_alt1],
        topology_graph=stk.macrocycle.Macrocycle('AB', [0, 0], 3)
    )
