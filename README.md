# 🧠 Detección de Tumores Cerebrales con MRI

<p align="center">
  <img src="recursos/demo.gif" alt="Demo de la aplicación" width="700"/>
</p>

Aplicación web con **Flask** para el análisis y visualización de imágenes de resonancia magnética (MRI) cerebral, orientada a la detección de tumores sobre el dataset TCGA.

---

## ✨ Características

| Función | Descripción |
|---|---|
| 📊 Estadísticas | Métricas del dataset con gráficos interactivos |
| 🖼️ Galería | MRI originales, máscaras y superposiciones |
| 🔍 Análisis detallado | 12 casos con visualización completa |
| 🔄 Actualización dinámica | Nuevas muestras aleatorias con un clic |
| 📱 Diseño responsivo | Interfaz adaptable a cualquier dispositivo |

## 🛠️ Tecnologías

- **Backend**: Python · Flask · Pandas · NumPy
- **Visión artificial**: OpenCV · scikit-image · Pillow
- **Frontend**: HTML5 · CSS3 · JavaScript
- **Despliegue**: Render

## 🚀 Instalación local

```bash
# 1. Clonar el repositorio
git clone https://github.com/Adrian-HI-LO/Tumores-Cerebreles-MRI.git
cd Tumores-Cerebreles-MRI

# 2. Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar
python app.py
```

Abre `http://localhost:5000` en tu navegador.

> **Requisito**: asegúrate de contar con `Brain_MRI/data_mask.csv` y las imágenes del dataset en la carpeta correspondiente.

## 📁 Estructura

```
Tumores-Cerebreles-MRI/
├── app.py                  # Aplicación Flask principal
├── data_processor.py       # Procesamiento de imágenes y datos
├── requirements.txt        # Dependencias
├── Brain_MRI/              # Dataset (imágenes + data_mask.csv)
├── templates/index.html    # Interfaz principal
└── static/                 # CSS, JS e imágenes generadas
```

## 🌐 Despliegue en Render

1. Sube el proyecto a GitHub y conéctalo en [Render.com](https://render.com).
2. Crea un **Web Service** con la siguiente configuración:
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
3. Haz clic en **Create Web Service** y espera ~5 minutos.

## 📊 Dataset

Dataset **TCGA** de imágenes MRI cerebrales:

- Total: **3 929 imágenes**
- Con tumor: **1 373** (34.95 %)
- Sin tumor: **2 556** (65.05 %)

---

<p align="center">
  ⭐ Si te resulta útil, dale una estrella en GitHub
</p>
