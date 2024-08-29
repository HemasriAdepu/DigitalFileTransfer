from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Member, File
from django.urls import reverse

class MemberModelTest(TestCase):
    
    def setUp(self):
        # Create test data
        self.user = User.objects.create_user(username='alice', password='password123')
        self.member = Member.objects.create(
            user=self.user,
            name='Bob',
            family_name='Smith',
            phone_number='1234567890',
            email='bob@example.com',
            relation_to_owner='Friend',
            question1='First pet?',
            answer1='Fluffy',
            question2='Mother\'s maiden name?',
            answer2='Smith',
            question3='Favorite color?',
            answer3='Blue'
        )
    
    def test_member_creation(self):
        """Test that a Member instance is created correctly"""
        self.assertEqual(self.member.name, 'Bob')
        self.assertEqual(self.member.phone_number, '1234567890')
        self.assertEqual(self.member.email, 'bob@example.com')
    
    def test_member_str(self):
        """Test the string representation of the Member"""
        self.assertEqual(str(self.member), 'Bob')
    
    def test_registration_view(self):
        """Test the registration view for members"""
        response = self.client.post(reverse('register_member'), {
            'name': 'Charlie',
            'family_name': 'Brown',
            'phone_number': '0987654321',
            'email': 'charlie@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Registration successful')
    
    def test_upload_file_view(self):
        """Test file upload view"""
        self.client.login(username='alice', password='password123')
        response = self.client.post(reverse('upload_file'), {
            'file': SimpleUploadedFile('testfile.txt', b'This is a test file.')
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'File uploaded successfully')

    def test_member_access_files(self):
        """Test access to files for members"""
        # Create a member who will be used to test file access
        self.member = Member.objects.create(
            user=self.user,
            name='Bob',
            family_name='Smith',
            phone_number='1234567890',
            email='bob@example.com',
            relation_to_owner='Friend',
            question1='First pet?',
            answer1='Fluffy',
            question2='Mother\'s maiden name?',
            answer2='Smith',
            question3='Favorite color?',
            answer3='Blue'
        )
        self.client.login(username='alice', password='password123')
        response = self.client.get(reverse('access_files'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Access files')
