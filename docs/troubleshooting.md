# Kubernetes Troubleshooting Guide

## CrashLoopBackOff

### Debug
kubectl get pods
kubectl describe pod <pod-name>
kubectl logs <pod-name>

### Root Cause
Container starts and exits repeatedly.

### Fix
Check container command, app startup, environment variables, and logs.

---

## ImagePullBackOff

### Debug
kubectl get pods
kubectl describe pod <pod-name>

### Root Cause
Kubernetes cannot pull the container image.

### Fix
Check image name, tag, registry access, and imagePullSecrets.

---

## OOMKilled

### Debug
kubectl describe pod <pod-name>
kubectl top pod

### Root Cause
Container exceeded memory limit.

### Fix
Increase memory limit or reduce application memory usage.