# **📊 OpenTelemetry Collector com Kubernetes & Python**

Este guia descreve como executar sua aplicação Python junto ao OpenTelemetry Collector no Kubernetes, aproveitando o Docker Compose para desenvolvimento local. Adicionalmente, abordaremos a configuração do Promtail para a integração com o Loki no Grafana.

## **Pré-requisitos**

- Docker e Docker Compose instalados.
- kubectl instalado e configurado para interagir com seu cluster Kubernetes.
- Uma conta no Grafana para obter as credenciais necessárias.

## **Configurando e Executando**

### **1. Arquivo de configuração do OpenTelemetry Collector:**

- Abra ou crie o arquivo **`otel-collector-config.yaml`** em seu diretório.
- Substitua o **`endpoint`** e o cabeçalho **`Authorization`** com suas credenciais do Grafana:

```yaml
otlp:
  endpoint: https://tempo-prod-12-prod-sa-east-0.grafana.net/tempo
  headers:
    Authorization: Basic CONVERTED_TO_BASE64 (INSTANCEID:APIKEY)
prometheusremotewrite:
  endpoint: https://INSTANCEID:APIKEY@prometheus-prod-25-prod-sa-east-0.grafana.net/api/prom/push
```

🚀 **Atenção**: Converta suas credenciais do Grafana para Base64 e use no lugar de **`CONVERTED_TO_BASE64`**. Para o **`prometheusremotewrite`**, não é necessária a conversão.

### **2. Configuração do Promtail:**

Altere a URL no arquivo de configuração do Promtail para apontar para sua instância Loki no Grafana:

```yaml
clients:
- url: https://YOUR_INSTANCE_ID:YOUR_API_KEY@logs-prod-015.grafana.net/loki/api/v1/push
```

🚀 **Atenção**: Substitua **`YOUR_API_KEY`** pela chave API correta.

## **Subindo a aplicação no Cluster Kubernetes:**

Primeiramente, crie um namespace chamado "observability":

```bash
kubectl create namespace observability
```

Em seguida, aplique as configurações necessárias para o deployment e serviço da sua aplicação:

```bash
kubectl apply -f rolldice-deployment.yaml -n observability
kubectl apply -f rolldice-service.yaml -n observability
```

Agora, configure o Promtail:

```bash
kubectl apply -f values-promtail.yaml -n observability
```

Finalmente, configure o OpenTelemetry Collector:

```bash
kubectl apply -f collector-service.yaml -n observability
kubectl apply -f collector-deployment.yaml -n observability
kubectl apply -f collector-config-map.yaml -n observabili
```

## **Usando Docker Compose:**

```bash
docker-compose up --build
```

## **Executando Localmente:**

Para rodar sua aplicação Python localmente:

```bash
python app.py
```

E para rodar o OpenTelemetry Collector localmente

```bash
otel-collector-contrib --config=otel-collector-config.yaml
```

---

Agora, sua aplicação Python estará interagindo com o OpenTelemetry Collector, o Promtail e o Loki, seja no Kubernetes ou localmente. Isso permitirá um monitoramento e logging robusto através do Grafana. Se encontrar qualquer problema ou tiver sugestões, não hesite em contribuir! 🚀