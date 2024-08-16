# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Expose the port your application will run on
EXPOSE 8000

# Run migrations and collect static files
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Define environment variable
ENV DJANGO_SETTINGS_MODULE=Courses.settings

# Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Courses.wsgi:application"]
