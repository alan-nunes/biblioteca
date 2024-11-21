from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from core.models import Colecao

# Create your tests here.

class ColecaoTests(APITestCase):
    def setUp(self):
        Colecao.objects.all().delete()  # Limpa todas as coleções antes de rodar o teste
        User.objects.all().delete()  # Também limpa os usuários para garantir um banco de dados limpo
        
        # Criar usuários para os testes
        self.user = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password456')

        # Autenticação do primeiro usuário
        self.client.login(username='user1', password='password123')

        # Criar coleções associadas aos usuários
        self.colecao = Colecao.objects.create(nome='Ficção Científica', colecionador=self.user)
        self.colecao2 = Colecao.objects.create(nome='História', colecionador=self.user)
        #self.colecao3 = Colecao.objects.create(nome='Filosofia', colecionador=self.user2)  # Coleção de outro usuário

    
    def test_criar_colecao(self):
        data = {'nome': 'Filosofia',
                'colecionador': self.user.id, # Passando o ID do usuário autenticado
            }
        response = self.client.post('/api/colecao/', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Colecao.objects.count(), 1)
        self.assertEqual(Colecao.objects.last().colecionador, self.user)
    
    def test_editar_colecao_apenas_proprietario(self):
        # Tentar editar a coleção como outro usuário
        self.client.logout()    # Garante que o usuário esteja desautenticado
        self.client.login(username='user2', password='password456')

        data = {'nome': 'Ficção Atualizada'}
        response = self.client.put(f'/api/colecao/{self.colecao.id}/', data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_deletar_colecao_apenas_proprietario(self):
        # Tentar deletar a coleção como outro usuário
        self.client.logout()
        self.client.login(username='user2', password='password456')

        response = self.client.delete(f'/api/colecao/{self.colecao.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_criar_colecao_usuario_nao_autenticado(self):
        # Tentar criar uma coleção sem autenticação
        self.client.logout()    # Garante que o usuário esteja desautenticado
        data = {'nome': 'História'}
        response = self.client.post('/api/colecao/', data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    
    def test_listar_colecoes_usuario_autenticado(self):
        
        #Colecao.objects.create(nome='Romance', colecionador=self.user)
        
        response = self.client.get('/api/colecao/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
        # Verificar se as coleções retornadas são de fato do usuário autenticado
       # self.assertEqual(response.data[0]['nome'], 'Romance')
       

    def test_listar_colecoes_usuario_nao_autenticado(self):
        self.client.logout()    # Garante que o usuário esteja desautenticado
        response = self.client.get('/api/colecao/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
