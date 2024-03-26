from rest_framework import serializers
from product.models import Product, Category, Review


def validate_name_max_length(value, max_length):
    if len(value) > max_length:
        raise serializers.ValidationError(f"Max length for {value} is 50 characters")
    return value


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_text(self, value):
        validate_name_max_length(value, 300)


class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_products_count(self, obj):
        return obj.products.count()

    def validate_name(self, value):
        validate_name_max_length(value, 50)


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'.split()

    def validate_title(self, value):
        validate_name_max_length(value, 100)


class Product2Serializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_average_rating(self, obj):
        total_stars = sum(review.stars for review in obj.reviews.all())
        num_reviews = obj.reviews.count()
        if num_reviews > 0:
            return total_stars/num_reviews
        else:
            return 0.0
