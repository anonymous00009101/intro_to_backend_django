from django.test import TestCase
from django.urls import reverse
from .models import Todo
from django.contrib.auth.models import User

class TodoModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.todo = Todo.objects.create(
            title='Test Todo',
            description='This is a test todo',
            due_date='2023-12-31',
            status=False,
            user=self.user
        )

    def test_todo_creation(self):
        self.assertEqual(self.todo.title, 'Test Todo')
        self.assertEqual(self.todo.description, 'This is a test todo')
        self.assertEqual(self.todo.due_date.strftime('%Y-%m-%d'), '2023-12-31')
        self.assertFalse(self.todo.status)
        self.assertEqual(self.todo.user.username, 'testuser')

class TodoViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_todo_list_view(self):
        response = self.client.get(reverse('todos:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todos/index.html')

    def test_todo_create_view(self):
        response = self.client.post(reverse('todos:create'), {
            'title': 'New Todo',
            'description': 'New todo description',
            'due_date': '2023-12-31',
            'status': False
        })
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertTrue(Todo.objects.filter(title='New Todo').exists())

    def test_todo_delete_view(self):
        todo = Todo.objects.create(
            title='Todo to delete',
            description='This todo will be deleted',
            due_date='2023-12-31',
            status=False,
            user=self.user
        )
        response = self.client.delete(reverse('todos:delete', args=[todo.id]))
        self.assertEqual(response.status_code, 204)  # No content on successful delete
        self.assertFalse(Todo.objects.filter(id=todo.id).exists())