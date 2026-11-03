import httpx2
import pytest

from fh_bits.css import blades, bulma, daisy, web_awesome

def test_get_blades():
    blades_url = blades.headers.href
    assert httpx2.get(blades_url).is_success

def test_get_bulma():
    bulma_url = bulma.headers.href
    assert httpx2.get(bulma_url).is_success

def test_get_daisy():
    daisy_gets = [
        httpx2.get((h.href or h.src)).is_success for h in daisy.headers
    ]
    assert all(daisy_gets)
def test_get_web_awesome():
    wa_gets = [
        httpx2.get((h.href or h.src)).is_success for h in web_awesome.headers
    ]
    assert all(wa_gets)
