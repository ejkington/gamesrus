"""
bag/test_views.py: testing of views in bag app.
functionality for it. Largely guided by project:
https://github.com/johnvenkiah/CI_PP5_John_Venkiah
"""

from django.contrib.messages import get_messages
from django.test import TestCase

from products.models import Product


class TestBagViews(TestCase):
    """
    Testing of bag views
    """
    def setUp(self):
        """
        Create a test product
        """
        # pylint: disable=no-member
        Product.objects.create(
            art_nr='999',
            name='Test Name',
            price='99.99',
            description='This is a description of the product',
        )

    def tearDown(self):
        """
        Delete test products
        """
        Product.objects.all().delete()  # pylint: disable=no-member

    def test_show_bag_page(self):
        """
        Tests that the bag page is displayed
        """
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_empty_bag(self):
        """
        Tests adding a product to an empty bag
        """
        # pylint: disable=no-member
        product = Product.objects.get(art_nr='999')
        response = self.client.post(f'/bag/add/{product.id}/', {
                'quantity': 1,
                'redirect_url': 'view_bag'
            }
        )
        bag = self.client.session['bag']
        self.assertEqual(bag[str(product.id)], 1)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Added Test Name to your bag')

    def test_update_item_quantity_to_two(self):
        """
        Tests updating bag item quantity to 2
        """
        # pylint: disable=no-member
        product = Product.objects.get(art_nr='999')
        response = self.client.post(f'/bag/update/{product.id}/', {
            'quantity': 2
        })
        bag = self.client.session['bag']
        self.assertEqual(bag[str(product.id)], 2)
        messages = list(get_messages(response.wsgi_request))
        product_id = bag[str(product.id)]
        self.assertEqual(
            str(messages[0]), (
                f'Updated Test Name quantity to {str(product_id)}'
            )
        )

    def test_update_bag_quantity_to_zero(self):
        """
        Tests updating the bag item quantity from 1 to 0
        """
        # pylint: disable=no-member
        product = Product.objects.get(art_nr='999')
        response = self.client.post(f'/bag/add/{product.id}/', {
            'quantity': 1, 'redirect_url': 'view_bag',
        })
        self.assertRedirects(response, '/bag/')
        bag = self.client.session['bag']
        self.assertEqual(bag[str(product.id)], 1)
        response = self.client.post(f'/bag/update/{product.id}/', {
            'quantity': 0, 'redirect_url': 'view_bag',
        })
        self.assertRedirects(response, '/bag/')
        bag = self.client.session['bag']
        self.assertEqual(bag, {})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Removed Test Name from your bag')
