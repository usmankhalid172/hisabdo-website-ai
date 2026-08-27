# 2. Current AI POC Overview

## 2.1 What is the Current AI POC?

The current AI Help & Support POC is a Flask-based backend system designed to provide AI-powered assistance to HisabDo users.

The POC receives user requests through API endpoints, processes the provided information, and generates an appropriate support response.

It is currently focused on demonstrating the core support workflow before full integration with the HisabDo application.

## 2.2 Main Purpose

The main purpose of the POC is to demonstrate how AI can be used to improve the HisabDo customer support experience.

The system is designed to help users with:

* Feature guidance
* Step-by-step instructions
* Common errors
* Frequently asked questions
* Context-aware assistance
* Personalized recommendations
* Human support escalation

## 2.3 Current Technology

The current POC uses the following technologies:

* Python
* Flask
* Flask REST API
* JSON for request and response data
* Pandas for processing structured expense data
* AI/support service modules
* Modular Python project structure

## 2.4 Current API Structure

The POC provides API endpoints through which a frontend application can communicate with the AI support system.

Example endpoints include:

```text
GET /
POST /ai/help/context
POST /ai/personalized-recommendation
```

The home endpoint is used to check whether the API is running successfully.

The context-help endpoint processes user context and generates appropriate assistance.

The personalized-recommendation endpoint processes expense information and generates recommendations based on the provided data.

## 2.5 Current POC Architecture

The basic architecture is:

```text
User
  ↓
HisabDo Website / Mobile App
  ↓
Flask REST API
  ↓
Request Validation
  ↓
AI Help & Support Services
  ↓
Response Generation
  ↓
JSON Response
  ↓
User
```

## 2.6 Current Status

The current system is a Proof of Concept rather than a complete production system.

The POC demonstrates the basic API structure, request processing, support-service integration, and response generation.

Future development will focus on improving response quality, integrating a larger knowledge base, strengthening security, adding anti-hallucination controls, and integrating the AI system with the actual HisabDo application.

### Basic flow
User
 ↓
Website/Mobile
 ↓
Flask API
 ↓
AI Services
 ↓
Response
 ↓
User