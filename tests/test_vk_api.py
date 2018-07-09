from tests import JSON_VK, WallResponse


class TestVK:
    def test_simple(self):
        vk: WallResponse = WallResponse.loads(JSON_VK)
        assert vk.count == 578
        assert list(list(vk.items)[0].attachments)[0].type == 'photo'
