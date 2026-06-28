# Kubernetes

## Validate YAML
python -c "import yaml,glob; [list(yaml.safe_load_all(open(f))) for f in glob.glob('infra/kubernetes/*.yaml')]; print('YAML OK')"

## Apply later on cluster
kubectl apply -f infra/kubernetes/