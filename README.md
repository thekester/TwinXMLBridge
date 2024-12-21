# TwinXML Bridge

TwinXML Bridge is a project facilitating the exchange of XML data between two network blocks, with validation via XSD, Jinja2 template generation, and integration of Docker and CI/CD.

## Features

- **Interchangeable Client and Server**: Blocks can act as client or server as needed.
- **XML Validation via XSD**: Ensures data conformity.
- **Jinja2 Templates**: Flexible generation of XML requests and responses.
- **Factories**: Dynamic creation of requests and responses.
- **Dockerization**: Easy deployment with Docker and Docker Compose.
- **CI/CD**: Automated pipeline with GitHub Actions.

## Installation

### Prerequisites

- **Python 3.9+**: Ensure you have Python installed. You can download it from [here](https://www.python.org/downloads/).
- **Docker**: Install Docker from [here](https://www.docker.com/).
- **Docker Compose**: Typically included with Docker Desktop, but verify installation [here](https://docs.docker.com/compose/install/).

### Clone the Repository

```bash
git clone https://github.com/yourusername/twinxml_bridge.git
cd twinxml_bridge
```

### Install Python Dependencies

It’s recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install --upgrade pip
pip install -r requirements.txt
```

## Usage

### Running with Python

#### Start the Server

```bash
python server/twinxml_server.py
```

#### Use the Client

```bash
python client/twinxml_client.py
```

### Running with Docker

Using Docker allows for easier deployment and environment consistency. Below are the steps to build and run the project using Docker.

#### 1. Build Docker Images

Build both the client and server Docker images using Docker Compose:

```bash
docker-compose build
```

#### 2. Start Services

Start the server and client containers:

```bash
docker-compose up
```

This command will:

- Build the Docker images if they haven’t been built already.
- Start the server and client containers.
- Stream the logs to your terminal.

#### 3. Running in Detached Mode

To run the containers in the background, use the `-d` flag:

```bash
docker-compose up -d
```

#### 4. Stopping Services

To stop the running containers, execute:

```bash
docker-compose down
```

This command stops and removes the containers, networks, and volumes defined in the `docker-compose.yml`.

#### 5. Viewing Logs

To view the logs of all services:

```bash
docker-compose logs
```

To view logs for a specific service (e.g., server):

```bash
docker-compose logs server
```

#### 6. Rebuilding Images

If you make changes to the Dockerfiles or the application code, rebuild the images:

```bash
docker-compose up --build
```

#### 7. Accessing Individual Containers

If you need to run commands inside a specific container, use `docker exec`. For example, to access the server container’s shell:

1. First, find the container ID or name:

    ```bash
    docker ps
    ```

2. Then, execute a shell inside the container:

    ```bash
    docker exec -it twinxml_bridge_server_1 /bin/bash
    ```

    Replace `twinxml_bridge_server_1` with your actual server container name.

### Using Docker Commands Directly

Alternatively, you can manage the Docker containers without Docker Compose using the following commands:

#### Building Images

```bash
# Build server image
docker build -t twinxml_bridge_server -f docker/Dockerfile.server .

# Build client image
docker build -t twinxml_bridge_client -f docker/Dockerfile.client .
```

#### Running Containers

```bash
# Run server
docker run -d --name twinxml_bridge_server -p 5000:5000 twinxml_bridge_server

# Run client
docker run -d --name twinxml_bridge_client twinxml_bridge_client
```

#### Stopping and Removing Containers

```bash
docker stop twinxml_bridge_server twinxml_bridge_client
docker rm twinxml_bridge_server twinxml_bridge_client
```

#### Viewing Logs

```bash
docker logs twinxml_bridge_server
docker logs twinxml_bridge_client
```

## Continuous Integration and Deployment (CI/CD)

This project uses GitHub Actions to automate testing, building, and deploying Docker images.

### GitHub Actions Workflow

The workflow is defined in `.github/workflows/ci.yml` and includes the following steps:

1. **Checkout Code**: Retrieves the latest code from the repository.
2. **Set up Python**: Sets up the specified Python version.
3. **Install Dependencies**: Installs the required Python packages.
4. **Linting**: Checks the code for style issues using `flake8`.
5. **Run Tests**: Placeholder for running tests.
6. **Build Docker Images**: Builds the Docker images using Docker Compose.
7. **Push to Docker Hub**: Pushes the built images to Docker Hub (only on the `main` branch).

### Configuring GitHub Secrets

To enable pushing Docker images, add the following secrets to your GitHub repository:

- `DOCKER_USERNAME`: Your Docker Hub username.
- `DOCKER_PASSWORD`: Your Docker Hub password. (https://app.docker.com/settings/personal-access-tokens/create)

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**: Click the "Fork" button on the GitHub repository page.

2. **Clone Your Fork**:

    ```bash
    git clone https://github.com/yourusername/twinxml_bridge.git
    cd twinxml_bridge
    ```

3. **Create a Branch**:

    ```bash
    git checkout -b feature/your-feature-name
    ```

4. **Make Changes**: Implement your feature or bug fix.

5. **Commit Changes**:

    ```bash
    git commit -m "Add feature X"
    ```

6. **Push to Your Fork**:

    ```bash
    git push origin feature/your-feature-name
    ```

7. **Create a Pull Request**: Go to the original repository and create a pull request from your fork.

### License
This project is licensed under the [MIT License](LICENSE). See the LICENSE file for details.
