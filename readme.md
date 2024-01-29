## Microsserviço Python para Extração de Entidades Nomeadas (NER)

### Estrutura do Projeto
```
ner_extractor_svc/
│
├── src/
│   └── main.py
│
├── tests/
│   └── test_app.py
│
├── .gitignore
├── deployment.yaml
├── Dockerfile
├── readme.md
├── requirements.txt
└── service.yaml
```

### Pré-requisitos
1. **Preparação**:
   - Certifique-se de que o Minikube esteja instalado e configurado corretamente em sua máquina local. Você pode iniciar o Minikube com o comando `minikube start`.
   - Certifique-se de que sua imagem do Docker esteja construída corretamente e esteja disponível. Se você estiver usando apenas o Minikube e não tiver um registro Docker privado, pode ser útil usar o ambiente Docker do Minikube para construir suas imagens, garantindo que elas estejam disponíveis para o Minikube. Você pode configurar isso com `eval $(minikube -p minikube docker-env)` antes de construir sua imagem Docker.

### Construindo a Imagem Docker

A partir da raiz do projeto, executar o comando:

```bash
eval $(minikube -p minikube docker-env) #Trabalhando com imagem local
docker build -t ner_extractor_svc .
```

### Executando o Contêiner

Para fazer o deploy no Minikube:

#### Executando o Deployment e o Service

1. **Deploy do Microsserviço**:
   Execute o seguinte comando para criar o Deployment no Kubernetes:

   ```bash
   kubectl apply -f deployment.yaml
   ```

2. **Criação do Service**:
   Execute o seguinte comando para criar o Service e expor seu microsserviço:

   ```bash
   kubectl apply -f service.yaml
   ```

3. **Verificando o Estado (opcional)**:
   Você pode verificar o estado do Deployment e do Service usando:

   ```bash
   kubectl get deployments
   kubectl get services
   kubectl get pods -l app=ner-extractor
   kubectl logs <nome-do-pod>
   ```

4. **Acesso ao Microsserviço**:
   - Com o Service do tipo `NodePort`, você pode acessar seu microsserviço fora do cluster Minikube. Para encontrar a URL que você pode usar para acessar o serviço, execute:

     ```bash
     minikube service ner-extractor-svc --url
     ```

     Isso fornecerá a URL que você pode usar para acessar seu microsserviço.

Isso mapeia a porta 8000 do host para a porta 80 do contêiner, permitindo que você acesse o microsserviço através de `http://{IP_HOST}:8000`.

### Testando o Serviço
   Após iniciar o servidor, você pode testar o serviço usando ferramentas como `curl`, Postman ou diretamente através do navegador acessando a documentação interativa gerada pelo FastAPI (`http://{IP_HOST}:8000/docs`).

   Exemplo de requisição `curl` a partir da máquina local:

   ```bash
   curl -X 'POST' \
     'http://127.0.0.1:8000/extrair-entidades/' \
     -H 'accept: application/json' \
     -H 'Content-Type: application/json' \
     -d '{
     "texto": "João da Silva mora em São Paulo - SP, na Avenida das Araucárias, Centro.",
     "labels": ["PER", "LOC"]
   }'
   ```

 Dependendo do modelo do Spacy escolhido, os tipos de entidades disponíveis podem variar, então ajuste os parâmetros e o código conforme necessário.

### Excluindo o deployment
  ```bash
  kubectl delete deployment ner-extractor-svc
  ```

Kubernetes v1.28.3 on Docker 24.0.7