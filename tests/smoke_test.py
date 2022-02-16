from django.test import TestCase


class SmokeTest(TestCase):
    # Very basic test which verifies that the website still shows stuff
    # As the website is very basic, this should be sufficient to catch any potential
    # errors due to version upgrading
    def test_main_page(self):
        response = self.client.get("/")

        # Check page succesfully loads
        self.assertEqual(200, response.status_code)

        # Check navbar has rendered
        self.assertContains(response, "Contact")

        # Check main sections have rendered
        self.assertContains(response, "About Us")
        self.assertContains(response, "Reservation")
        self.assertContains(response, "Calendar")

        # Check footer has rendered
        self.assertContains(response, "Directions")
