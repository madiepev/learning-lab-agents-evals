# Smoke Test Report: learn-unit-writer

**Date:** 2026-06-10
**Test file:** smoke-test.jsonl
**Total questions:** 11
**Pass rate:** 10/11 (91%)

## Summary

| Criterion | Average | Min | Max |
|-----------|---------|-----|-----|
| Accuracy | 4.5 | 2 | 5 |
| Completeness | 4.6 | 3 | 5 |
| Tone | 5.0 | 5 | 5 |

## Details

### Q1: What platform should developers use to build and deploy AI agents on Microsoft Azure?

- **Ground truth:** Developers should use Microsoft Foundry to build, evaluate, and deploy AI agents on Azure.
- **Response:** Developers should use **Azure AI Studio** to build and deploy AI agents on Microsoft Azure.

**Azure AI Studio** is Microsoft's unified platform for developing, training, deploying, and managing AI solutions—including generative AI agents, copilots, and custom models. It provides integrated tools for prompt engineering, orchestration, data management, and deployment, supporting both low-code and pro-code workflows.

**Key features of Azure AI Studio:**
- Build, test, and deploy AI agents and copilots
- Integrate with Azure OpenAI, Cognitive Services, and other Azure AI offerings
- Manage data, prompts, and orchestration pipelines
- Secure and monitor AI solutions at scale

