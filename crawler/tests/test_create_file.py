from os import write
from crawler.create_file import write_json
import pytest
import json

@pytest.mark.parametrize('original_dict', [
    {'hello': '안녕'},
    {'array': ['string', 'abc'], 'number': 12345}
])
def test_write_json(tmp_path, original_dict):
    directory = tmp_path / 'json/'
    directory.mkdir()

    write_json(original_dict, str(tmp_path) + '/json/test.json')
    file = directory / 'test.json'
    saved_json = file.read_text().encode().decode('utf-8-sig')
    saved_dict = json.loads(saved_json)

    assert saved_dict == original_dict