from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, reverse_lazy

from centros_proteccion.models import RepresentanteLegal
from centros_proteccion.tests.factories.representante_legal import RepresentanteLegalFactory


class RepresentanteLegalViewTest(TestCase):
    def setUp(self):
        self.test_user_1 = get_user_model().objects.create_user(
            email='random_mail@correo.com',
            password='testpass123'
        )
        self.test_user_1.save()
        num_representantes = 13
        for representante in range(num_representantes):
            foo = RepresentanteLegalFactory.create(usuario_registro=self.test_user_1)
            print(foo.muni_residencia.codigo)
        self.client.login(email='random_mail@correo.com', password='testpass123')

    def test_cantidad_correcta(self):
        self.assertEqual(RepresentanteLegal.objects.count(), 13)

    def test_list_view(self):

        resp = self.client.get(reverse('representante_legal_list'))

        self.assertTrue(resp.context['is_paginated'])
        self.assertEqual(resp.context['paginator'].per_page, 5)
        self.assertEqual(len(resp.context['representantes_legales']), 5)
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(reverse('representante_legal_list') + '?page=3')
        self.assertEqual(len(resp.context['representantes_legales']), 3)


