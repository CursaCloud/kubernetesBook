
# 📘 Kubernetes Book - Ejemplos y Recursos Prácticos

Bienvenido al repositorio oficial de ejemplos que acompañan el libro **"Kubernetes: De los Fundamentos a la Práctica"**, publicado por **CursaCloud**.

Aquí encontrarás los archivos, manifiestos YAML y recursos necesarios para seguir los ejemplos prácticos de cada capítulo.

---

## 🚀 Sobre este Repositorio

Este proyecto está diseñado como material complementario para que puedas:

✅ Comprender conceptos básicos y avanzados de Kubernetes.  
✅ Probar y desplegar tus propios Pods, Deployments, Services y otros recursos.  
✅ Experimentar en un entorno controlado mientras avanzas en la lectura del libro.  

**Importante:** Los ejemplos están organizados por capítulos y pensados para ejecutarse en un clúster local (por ejemplo, [Minikube](https://minikube.sigs.k8s.io/) o [Kind](https://kind.sigs.k8s.io/)) o en entornos en la nube, según el nivel de complejidad.

---

## 📂 Estructura del Repositorio

```plaintext
kubernetesBook/
├── capitulo-01-introduccion/
├── capitulo-02-pods-y-containers/
├── capitulo-03-deployments-y-escalabilidad/
├── capitulo-04-services-y-networking/
├── capitulo-05-configmaps-y-secrets/
├── ...
└── README.md
```

Cada carpeta corresponde a los ejemplos prácticos de un capítulo del libro.

---

## ⚙️ Requisitos Previos

Antes de ejecutar los ejemplos:

- Tener [kubectl](https://kubernetes.io/docs/tasks/tools/) instalado.
- Disponer de un clúster de Kubernetes funcional (recomendado: Minikube o Kind).
- Conocer los conceptos básicos explicados en el libro.

---

## 📦 Ejecución de Ejemplos

Desde la carpeta correspondiente, puedes aplicar los manifiestos con:

```bash
kubectl apply -f ejemplo.yaml
```

Para verificar recursos:

```bash
kubectl get pods
kubectl get deployments
kubectl get services
```

---

## 📚 Sobre el Libro

Este repositorio acompaña el libro:

> **Kubernetes: De los Fundamentos a la Práctica**  
> Autor: CursaCloud  
> [Sitio oficial del libro próximamente]

En el libro aprenderás:

- Conceptos esenciales de Kubernetes.  
- Despliegue de aplicaciones.  
- Escalabilidad y alta disponibilidad.  
- Seguridad y configuración avanzada.  
- Casos prácticos del mundo real.  

---

## 🤝 Contribuciones

Este repositorio es público para que estudiantes y profesionales puedan:

- Probar los ejemplos.  
- Proponer mejoras o correcciones.  
- Compartir dudas y sugerencias.  

Pull Requests y Issues son bienvenidos. 🚀

---

## 📢 Licencia

Este proyecto se distribuye bajo la licencia [MIT](LICENSE).

---

**¡Gracias por ser parte de la comunidad CursaCloud!** 🌐
