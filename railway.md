# Deploy en Railway usando Docker

Pasos rápidos para desplegar este bot en Railway usando el Dockerfile incluido:

1. Asegúrate de tener el repositorio con este código en GitHub (o conecta tu repo a Railway).
2. En Railway crea un nuevo proyecto y elige "Deploy from GitHub" o "Deploy with Docker".
3. Si usas el Dockerfile incluido, Railway construirá la imagen automáticamente.
4. Añade una Environment Variable (Secret) llamada `DISCORD_TOKEN` con el token de tu bot.
5. Verifica que Railway esté usando la variable `PORT` (Railway suele inyectarla automáticamente). El contenedor expone el puerto 8000 y respeta la variable `PORT` en `keep_alive.py`.
6. Despliega y revisa los logs. Si la health check falla, revisa que la ruta `/` devuelva 200 (el código ya incluye un fallback HTTP server que responde 200 en `/`).

Notas:
- Si el deployment falla en la instalación de dependencias, revisa los logs de build para ver errores de pip o paquetes nativos faltantes. Puedes añadir dependencias del sistema al Dockerfile si hace falta.
- Nunca subas tu `DISCORD_TOKEN` al repo; usa los Secrets/Environment Variables de Railway.
