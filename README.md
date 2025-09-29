# SIH FHIR Terminology Service

A lightweight micro-service designed for the Smart India Hackathon (SIH) to facilitate interoperability in Ayush EMR systems. This project focuses on ingesting NAMASTE codes, synchronizing with ICD-11 (TM2 and Biomedicine), enabling dual-coding, and ensuring compliance with FHIR R4 standards aligned with India's 2016 EHR Standards.

## Overview

The SIH FHIR Terminology Service acts as a bridge between traditional Ayush medical terminologies (NAMASTE) and modern international standards (ICD-11). By providing a modular, RESTful API, it enables seamless dual-coding for electronic health records, promoting data interoperability and standardization in India's healthcare ecosystem.

This MVP prioritizes core functionalities while maintaining a scalable architecture for future enhancements.

## Key Features

- **Data Ingestion**: Automated loading of NAMASTE CSV files and real-time fetching of ICD-11 data.
- **Terminology Management**: Robust handling of CodeSystems, ConceptMaps, and translations between terminologies.
- **Dual-Coding Support**: Enables mapping and translation between NAMASTE and ICD-11 codes.
- **FHIR R4 Compliance**: Adheres to FHIR R4 specifications and India's 2016 EHR Standards.
- **RESTful API**: Provides endpoints for code lookups, translations, and data uploads.
- **Basic UI/CLI**: Simple interface for testing and demonstration purposes.
- **Security & Compliance**: Implements OAuth authentication, audit logging, and standards adherence.

## Architecture

The service is built as a modular micro-service with the following components:

### 1. Data Ingestion Layer
- Handles CSV parsing for NAMASTE codes.
- Integrates with ICD-11 APIs for data synchronization.
- Supports batch and incremental updates.

### 2. Terminology Service
- Manages FHIR CodeSystems for NAMASTE and ICD-11.
- Creates and maintains ConceptMaps for terminology mappings.
- Provides translation logic for dual-coding scenarios.

### 3. API Endpoints
- RESTful interfaces built with FastAPI (Python).
- Endpoints for:
  - Code lookups and searches.
  - Terminology translations.
  - Data uploads and synchronization.

### 4. User Interface
- Basic web interface using HTML/CSS/JavaScript for demonstrations.
- Command-line interface (CLI) for batch operations and testing.

### 5. Security and Compliance Layer
- OAuth 2.0 for authentication.
- Audit trails for all operations.
- Validation against FHIR R4 profiles and India's EHR standards.

## Installation

### Prerequisites
- Python 3.8+
- uv (recommended) or pip
- Access to ICD-11 API (requires API key - contact WHO for access)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yagnikpt/sih-fhir-server.git
   cd sih-fhir-server
   ```

2. Create a virtual environment:
   ```bash
   uv init
   ```

3. Install dependencies:
   ```bash
   uv sync
   ```

4. Configure environment variables:
   Create a `.env` file with:
   ```
   ICD11_API_KEY=your_icd11_api_key_here
   OAUTH_CLIENT_ID=your_oauth_client_id
   OAUTH_CLIENT_SECRET=your_oauth_client_secret
   ```

5. Run the service:
   ```bash
   uv run main.py
   ```

The service will start on `http://localhost:8000`.

## Usage

### Contributing
1. Fork the repository.
2. Create a feature branch: `git switch -c feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request.

## Compliance and Standards

- **FHIR R4**: Fully compliant with HL7 FHIR Release 4 specifications.
- **ICD-11**: Integrates with WHO's International Classification of Diseases, 11th Revision.
- **NAMASTE**: Supports National Ayush Morbidity and Standardized Terminologies of Ayurveda.

## Usage

### Setup
1. Install dependencies: `uv sync`
2. Seed the database: `uv run python seed.py`
3. Run the server: `uv run fastapi dev app/main.py`

### API Endpoints
- `GET /codesystem/{id}`: Retrieve a CodeSystem (e.g., namaste, icd11)
- `GET /conceptmap/{id}`: Retrieve a ConceptMap (e.g., namaste-to-icd11)
- `GET /lookup?q={query}`: Search for codes in NAMASTE
- `GET /translate?code={code}`: Translate code between systems
- `POST /upload`: Upload FHIR Bundle

All endpoints require `X-API-Key: secret-key` header.

## Security

- All API endpoints require OAuth authentication.
- Sensitive operations are logged for audit purposes.
- Data transmission uses HTTPS in production environments.

## Acknowledgments

- Smart India Hackathon organizers
- World Health Organization (WHO) for ICD-11 access
- HL7 International for FHIR standards

For more information, contact the development team or visit the SIH portal.
