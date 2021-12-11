from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from products.models import Product, Brand, Category


@registry.register_document
class ProductDocument(Document):
    class Index:
        name = "products"

        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Product

        fields = [
            'name',
            'description',
            'origin_country'
        ]


@registry.register_document
class BrandDocument(Document):
    class Index:
        name = 'brands'

        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Brand

        fields = [
            'name',
            'is_premium'
        ]


@registry.register_document
class CategoryDocument(Document):
    class Index:
        name = 'categories'

    class Django:
        model = Category

        fields = [
            'name',
            'displayed'
        ]
