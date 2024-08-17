# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Set the working directory to the directory containing manage.py
WORKDIR /app/Courses

# Expose the port your application will run on
# EXPOSE 8000

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=Courses.settings

# Run migrations and collect static files
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Command to run the application
CMD ["python3", "manage.py", "runserver","0.0.0.0:8000"]
