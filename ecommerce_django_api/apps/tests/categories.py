from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.product.models import Category


class CategoryViewSetTest(APITestCase):
    def setUp(self):
        self.apple = Category.objects.create(name='apple')
        self.sony = Category.objects.create(name='sony')
        self.huawei = Category.objects.create(name='huawei')
        self.dell = Category.objects.create(name='dell')

    def test_list_categories_with_pagination(self):
        url = reverse('category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 3)  # Checking page size
        self.assertEqual(Category.objects.all().count(), 4)

    def test_retrieve_category(self):
        apple_url = reverse("category-detail", kwargs={"pk": self.apple.uuid})
        response = self.client.get(apple_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), self.apple.name)
        self.assertEqual(f"{self.apple.uuid}", response.data.get("uuid"))

    def test_create_category(self):
        url = reverse("category-list")
        response = self.client.post(url, data={"name": "samsung"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("name"), "samsung")
        self.assertEqual(Category.objects.count(), 5)

    def test_update_category(self):
        url = reverse("category-detail", kwargs={"pk": self.sony.uuid})
        response = self.client.put(url, data={"name": "Sony 2023"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), "Sony 2023")
        self.assertEqual(response.data.get("uuid"), f"{self.sony.uuid}")

    def test_delete_category(self):
        huawei_url = reverse("category-detail", kwargs={"pk": self.huawei.uuid})
        response = self.client.delete(huawei_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 3)