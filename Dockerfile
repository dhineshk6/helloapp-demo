# Use the official nginx image as the base
FROM nginx:alpine

# Copy the static HTML file to the nginx html directory
COPY index.html /usr/share/nginx/html/

# Expose port 80 for HTTP traffic
EXPOSE 80
