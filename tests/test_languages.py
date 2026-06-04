from nllw.languages import (
    convert_to_nllb_code,
    get_language_info,
    get_language_name_by_language_code,
    get_nllb_code,
    normalize_language_identifier,
)


def test_chinese_aliases_resolve_to_nllb_codes():
    assert normalize_language_identifier("zh") == "zh-CN"
    assert normalize_language_identifier("zh_Hans") == "zh-CN"
    assert normalize_language_identifier("zh-Hant") == "zh-TW"

    assert convert_to_nllb_code("zh") == "zho_Hans"
    assert convert_to_nllb_code("zh-Hans") == "zho_Hans"
    assert convert_to_nllb_code("zh-Hant") == "zho_Hant"

    assert get_nllb_code("zh") == "zho_Hans"
    assert get_language_name_by_language_code("zh") == "Chinese (Simplified)"
    assert get_language_info("zh")["language_code"] == "zh-CN"


def test_existing_language_identifiers_still_resolve():
    assert normalize_language_identifier("eng_Latn") == "eng_Latn"
    assert convert_to_nllb_code("eng_Latn") == "eng_Latn"
    assert convert_to_nllb_code("en") == "eng_Latn"
    assert convert_to_nllb_code("auto") == "auto"
    assert convert_to_nllb_code(None) is None
