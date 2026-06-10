# Smoke Test Report: learn-unit-writer

**Date:** 2026-06-10
**Test file:** smoke-test.jsonl
**Total questions:** 11
**Pass rate:** 10/11 (91%)

## Summary

| Criterion | Average | Min | Max |
|-----------|---------|-----|-----|
| Accuracy | 4.4 | 2 | 5 |
| Completeness | 4.4 | 3 | 5 |
| Tone | 5.0 | 5 | 5 |

## Details

### Q1: What platform should developers use to build and deploy AI agents on Microsoft Azure?

- **Ground truth:** Developers should use Microsoft Foundry to build, evaluate, and deploy AI agents on Azure.
- **Response:** Developers should use **Azure AI Studio** to build and deploy AI agents on Microsoft Azure.

**Azure AI Studio** is Microsoft's unified platform for developing, deploying, and managing AI solutions, including generative AI agents, copilots, and custom models. It provides integrated tools for prompt engineering, model fine-tuning, orchestration, and deployment, as well as access to Azure OpenAI Service, Cognitive Services, and other Azure AI capabilities.

**Key features of Azure AI Studio:**
- Visual interface for designing AI workflows and agents
- Integration with Azure OpenAI Service for large language models (GPT, DALL-E, etc.)
- Data management, evaluation, and monitoring tools
- Secure deployment and scaling on Azure infrastructure
- Collaboration and version control for AI projects

