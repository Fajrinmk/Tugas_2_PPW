# from django.test import TestCase
# from django.test import Client
# from django.urls import resolve
# from datetime import datetime, date
# from .views import index, profile_name,birthdate,gender,email,desc_profile,expert
# import unittest
# from .models import DataProfile

# # Create your tests here.
# class HalamanProfileUnitTest(TestCase):
#     def setUp(self):
#         Profile = DataProfile(name= profile_name, birthday = birthdate, gender = gender,expertise = expert, email = email, description = desc_profile, id = 1 )
#         Profile.save()     
    
#     def test_name_is_exist(self):
#         response = Client().get('/halaman_profile/')
#         self.assertEqual(response.status_code,200)

#     def test_using_index_func(self):
#         found = resolve('/halaman_profile/')
#         self.assertEqual(found.func, index)

#     def test_all_profile_is_exist(self):
#         #to check whether name is not none
#         self.assertIsNotNone(profile_name)
#         self.assertIsNotNone(birthdate)
#         self.assertIsNotNone(gender)
#         self.assertIsNotNone(email)

#     def test_description_is_written(self):
#         #check whether there is any description
#         self.assertIsNotNone(desc_profile)

#         #the description is filled with 20 characters at least
#         self.assertTrue(len(desc_profile) >= 20)

#     def test_expertise_is_more_than_3(self):
#         self.assertTrue(len(expert) >= 3)


# from django.test import TestCase
# from django.test import Client

# # Create your tests here.
# class PageRiwayatUnitTest(TestCase):
#     def test_page_profile_url_is_exist(self):
#     	response = Client().get('/page_profile/')
#     	self.assertEqual(response.status_code, 200)


    

    
