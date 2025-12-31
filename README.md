# Deploy en Replit

Instrucciones rápidas para hospedar este bot en Replit:

1. Crea un nuevo Repl (Python) y sube estos archivos.
2. En Replit, ve a la sección "Secrets" (o Environment Variables) y añade la clave `DISCORD_TOKEN` con el token de tu bot.
   - No subas ni pegues el token en el código fuente.
3. El archivo `.replit` ya está configurado para ejecutar `main.py`.
4. Asegúrate de que `requirements.txt` incluya las dependencias (ya se añadió `Flask` y `python-dotenv`). Replit instalará las dependencias automáticamente.
5. Pulsa Run. El servidor Flask sirve una ruta en `/` para mantener el repl despierto (útil junto con uptime monitors).

Notas:
- Para desarrollo local puedes copiar `.env.template` a `.env` y añadir `DISCORD_TOKEN=tu_token`.
- Nunca comites tu token ni lo compartas públicamente.
# tulio-albeiro
