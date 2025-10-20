from tests import (JSON_TINGLI, JOIN_PROFILE, ChineseWordDetail, WordTranslation, 
                   ChineseWordDetailV3, ChineseWordDetailV2, Profile, ProfileV2, ProfileV3)

class TestTingli:

    def test_tingli(self):
        tingli: list[ChineseWordDetail] = list(ChineseWordDetail.loads(JSON_TINGLI, many=True))
        assert isinstance(tingli[0].translations, list) is True
        assert isinstance(tingli[0].translations[0], WordTranslation) is True

    def test_tingli_v2(self):
        tingli: list[ChineseWordDetailV2] = list(ChineseWordDetailV2.loads(JSON_TINGLI, many=True))
        assert isinstance(tingli[0].translations, list) is True
        assert isinstance(tingli[0].translations[0], WordTranslation) is True

    def test_tingli_v3(self):
        tingli: list[ChineseWordDetailV3] = list(ChineseWordDetailV3.loads(JSON_TINGLI, many=True))
        assert isinstance(tingli[0].translations, list) is True
        assert isinstance(tingli[0].translations[0], WordTranslation) is True

    def test_profile(self):
        profile: Profile = Profile.loads(JOIN_PROFILE)
        assert profile.working_time == {'monday': [['12:00', '13:00']]}

    def test_profile_v2(self):
        profile: ProfileV2 = ProfileV2.loads(JOIN_PROFILE)
        assert profile.working_time == {'monday': [['12:00', '13:00']]}

    def test_profile_v2(self):
        profile: ProfileV3 = ProfileV3.loads(JOIN_PROFILE)
        assert profile.working_time == {'monday': [['12:00', '13:00']]}