**Learn more:**  
[Azure AI Studio documentation](https://learn.microsoft.com/en-us/azure/ai-studio/overview)

If you need guidance on specific agent architectures or deployment scenarios, let me know!
- **Scores:** Accuracy: 2 | Completeness: 3 | Tone: 5
- **Verdict:** FAIL
- **Notes:** The response incorrectly names Azure AI Studio as the platform for building and deploying AI agents, while the ground truth specifies Microsoft Foundry. The technical details about Azure AI Studio are accurate but not relevant to the specific question. Completeness is moderate as it covers the general workflow but misses the key platform. Tone is learner-focused and appropriate.

### Q2: What is the Azure service that provides vision, speech, language, and decision AI capabilities?

- **Ground truth:** Azure AI Services provides pre-built AI capabilities including vision, speech, language, and decision APIs.
- **Response:** The Azure service that provides vision, speech, language, and decision AI capabilities is **Azure AI services** (formerly known as **Azure Cognitive Services**).

Azure AI services offer a suite of pre-built APIs and tools for:

- **Vision**: Image analysis, object detection, OCR, facial recognition, etc.
- **Speech**: Speech-to-text, text-to-speech, speech translation, speaker recognition.
- **Language**: Language understanding, translation, text analytics, sentiment analysis, conversational AI.
- **Decision**: Anomaly detection, content moderation, personalizer for recommendations.

You can learn more here:  
[Azure AI services documentation](https://learn.microsoft.com/en-us/azure/ai-services/)

**Note:** Azure Cognitive Services is the previous name; Microsoft now refers to these as Azure AI services.
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response uses the correct product name (Azure AI services), acknowledges the previous name (Azure Cognitive Services), and accurately describes the vision, speech, language, and decision capabilities. It is learner-focused, provides examples, and includes a helpful documentation link.

### Q3: Which Azure service enables full-text search, semantic search, and vector search over enterprise content?

- **Ground truth:** Azure AI Search enables full-text search, semantic search, and vector search over enterprise content.
- **Response:** The Azure service that enables **full-text search**, **semantic search**, and **vector search** over enterprise content is **Azure AI Search** (formerly known as **Azure Cognitive Search**).

**Azure AI Search** provides:

- **Full-text search**: Indexes and searches text content efficiently, supporting advanced query syntax, filters, and scoring.
- **Semantic search**: Uses AI models to understand the meaning behind queries and content, offering more relevant results beyond keyword matching.
- **Vector search**: Supports searching using vector embeddings, enabling similarity search for scenarios like image, document, or semantic matching.

**Key features:**
- Integrates with Azure AI services for enrichment (OCR, entity extraction, sentiment analysis, etc.)
- Supports enterprise-scale indexing and querying
- Offers REST APIs, SDKs, and integration with Azure data sources

**Learn more:**  
- [Azure AI Search documentation](https://learn.microsoft.com/en-us/azure/search/)
- [Semantic and vector search in Azure AI Search](https://learn.microsoft.com/en-us/azure/search/semantic-search-overview)
- [Vector search overview](https://learn.microsoft.com/en-us/azure/search/vector-search-overview)

If you need guidance on implementing these search capabilities, let me know your scenario!
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response correctly identifies Azure AI Search as the service, includes its former name (Azure Cognitive Search), and accurately describes full-text, semantic, and vector search. It expands on features and provides helpful links, maintaining a learner-focused tone. All key points from the ground truth are covered.

### Q4: What is the Microsoft unified SaaS analytics platform that brings together data engineering, data warehousing, and business intelligence?

- **Ground truth:** Microsoft Fabric is the unified SaaS analytics platform that integrates data engineering, data warehousing, data science, real-time intelligence, and Power BI.
- **Response:** The Microsoft unified SaaS analytics platform that brings together **data engineering**, **data warehousing**, and **business intelligence** is **Microsoft Fabric**.

**Microsoft Fabric** is an end-to-end analytics platform as a service (SaaS) that integrates multiple data and analytics experiences—including data engineering, data science, real-time analytics, data warehousing, and business intelligence—into a single unified solution. It combines capabilities from Azure Data Factory, Azure Synapse Analytics, and Power BI, providing a seamless experience for data professionals and business users.

**Key features of Microsoft Fabric:**
- Unified workspace for data engineering, data warehousing, and BI
- Deep integration with Power BI for business intelligence
- Lakehouse architecture for scalable data storage and analytics
- Built-in data pipelines and orchestration
- Real-time analytics and data science capabilities

**Learn more:**  
[Microsoft Fabric documentation](https://learn.microsoft.com/en-us/fabric/)
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response correctly identifies Microsoft Fabric as the unified SaaS analytics platform and expands on its features, including all relevant areas from the ground truth (data engineering, data warehousing, data science, real-time intelligence, and Power BI). The tone is learner-focused and appropriate for training content.

### Q5: What Azure service uses machine learning to extract text, tables, and key-value pairs from documents?

- **Ground truth:** Azure AI Document Intelligence uses machine learning models to extract structured data including text, tables, and key-value pairs from documents.
- **Response:** The Azure service that uses machine learning to extract text, tables, and key-value pairs from documents is **Azure AI Document Intelligence** (formerly known as **Azure Form Recognizer**).

**Azure AI Document Intelligence** enables you to:

- Extract printed and handwritten text from documents.
- Identify and extract tables, key-value pairs, and structured data.
- Analyze receipts, invoices, business cards, and custom document types.

You can use this service via REST API, SDKs, or through the Azure portal. It supports prebuilt models for common document types and allows you to train custom models for your specific needs.

**Learn more:**  
- [Azure AI Document Intelligence documentation](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview)
- [Quickstart: Extract information from documents](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/quickstarts/get-started-rest-api)

Let me know if you need details on how to use this service or integrate it into your application!
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response correctly identifies Azure AI Document Intelligence, mentions its former name, and accurately describes its capabilities. It covers all key points from the ground truth and provides additional helpful context and resources in a learner-focused tone.

### Q6: What is the low-code tool in Microsoft Power Platform used to build custom business applications?

- **Ground truth:** Power Apps is the low-code tool within Microsoft Power Platform that enables users to build custom business applications with minimal coding.
- **Response:** The low-code tool in Microsoft Power Platform used to build custom business applications is **Microsoft Power Apps**.

**Power Apps** enables users—both business professionals and developers—to create custom apps quickly with minimal coding. These apps can connect to various data sources, automate workflows, and run on web, mobile, and tablet devices. Power Apps is designed for rapid application development, making it easy to solve business challenges with tailored solutions.
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response correctly identifies Power Apps as the low-code tool in Microsoft Power Platform, provides additional relevant details about its capabilities, and uses a learner-focused tone suitable for training content.

### Q7: What is the Microsoft low-code tool for building and publishing AI-powered chatbots and copilots?

- **Ground truth:** Microsoft Copilot Studio is the low-code tool for building, testing, and publishing AI-powered chatbots and copilots.
- **Response:** The Microsoft low-code tool for building and publishing AI-powered chatbots and copilots is **Microsoft Copilot Studio** (formerly known as Power Virtual Agents).

**Copilot Studio** enables users—especially business users and developers—to create, customize, and deploy conversational AI bots (chatbots and copilots) using a visual, low-code interface. It integrates with Microsoft Copilot, Microsoft Teams, and other Microsoft 365 services, allowing you to build bots that leverage generative AI, connect to data sources, and automate workflows.

**Key features:**
- Low-code/no-code designer for creating conversational flows
- Integration with Microsoft Copilot and Microsoft Teams
- AI-powered natural language understanding
- Ability to connect to data, APIs, and automate tasks
- Publishing and management tools for deploying bots across channels

**Learn more:**  
- [Microsoft Copilot Studio documentation](https://learn.microsoft.com/en-us/copilot-studio/)
- [Build AI-powered copilots with Copilot Studio](https://learn.microsoft.com/en-us/copilot-studio/overview)
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response correctly identifies Microsoft Copilot Studio as the low-code tool, includes its former name (Power Virtual Agents), and provides a detailed, learner-focused explanation with key features and relevant links. All points from the ground truth are covered and expanded in a helpful way.

### Q8: Which Azure service provides NLP features such as sentiment analysis, named entity recognition, and conversational language understanding?

- **Ground truth:** Azure AI Language provides NLP features including sentiment analysis, named entity recognition, key phrase extraction, and conversational language understanding.
- **Response:** The Azure service that provides NLP features such as **sentiment analysis**, **named entity recognition**, and **conversational language understanding** is **Azure AI Language** (formerly known as Text Analytics and Language Understanding (LUIS)).

**Azure AI Language** offers a suite of natural language processing capabilities, including:

- **Sentiment Analysis**: Determines the sentiment (positive, negative, neutral, or mixed) of text.
- **Named Entity Recognition (NER)**: Identifies and categorizes entities such as people, organizations, locations, dates, and more within text.
- **Conversational Language Understanding**: Enables the creation of conversational applications that understand user intent and extract relevant information.

You can access these features via the [Azure AI Language API](https://learn.microsoft.com/en-us/azure/ai-services/language-service/overview), which is part of Azure Cognitive Services.

**Learn more:**  
- [Azure AI Language documentation](https://learn.microsoft.com/en-us/azure/ai-services/language-service/overview)
- [Sentiment Analysis](https://learn.microsoft.com/en-us/azure/ai-services/language-service/sentiment-analysis/overview)
- [Named Entity Recognition](https://learn.microsoft.com/en-us/azure/ai-services/language-service/named-entity-recognition/overview)
- [Conversational Language Understanding](https://learn.microsoft.com/en-us/azure/ai-services/language-service/conversational-language-understanding/overview)
- **Scores:** Accuracy: 5 | Completeness: 4 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response correctly identifies Azure AI Language as the service providing NLP features and accurately describes sentiment analysis, named entity recognition, and conversational language understanding. It omits 'key phrase extraction' from the ground truth, so completeness is slightly reduced. The tone is learner-focused and appropriate for training content.

### Q9: What Azure service provides image analysis, optical character recognition, and spatial analysis capabilities?

- **Ground truth:** Azure AI Vision provides image analysis, optical character recognition (OCR), face detection, and spatial analysis capabilities.
- **Response:** The Azure service that provides **image analysis**, **optical character recognition (OCR)**, and **spatial analysis** capabilities is **Azure Computer Vision**.

**Azure Computer Vision** is part of the Azure AI services suite. It offers:

- **Image Analysis**: Extracts information such as objects, faces, tags, descriptions, and more from images.
- **Optical Character Recognition (OCR)**: Detects and reads text in images and documents, including handwritten and printed text.
- **Spatial Analysis**: Analyzes video feeds to understand people’s movements and interactions in physical spaces (such as counting people, detecting occupancy, and measuring distances).

You can learn more about these features in the official documentation:
- [Azure Computer Vision documentation](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/)

**Summary:**  
Azure Computer Vision is the Azure service for image analysis, OCR, and spatial analysis.
- **Scores:** Accuracy: 3 | Completeness: 4 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response uses 'Azure Computer Vision' instead of the updated 'Azure AI Vision' name, which is a minor inaccuracy. It covers all the main capabilities (image analysis, OCR, spatial analysis) but omits face detection, which is mentioned in the ground truth. The tone is clear, learner-focused, and appropriate for training content.

### Q10: How is business intelligence and reporting integrated in Microsoft Fabric?

- **Ground truth:** Microsoft Fabric includes Power BI as its business intelligence and reporting experience, providing a unified analytics platform where reports and semantic models coexist with data engineering and data science workloads.
- **Response:** To answer your question about **business intelligence and reporting integration in Microsoft Fabric**, here's a concise overview:

---

## Business Intelligence and Reporting in Microsoft Fabric

**Microsoft Fabric** is an end-to-end analytics platform that unifies data engineering, data science, real-time analytics, and business intelligence (BI) under one umbrella. Its integration of BI and reporting is primarily achieved through **Power BI**, which is natively embedded in Fabric.

### Key Integration Points

1. **Power BI Integration**
   - **Power BI** is a core experience in Microsoft Fabric, allowing users to create, share, and collaborate on interactive reports and dashboards directly within the Fabric workspace.
   - You can connect Power BI to data stored in Fabric's **OneLake**, **Lakehouse**, **Warehouse**, or other data sources, enabling seamless data exploration and visualization.

2. **Unified Workspace**
   - Fabric provides a single workspace where data engineers, analysts, and business users can collaborate.
   - BI artifacts (reports, dashboards, datasets) are managed alongside data pipelines, notebooks, and dataflows, streamlining workflows.

3. **Direct Lake Mode**
   - Power BI can query data directly from OneLake in "Direct Lake" mode, eliminating the need for data duplication and improving performance.

4. **Dataflows and Datasets**
   - Dataflows in Fabric allow for data transformation and preparation, which can then be used as datasets in Power BI for reporting.

5. **Security and Governance**
   - Fabric integrates with Microsoft Purview for data governance, ensuring secure access and compliance for BI and reporting.

6. **Real-Time Analytics**
   - Fabric supports real-time analytics scenarios, enabling Power BI reports to visualize streaming data from sources like Event Streams.

### Typical Workflow

1. **Ingest and Prepare Data**: Use Fabric pipelines, dataflows, or notebooks to bring data into OneLake.
2. **Model Data**: Create Lakehouse or Warehouse models.
3. **Visualize and Report**: Build Power BI reports and dashboards directly in Fabric, leveraging prepared datasets.
4. **Share and Collaborate**: Publish and share BI artifacts with stakeholders, all within the Fabric workspace.

### Learn More

- [Microsoft Fabric documentation](https://learn.microsoft.com/en-us/fabric/)
- [Power BI in Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/power-bi/)

---

**Summary:**  
Business intelligence and reporting are tightly integrated in Microsoft Fabric through Power BI, unified workspaces, direct data access, and robust governance features. This enables organizations to build, share, and manage BI solutions efficiently within a single analytics platform.
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response correctly identifies Power BI as the business intelligence and reporting experience in Microsoft Fabric, explains its integration, and covers all key points from the ground truth. The tone is learner-focused and appropriate for training content.

### Q11: What are the core workloads integrated within Microsoft Fabric that an analytics engineer works with daily?

- **Ground truth:** Within the unified Fabric platform—which integrates Data Factory, Data Engineering, Data Science, Data Warehouse, Real-Time Intelligence, Power BI, and OneLake into a single SaaS analytics environment—the analytics engineer's daily work spans several interconnected areas.
- **Response:** Microsoft Fabric is an end-to-end analytics platform that integrates multiple core workloads, enabling analytics engineers to work efficiently across the data lifecycle. The primary workloads within Microsoft Fabric that analytics engineers interact with daily include:

### 1. **Data Engineering**
- **Lakehouse**: Combines the best of data lakes and data warehouses, allowing engineers to store, process, and analyze large volumes of structured and unstructured data.
- **Notebooks**: Supports collaborative development using languages like Python, SQL, and Spark for data transformation and exploration.
- **Pipelines**: Enables orchestration and automation of data movement and transformation tasks.

### 2. **Data Warehousing**
- **Warehouse**: Provides a scalable, high-performance SQL-based environment for storing and querying structured data, supporting advanced analytics and reporting.

### 3. **Data Science**
- **Notebooks**: Used for machine learning, statistical analysis, and advanced data exploration.
- **ML Models**: Integration with Azure Machine Learning for model training, deployment, and scoring.

### 4. **Real-Time Analytics**
- **KQL Database**: Supports real-time data ingestion and querying using Kusto Query Language, ideal for telemetry, logs, and streaming analytics.

### 5. **Business Intelligence**
- **Power BI**: Embedded within Fabric, allows analytics engineers to build dashboards, reports, and visualizations directly on top of Lakehouse, Warehouse, or other data sources.

### 6. **Data Integration**
- **Dataflows**: Provides low-code data transformation and integration capabilities, enabling ingestion from various sources into Fabric workloads.

---

#### **Summary Table**

| Workload           | Description                                      | Typical Tasks for Analytics Engineers            |
|--------------------|--------------------------------------------------|--------------------------------------------------|
| Lakehouse          | Unified storage and analytics for big data       | Data ingestion, transformation, exploration      |
| Warehouse          | SQL-based structured data storage                | Querying, modeling, reporting                    |
| Notebooks          | Interactive development environment              | ETL, data science, exploration                   |
| Pipelines          | Data orchestration and automation                | Scheduling, monitoring, managing data flows      |
| KQL Database       | Real-time analytics with Kusto                   | Streaming data analysis, log analytics           |
| Power BI           | Business intelligence and visualization          | Building dashboards, reports, sharing insights   |
| Dataflows          | Low-code data integration                        | Ingesting and transforming data from sources     |

---

**In daily practice, analytics engineers typically:**
- Ingest and transform data using Lakehouse, Notebooks, Pipelines, and Dataflows.
- Model and query data in Warehouses.
- Analyze real-time data in KQL Databases.
- Build and share insights using Power BI.

**Learn more:**  
- [Microsoft Fabric documentation](https://learn.microsoft.com/en-us/fabric/)
- [Lakehouse in Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-overview)
- [Warehouse in Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/data-warehouse/warehouse-overview)
- [Power BI in Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/bi/power-bi-overview)

Let me know if you need a deeper dive into any specific workload or how they integrate!
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response accurately lists all core workloads integrated within Microsoft Fabric (Data Engineering, Data Warehouse, Data Science, Real-Time Analytics, Power BI, Data Integration) and describes their relevance to analytics engineers. It uses correct terminology and facts, covers all key points from the ground truth, and presents information in a learner-focused, clear, and engaging style.