**Learn more:**  
- [Azure AI Studio documentation](https://learn.microsoft.com/en-us/azure/ai-studio/)
- [Build AI solutions with Azure AI Studio](https://learn.microsoft.com/en-us/azure/ai-studio/overview)

If you want to build and deploy AI agents, copilots, or generative AI solutions on Azure, **Azure AI Studio** is the recommended platform.
- **Scores:** Accuracy: 2 | Completeness: 3 | Tone: 5
- **Verdict:** FAIL
- **Notes:** The response incorrectly names Azure AI Studio as the platform for building and deploying AI agents, while the ground truth specifies Microsoft Foundry. The technical details about Azure AI Studio are accurate for that product, but do not match the ground truth. Completeness is moderate as it covers the general process but misses the key point about Foundry. Tone is learner-focused and appropriate.

### Q2: What is the Azure service that provides vision, speech, language, and decision AI capabilities?

- **Ground truth:** Azure AI Services provides pre-built AI capabilities including vision, speech, language, and decision APIs.
- **Response:** The Azure service that provides vision, speech, language, and decision AI capabilities is **Azure Cognitive Services**.

Azure Cognitive Services is a collection of cloud-based APIs and services that enable developers to add intelligent features—such as image recognition, speech processing, language understanding, and decision-making—to their applications without needing deep AI expertise. The main categories include:

- **Vision**: Computer Vision, Face, Custom Vision, Form Recognizer
- **Speech**: Speech-to-text, Text-to-speech, Speech Translation, Speaker Recognition
- **Language**: Text Analytics, Translator, Language Understanding (LUIS), QnA Maker
- **Decision**: Personalizer, Content Moderator, Anomaly Detector

You can learn more about Azure Cognitive Services on the [official documentation page](https://learn.microsoft.com/en-us/azure/cognitive-services/).
- **Scores:** Accuracy: 3 | Completeness: 3 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response uses 'Azure Cognitive Services' instead of the updated 'Azure AI Services' terminology, which is the current branding per ground truth. It covers the main categories and APIs, matching the completeness of the ground truth, but misses the updated product name. The tone is learner-focused and appropriate for training content.

### Q3: Which Azure service enables full-text search, semantic search, and vector search over enterprise content?

- **Ground truth:** Azure AI Search enables full-text search, semantic search, and vector search over enterprise content.
- **Response:** The Azure service that enables **full-text search**, **semantic search**, and **vector search** over enterprise content is **Azure AI Search** (formerly known as **Azure Cognitive Search**).

**Azure AI Search** provides:

- **Full-text search**: Indexes and searches text content efficiently, supporting complex queries, filters, and scoring.
- **Semantic search**: Uses AI models to understand intent and context, delivering more relevant results beyond keyword matching.
- **Vector search**: Supports searching using embeddings, allowing similarity search and retrieval based on meaning (useful for scenarios like document retrieval, recommendations, and generative AI).

**Learn more:**
- [Azure AI Search documentation](https://learn.microsoft.com/en-us/azure/search/)
- [Semantic and vector search in Azure AI Search](https://learn.microsoft.com/en-us/azure/search/semantic-search-overview)
- [Vector search overview](https://learn.microsoft.com/en-us/azure/search/vector-search-overview)

**Summary:**  
Azure AI Search is the Microsoft Azure service designed for advanced search scenarios, including full-text, semantic, and vector search across enterprise content.
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response uses the correct product name (Azure AI Search), includes its former name for clarity, and accurately describes full-text, semantic, and vector search. It covers all key points from the ground truth and provides helpful links and explanations in a learner-focused tone.

### Q4: What is the Microsoft unified SaaS analytics platform that brings together data engineering, data warehousing, and business intelligence?

- **Ground truth:** Microsoft Fabric is the unified SaaS analytics platform that integrates data engineering, data warehousing, data science, real-time intelligence, and Power BI.
- **Response:** The Microsoft unified SaaS analytics platform that brings together **data engineering**, **data warehousing**, and **business intelligence** is **Microsoft Fabric**.

**Microsoft Fabric** is an end-to-end analytics platform that integrates multiple data and analytics services, including:

- **Data engineering** (with tools like Data Factory and Spark)
- **Data warehousing** (with Synapse Data Warehousing)
- **Business intelligence** (with Power BI)

Fabric provides a unified experience for data professionals, allowing them to ingest, transform, store, analyze, and visualize data all within a single SaaS environment. It is designed to streamline analytics workflows and enable collaboration across data roles.

**Learn more:**  
- [Microsoft Fabric documentation](https://learn.microsoft.com/en-us/fabric/)
- [What is Microsoft Fabric?](https://learn.microsoft.com/en-us/fabric/get-started/overview/)
- **Scores:** Accuracy: 5 | Completeness: 4 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response correctly identifies Microsoft Fabric and its integration of data engineering, data warehousing, and business intelligence, matching the query. It omits 'data science' and 'real-time intelligence' from the ground truth, so completeness is slightly reduced. The tone is learner-focused and appropriate for training content.

### Q5: What Azure service uses machine learning to extract text, tables, and key-value pairs from documents?

- **Ground truth:** Azure AI Document Intelligence uses machine learning models to extract structured data including text, tables, and key-value pairs from documents.
- **Response:** The Azure service that uses machine learning to extract text, tables, and key-value pairs from documents is **Azure AI Document Intelligence** (formerly known as **Azure Form Recognizer**).

**Azure AI Document Intelligence** enables you to:

- Extract printed and handwritten text from documents
- Identify and extract tables
- Detect and extract key-value pairs (such as fields and their values)
- Analyze documents such as invoices, receipts, business cards, and more

You can use this service via REST API, SDKs, or the Azure portal. It supports custom models for specialized document types and prebuilt models for common document formats.

**Learn more:**  
- [Azure AI Document Intelligence documentation](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview)
- [Quickstart: Extract data from documents using Azure AI Document Intelligence](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/quickstarts/get-started)

Let me know if you need details on how to use it or integrate it into your workflow!
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response uses the correct product name (Azure AI Document Intelligence), mentions its former name, and accurately describes its capabilities in extracting text, tables, and key-value pairs. It also provides additional relevant details and resources, and the tone is learner-focused and supportive.

### Q6: What is the low-code tool in Microsoft Power Platform used to build custom business applications?

- **Ground truth:** Power Apps is the low-code tool within Microsoft Power Platform that enables users to build custom business applications with minimal coding.
- **Response:** The low-code tool in Microsoft Power Platform used to build custom business applications is **Microsoft Power Apps**.

**Power Apps** enables users to create custom apps with minimal coding, allowing business users and developers to design applications that connect to data sources, automate processes, and solve business challenges quickly and efficiently.
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response correctly identifies Power Apps as the low-code tool, uses accurate terminology, and expands on its capabilities in a learner-focused manner. All key points from the ground truth are covered.

### Q7: What is the Microsoft low-code tool for building and publishing AI-powered chatbots and copilots?

- **Ground truth:** Microsoft Copilot Studio is the low-code tool for building, testing, and publishing AI-powered chatbots and copilots.
- **Response:** The Microsoft low-code tool for building and publishing AI-powered chatbots and copilots is **Microsoft Copilot Studio** (formerly known as Power Virtual Agents).

**Copilot Studio** enables users—including business users and developers—to create, customize, and deploy conversational AI bots and copilots using a graphical, low-code interface. It integrates with Microsoft Copilot and other Microsoft 365 services, allowing you to build sophisticated bots that leverage AI, connect to data sources, and automate workflows.

**Key features:**
- Low-code/no-code bot creation
- Integration with Microsoft Copilot and Microsoft 365
- AI-powered conversation design
- Publishing to multiple channels (Teams, web, etc.)
- Extensibility with Power Automate and custom code

**Learn more:**  
- [Microsoft Copilot Studio documentation](https://learn.microsoft.com/en-us/copilot-studio/)
- [Build copilots with Copilot Studio](https://learn.microsoft.com/en-us/copilot-studio/build-copilot)

Let me know if you need guidance on getting started or specific features!
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response correctly identifies Microsoft Copilot Studio as the low-code tool, includes its former name (Power Virtual Agents), and provides additional relevant details and features. The tone is learner-focused and supportive, matching training content style.

### Q8: Which Azure service provides NLP features such as sentiment analysis, named entity recognition, and conversational language understanding?

- **Ground truth:** Azure AI Language provides NLP features including sentiment analysis, named entity recognition, key phrase extraction, and conversational language understanding.
- **Response:** The Azure service that provides NLP features such as **sentiment analysis**, **named entity recognition**, and **conversational language understanding** is **Azure AI Language** (formerly known as Text Analytics and Language Understanding).

### Key Features:
- **Sentiment Analysis:** Determines the sentiment (positive, negative, neutral, mixed) of text.
- **Named Entity Recognition (NER):** Identifies entities such as people, organizations, locations, dates, etc. in text.
- **Conversational Language Understanding (CLU):** Enables understanding of conversational input, extracting intents and entities for building chatbots and conversational apps.

#### Service Components:
- **Azure AI Language (Text Analytics API):** For sentiment analysis, NER, key phrase extraction, and language detection.
- **Azure AI Language (Conversational Language Understanding):** For intent and entity extraction in conversational scenarios.

#### Learn More:
- [Azure AI Language documentation](https://learn.microsoft.com/en-us/azure/ai-services/language-service/)
- [Text Analytics overview](https://learn.microsoft.com/en-us/azure/ai-services/language-service/text-analytics/overview)
- [Conversational Language Understanding overview](https://learn.microsoft.com/en-us/azure/ai-services/language-service/conversational-language-understanding/overview)

**Summary:**  
Use **Azure AI Language** for NLP tasks like sentiment analysis, named entity recognition, and conversational language understanding.
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response correctly identifies Azure AI Language as the service providing NLP features, includes all relevant features from the ground truth, and uses learner-focused, clear explanations with helpful links. Terminology and facts are accurate and complete.

### Q9: What Azure service provides image analysis, optical character recognition, and spatial analysis capabilities?

- **Ground truth:** Azure AI Vision provides image analysis, optical character recognition (OCR), face detection, and spatial analysis capabilities.
- **Response:** The Azure service that provides **image analysis**, **optical character recognition (OCR)**, and **spatial analysis** capabilities is **Azure Computer Vision**.

**Azure Computer Vision** is part of the Azure AI services suite and offers a range of features, including:

- **Image Analysis**: Extracts information such as objects, faces, text, and descriptions from images.
- **Optical Character Recognition (OCR)**: Detects and extracts printed or handwritten text from images and documents.
- **Spatial Analysis**: Analyzes video streams to understand people's movements and occupancy in physical spaces (available in the Azure Video Analyzer for spatial analysis scenarios).

**Learn more:**
- [Azure Computer Vision documentation](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/)
- [Azure Spatial Analysis overview](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/spatial-analysis-overview)

**Note:** For spatial analysis specifically, Azure Computer Vision offers this capability as part of its Video Analysis features, sometimes referred to as "Spatial Analysis" in the context of analyzing video feeds for people movement and occupancy.
- **Scores:** Accuracy: 3 | Completeness: 3 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response uses 'Azure Computer Vision' instead of the updated 'Azure AI Vision' service name, which is the current branding. It covers the main capabilities (image analysis, OCR, spatial analysis) but does not mention face detection, which is in the ground truth. The tone is clear, learner-focused, and appropriate for training content.

### Q10: How is business intelligence and reporting integrated in Microsoft Fabric?

- **Ground truth:** Microsoft Fabric includes Power BI as its business intelligence and reporting experience, providing a unified analytics platform where reports and semantic models coexist with data engineering and data science workloads.
- **Response:** To answer your question thoroughly, I'll provide a concise overview:

**Business intelligence (BI) and reporting in Microsoft Fabric** are integrated through several core components that work together to deliver end-to-end analytics and insights:

1. **Power BI Integration**:  
   - Power BI is natively embedded in Microsoft Fabric, enabling users to create, share, and collaborate on interactive reports and dashboards directly within the Fabric workspace.
   - You can connect to data stored in Fabric (such as Lakehouse, Data Warehouse, or other sources) and build visualizations without leaving the platform.

2. **Unified Data Platform**:  
   - Fabric unifies data engineering, data science, real-time analytics, and BI under one SaaS experience.
   - Dataflows, pipelines, and Lakehouse objects are accessible to BI tools, streamlining data preparation and modeling.

3. **Direct Lake Integration**:  
   - Power BI can connect directly to Delta tables in the Lakehouse, supporting real-time analytics and reducing data duplication.

4. **Workspace Collaboration**:  
   - Fabric workspaces allow teams to collaborate on datasets, reports, and dashboards, with integrated security and governance.

5. **End-to-End Analytics**:  
   - Users can ingest, transform, model, and visualize data in a single environment, accelerating the time from raw data to actionable insights.

6. **Reporting Features**:  
   - Fabric supports paginated reports, interactive dashboards, and AI-powered insights, all accessible through Power BI.

**Learn more:**  
- [Microsoft Fabric documentation](https://learn.microsoft.com/en-us/fabric/)
- [Power BI in Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/bi/power-bi-in-fabric)

If you need a deeper technical walkthrough or want to see how to set up BI and reporting in Fabric step-by-step, let me know your role (e.g., data analyst, business user, IT admin) and your goals, and I can tailor the guidance!
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response correctly identifies Power BI as the business intelligence and reporting experience in Microsoft Fabric, explains its integration, and covers the unified analytics platform concept. It expands on the ground truth with additional details (e.g., direct lake integration, workspace collaboration), all accurate. The tone is learner-focused and offers further help, matching training content style.

### Q11: What are the core workloads integrated within Microsoft Fabric that an analytics engineer works with daily?

- **Ground truth:** Within the unified Fabric platform—which integrates Data Factory, Data Engineering, Data Science, Data Warehouse, Real-Time Intelligence, Power BI, and OneLake into a single SaaS analytics environment—the analytics engineer's daily work spans several interconnected areas.
- **Response:** Microsoft Fabric is an end-to-end analytics platform that integrates multiple core workloads, enabling analytics engineers to build, manage, and operationalize data solutions efficiently. The main workloads within Microsoft Fabric that analytics engineers interact with daily include:

---

### 1. **Data Engineering**
- **Lakehouse**: Combines the best of data lakes and data warehouses, allowing engineers to store, transform, and manage structured and unstructured data.
- **Notebooks**: Supports collaborative development using languages like SQL, Python, and Spark for data exploration, transformation, and analysis.
- **Pipelines**: Enables orchestration and automation of data movement and transformation tasks.

### 2. **Data Warehousing**
- **Warehouse**: Provides a scalable, high-performance SQL-based environment for storing and querying structured data, supporting analytics and reporting workloads.

### 3. **Data Science**
- **Notebooks & ML Workspaces**: Facilitates advanced analytics, machine learning model development, and experimentation directly within Fabric.

### 4. **Real-Time Analytics**
- **KQL Database**: Allows ingestion, processing, and querying of streaming data using Kusto Query Language (KQL), ideal for telemetry, logs, and IoT scenarios.

### 5. **Business Intelligence**
- **Power BI**: Integrated for data visualization, dashboarding, and reporting, enabling analytics engineers to deliver insights to business stakeholders.

### 6. **Data Integration**
- **Dataflows**: Provides low-code/no-code tools for ingesting, transforming, and preparing data from multiple sources.

---

**Daily Tasks for Analytics Engineers:**
- Ingesting and transforming data using Lakehouse, Pipelines, and Dataflows.
- Building and managing data models in Warehouses and Lakehouses.
- Developing and running notebooks for data exploration and transformation.
- Creating real-time analytics solutions with KQL Databases.
- Visualizing and sharing insights via Power BI.
- Automating workflows and orchestrating data processes.

**Learn more:**  
- [Microsoft Fabric documentation](https://learn.microsoft.com/en-us/fabric/)
- [Fabric workloads overview](https://learn.microsoft.com/en-us/fabric/get-started/fabric-workloads)

Let me know if you want a deeper dive into any specific workload or scenario!
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response accurately names all core workloads (Data Engineering, Data Science, Data Warehouse, Real-Time Analytics, Power BI, Data Integration) and describes their roles, matching the ground truth. It is comprehensive and learner-focused, with clear explanations and links for further learning.
