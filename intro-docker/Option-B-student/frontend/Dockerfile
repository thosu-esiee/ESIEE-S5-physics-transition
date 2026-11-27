# TODO: Base image nginx:stable-alpine.
# TODO: Copy the supplied frontend files into /usr/share/nginx/html.
# TODO: Copy default.conf to /etc/nginx/conf.d/default.conf.
# Optional: EXPOSE 80 (documentary only).

FROM nginx:stable-alpine
COPY index.html style.css app.js /usr/share/nginx/html/
COPY default.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
