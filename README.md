# Duke University API Examples

This repository provides a collection of example scripts and code snippets for interacting with the Duke University APIs. These examples demonstrate various use cases, making it easier to understand how to consume the API endpoints, handle data, and integrate them into applications.

## Table of Contents

- [Getting Started](#getting-started)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)

## Getting Started

These examples assume you have an active user for Duke University APIs. You can typically obtain an user by registering with [Duke University’s Atlas portal](https://sdoh.duhs.duke.edu/).

## Setup and Installation

### Prerequisites

- Python (>= 3.10)

### Python Setup

1. Clone the repository:

    ```bash
    git clone git@github.com:duke-university-amplifilabs/api-examples.git
    cd api-examples
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables (you can store your API key in a `.env` file in the root directory):

    ```bash
    DUKE_API_USERNAME=your_email
    DUKE_API_PASSWORD=your_password
    ```

## Usage

To run an example, navigate to src dir and execute the following commando

```bash
python -m examples.query_measure_data
```

