from tests import JSON_TINGLI, ChineseWordDetail, WordTranslation, ChineseWordDetailV2

class TestTingli:

    def test_tingli(self):
        tingli: list[ChineseWordDetail] = list(ChineseWordDetail.loads(JSON_TINGLI, many=True))
        assert isinstance(tingli[0].translations, list) is True
        assert isinstance(tingli[0].translations[0], WordTranslation) is True

    def test_tingli_v2(self):
        tingli: list[ChineseWordDetailV2] = list(ChineseWordDetailV2.loads(JSON_TINGLI, many=True))
        assert isinstance(tingli[0].translations, list) is True
        print(tingli[0].translations[0], type(tingli[0].translations[0]))
        assert isinstance(tingli[0].translations[0], WordTranslation) is True
