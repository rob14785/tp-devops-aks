import pytest
from calendrier import est_bissextile


@pytest.mark.parametrize("annee", [2004, 2024, 2000, 1600])
def test_annees_bissextiles(annee):
    assert est_bissextile(annee) is True


@pytest.mark.parametrize("annee", [2009, 2017, 1900, 2100])
def test_annees_non_bissextiles(annee):
    assert est_bissextile(annee) is False
