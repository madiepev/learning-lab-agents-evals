# Smoke Test Report: learn-unit-writer

**Date:** 2026-05-07
**Test file:** smoke-test.jsonl
**Total questions:** 11
**Pass rate:** 11/11 (100%)

## Summary

| Criterion | Average | Min | Max |
|-----------|---------|-----|-----|
| Accuracy | 4.5 | 3 | 5 |
| Completeness | 4.7 | 3 | 5 |
| Tone | 5.0 | 5 | 5 |

## Details

### Q1: What platform should developers use to build and deploy AI agents on Microsoft Azure?

- **Ground truth:** Developers should use Microsoft Foundry to build, evaluate, and deploy AI agents on Azure.
- **Response:** Developers should use **Azure AI Studio** to build and deploy AI agents on Microsoft Azure.

**Azure AI Studio** is Microsoft's unified platform for developing, deploying, and managing AI solutions, including generative AI agents, copilots, and custom machine learning models. It provides integrated tools for prompt engineering, orchestration, data management, and deployment, making it the recommended environment for creating AI-powered applications and agents on Azure.

**Key features of Azure AI Studio:**
- Visual interface for designing AI workflows and agents
- Integration with Azure OpenAI Service, Azure Machine Learning, and other Azure AI services
- Built-in tools for prompt engineering, evaluation, and monitoring
- Support for deploying agents as APIs, web apps, or within Microsoft Teams and other platforms

**Learn more:**  
[Azure AI Studio documentation](https://learn.microsoft.com/en-us/azure/ai-studio/overview)

If you need guidance on getting started or specific agent scenarios, let me know!
- **Scores:** Accuracy: 3 | Completeness: 3 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response incorrectly names Azure AI Studio as the platform, while the ground truth specifies Microsoft Foundry. The technical details about Azure AI Studio are accurate, but the main point (the correct platform) is missed. The tone is learner-focused and appropriate.

### Q2: What is the Azure service that provides vision, speech, language, and decision AI capabilities?

- **Ground truth:** Azure AI Services provides pre-built AI capabilities including vision, speech, language, and decision APIs.
- **Response:** The Azure service that provides vision, speech, language, and decision AI capabilities is **Azure Cognitive Services**.

Azure Cognitive Services is a collection of AI services and APIs that enable developers to easily add intelligent features—such as image recognition, speech processing, language understanding, and decision-making—to their applications. The main categories include:

- **Vision**: Computer Vision, Face, Custom Vision, Form Recognizer
- **Speech**: Speech-to-text, Text-to-speech, Speech Translation, Speaker Recognition
- **Language**: Text Analytics, Translator, Language Understanding (LUIS), QnA Maker
- **Decision**: Personalizer, Content Moderator, Anomaly Detector

You can learn more about Azure Cognitive Services here:  
[Azure Cognitive Services documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/)
- **Scores:** Accuracy: 4 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response uses 'Azure Cognitive Services' instead of 'Azure AI Services', which is the updated branding. However, it correctly describes the capabilities and categories, and provides a learner-focused explanation. Completeness and tone are excellent, but accuracy is slightly reduced due to outdated terminology.

### Q3: Which Azure service enables full-text search, semantic search, and vector search over enterprise content?

- **Ground truth:** Azure AI Search enables full-text search, semantic search, and vector search over enterprise content.
- **Response:** The Azure service that enables **full-text search**, **semantic search**, and **vector search** over enterprise content is **Azure AI Search** (formerly known as Azure Cognitive Search).

**Azure AI Search** provides:

- **Full-text search**: Indexes and searches text in documents, databases, and other sources.
- **Semantic search**: Uses AI models to understand intent and context, delivering more relevant results.
- **Vector search**: Supports searching using embeddings, enabling similarity search for scenarios like image, audio, or natural language queries.

**Key features:**
- Integrates with Azure OpenAI for advanced semantic and vector search capabilities.
- Supports indexing of structured and unstructured data from various sources.
- Offers built-in cognitive skills for enrichment (OCR, entity extraction, language detection, etc.).

**Learn more:**  
- [Azure AI Search documentation](https://learn.microsoft.com/en-us/azure/search/)
- [Semantic and vector search in Azure AI Search](https://learn.microsoft.com/en-us/azure/search/semantic-search-overview)
- [Vector search in Azure AI Search](https://learn.microsoft.com/en-us/azure/search/vector-search-overview)
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response uses the correct product name (Azure AI Search), accurately describes its capabilities (full-text, semantic, and vector search), and provides additional relevant details and resources. The tone is learner-focused and clear, matching training content style.

### Q4: What is the Microsoft unified SaaS analytics platform that brings together data engineering, data warehousing, and business intelligence?

- **Ground truth:** Microsoft Fabric is the unified SaaS analytics platform that integrates data engineering, data warehousing, data science, real-time intelligence, and Power BI.
- **Response:** The Microsoft unified SaaS analytics platform that brings together **data engineering**, **data warehousing**, and **business intelligence** is **Microsoft Fabric**.

**Microsoft Fabric** is an end-to-end analytics platform as a service (SaaS) that integrates multiple data and analytics experiences—including data engineering, data science, real-time analytics, data warehousing, and business intelligence—into a single unified solution. It combines technologies like Azure Data Factory, Azure Synapse Analytics, and Power BI, providing a seamless experience for data professionals and business users.

**Key features of Microsoft Fabric:**
- Unified workspace for data engineering, warehousing, and BI
- Deep integration with Power BI for business intelligence
- Built-in data lake (OneLake) for centralized storage
- SaaS model for simplified management and scalability

**Learn more:**  
- [Microsoft Fabric documentation](https://learn.microsoft.com/en-us/fabric/)
- [What is Microsoft Fabric?](https://learn.microsoft.com/en-us/fabric/get-started/overview/)
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response correctly identifies Microsoft Fabric as the unified SaaS analytics platform and expands on its features, including integration of data engineering, data warehousing, data science, real-time analytics, and business intelligence. It uses accurate terminology and provides helpful links, matching the learner-focused tone of Microsoft training content.

### Q5: What Azure service uses machine learning to extract text, tables, and key-value pairs from documents?

- **Ground truth:** Azure AI Document Intelligence uses machine learning models to extract structured data including text, tables, and key-value pairs from documents.
- **Response:** The Azure service that uses machine learning to extract text, tables, and key-value pairs from documents is **Azure AI Document Intelligence** (formerly known as **Azure Form Recognizer**).

**Azure AI Document Intelligence** enables you to:

- Extract printed and handwritten text from documents.
- Identify and extract tables, key-value pairs, and structured data.
- Analyze documents such as invoices, receipts, contracts, and more.

You can use pre-built models for common document types or train custom models for your specific document layouts.

**Learn more:**  
- [Azure AI Document Intelligence documentation](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/)
- [Quickstart: Extract information from documents using Azure AI Document Intelligence](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/quickstarts/get-started-rest-api)

Let me know if you need details on how to use this service or integrate it into your applications!
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response correctly identifies Azure AI Document Intelligence, includes its former name, and explains its capabilities in extracting text, tables, and key-value pairs. It provides additional context and helpful links, maintaining a learner-focused tone.

### Q6: What is the low-code tool in Microsoft Power Platform used to build custom business applications?

- **Ground truth:** Power Apps is the low-code tool within Microsoft Power Platform that enables users to build custom business applications with minimal coding.
- **Response:** The low-code tool in Microsoft Power Platform used to build custom business applications is **Microsoft Power Apps**.

**Power Apps** enables users—both developers and non-developers—to create custom apps for business needs with minimal coding. You can design apps for web and mobile devices, connect to various data sources (like SharePoint, Microsoft Dataverse, Excel, and more), and automate workflows. The platform provides a drag-and-drop interface, pre-built templates, and integration with other Power Platform tools such as Power Automate and Power BI.

**Learn more:**  
- [Power Apps documentation](https://learn.microsoft.com/power-apps/)
- [Introduction to Power Apps](https://learn.microsoft.com/power-apps/getting-started)
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response correctly identifies Power Apps as the low-code tool in Microsoft Power Platform for building custom business applications. It expands on the features, integration, and usability, covering all key points from the ground truth. The tone is learner-focused and includes helpful links for further learning.

### Q7: What is the Microsoft low-code tool for building and publishing AI-powered chatbots and copilots?

- **Ground truth:** Microsoft Copilot Studio is the low-code tool for building, testing, and publishing AI-powered chatbots and copilots.
- **Response:** The Microsoft low-code tool for building and publishing AI-powered chatbots and copilots is **Microsoft Copilot Studio** (formerly known as Power Virtual Agents).

**Copilot Studio** enables users—including business users, developers, and IT professionals—to create, customize, and deploy conversational AI solutions (chatbots and copilots) with a visual, low-code interface. It integrates with Microsoft Copilot and other Microsoft services, allowing you to build intelligent bots that can connect to data, automate workflows, and provide personalized experiences.

**Key features:**
- Visual designer for creating conversation flows
- Integration with Microsoft Copilot, Teams, and other platforms
- Built-in AI capabilities for natural language understanding
- Easy publishing and management of bots/copilots
- Extensible with custom code and connectors

**Learn more:**  
- [Microsoft Copilot Studio documentation](https://learn.microsoft.com/en-us/copilot-studio/)
- [Overview of Copilot Studio](https://learn.microsoft.com/en-us/copilot-studio/overview)

If you need guidance on how to use Copilot Studio or want to build a chatbot/copilot, let me know!
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response correctly identifies Microsoft Copilot Studio as the low-code tool, provides its former name, and elaborates on its features and integration. The tone is learner-focused and supportive, matching training content style. All key points from the ground truth are covered.

### Q8: Which Azure service provides NLP features such as sentiment analysis, named entity recognition, and conversational language understanding?

- **Ground truth:** Azure AI Language provides NLP features including sentiment analysis, named entity recognition, key phrase extraction, and conversational language understanding.
- **Response:** The Azure service that provides NLP features such as sentiment analysis, named entity recognition, and conversational language understanding is **Azure AI Language** (formerly known as Azure Cognitive Services Language).

Azure AI Language offers:
- Sentiment analysis
- Named entity recognition (NER)
- Conversational language understanding
- Key phrase extraction
- Language detection
- Opinion mining
- Question answering
- Summarization

You can learn more about its capabilities in the official documentation:
- [Azure AI Language overview](https://learn.microsoft.com/en-us/azure/ai-services/language-service/overview)
- [Get started with natural language processing in Azure](https://learn.microsoft.com/training/modules/get-started-language-azure/)

This service is designed for developers, AI engineers, and data scientists to integrate advanced NLP features into applications.
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response correctly identifies Azure AI Language as the service, lists all relevant NLP features (including those in the ground truth), and provides additional context and resources. The tone is learner-focused and appropriate for training content.

### Q9: What Azure service provides image analysis, optical character recognition, and spatial analysis capabilities?

- **Ground truth:** Azure AI Vision provides image analysis, optical character recognition (OCR), face detection, and spatial analysis capabilities.
- **Response:** The Azure service that provides **image analysis**, **optical character recognition (OCR)**, and **spatial analysis** capabilities is **Azure Computer Vision**, which is part of the Azure AI services suite.

### Key Features:

- **Image Analysis**: Extracts information such as objects, faces, colors, and tags from images.
- **Optical Character Recognition (OCR)**: Detects and extracts printed or handwritten text from images and documents.
- **Spatial Analysis**: Analyzes video streams to detect people, movement, and spatial relationships (such as occupancy and distance), often used for workplace safety and retail scenarios.

**Learn more:**  
- [Azure Computer Vision documentation](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/)
- [Spatial Analysis overview](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/concept-spatial-analysis)

If you need details on how to implement these features or want code samples, let me know!
- **Scores:** Accuracy: 3 | Completeness: 4 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response uses 'Azure Computer Vision' instead of the updated 'Azure AI Vision' name, which is the current branding per ground truth. It covers all key features (image analysis, OCR, spatial analysis) and provides helpful, learner-focused explanations and links. Minor omission: does not mention face detection, which is listed in the ground truth.

### Q10: How is business intelligence and reporting integrated in Microsoft Fabric?

- **Ground truth:** Microsoft Fabric includes Power BI as its business intelligence and reporting experience, providing a unified analytics platform where reports and semantic models coexist with data engineering and data science workloads.
- **Response:** To answer your question thoroughly, here's a concise overview:

**Business intelligence (BI) and reporting in Microsoft Fabric** are integrated through several core components and services that enable data-driven insights across the organization. Microsoft Fabric is an end-to-end analytics platform that unifies data engineering, data science, real-time analytics, and business intelligence under one umbrella.

### Key Integration Points:

1. **Power BI Integration**  
   - **Power BI** is natively integrated into Microsoft Fabric as the primary tool for business intelligence and reporting.
   - Users can create, share, and collaborate on interactive reports and dashboards directly within Fabric.
   - Dataflows, datasets, and reports are managed in a unified workspace, streamlining the process from data ingestion to visualization.

2. **OneLake Data Lake**  
   - Fabric uses **OneLake** as a centralized data repository, allowing BI tools to access data from various sources without duplication.
   - Power BI can connect to OneLake, enabling real-time analytics and reporting on data stored across the organization.

3. **Direct Lake Mode**  
   - Power BI in Fabric supports **Direct Lake mode**, which allows reports and dashboards to query data directly from OneLake without the need for data import or caching.
   - This improves performance and ensures users always see the most up-to-date information.

4. **Data Integration and Transformation**  
   - Fabric includes **Data Engineering** and **Data Integration** experiences (like Dataflows and Pipelines) to prepare and transform data for BI.
   - These tools ensure data is clean, modeled, and ready for reporting.

5. **Collaboration and Governance**  
   - Fabric workspaces provide role-based access, version control, and governance features, ensuring BI assets are secure and compliant.
   - Integration with Microsoft 365 enables sharing and collaboration across Teams, Excel, and other apps.

6. **AI and Advanced Analytics**  
   - Fabric integrates AI capabilities, allowing BI reports to include predictive analytics, natural language queries, and automated insights.

### Example Workflow:

- Data is ingested and stored in OneLake.
- Dataflows and pipelines transform and model the data.
- Power BI connects to the modeled data, enabling users to build reports and dashboards.
- Reports are shared and consumed across the organization, with real-time updates and collaboration.

### Learn More

- [Microsoft Fabric documentation](https://learn.microsoft.com/en-us/fabric/)
- [Power BI in Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/power-bi/)
- [Direct Lake mode in Power BI](https://learn.microsoft.com/en-us/fabric/power-bi/direct-lake-mode/)

Let me know if you want a deeper technical walkthrough, a comparison with legacy BI solutions, or guidance on implementing BI in Fabric for your organization!
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response accurately identifies Power BI as the integrated business intelligence and reporting tool in Microsoft Fabric, and explains its role in the unified analytics platform. It covers all key points from the ground truth, including coexistence with data engineering and data science workloads, and expands with relevant details. The tone is learner-focused, clear, and appropriate for training content.

### Q11: What are the core workloads integrated within Microsoft Fabric that an analytics engineer works with daily?

- **Ground truth:** Within the unified Fabric platform—which integrates Data Factory, Data Engineering, Data Science, Data Warehouse, Real-Time Intelligence, Power BI, and OneLake into a single SaaS analytics environment—the analytics engineer's daily work spans several interconnected areas.
- **Response:** Microsoft Fabric is an end-to-end analytics platform that unifies multiple data and analytics workloads into a single SaaS solution. For analytics engineers, the core workloads integrated within Microsoft Fabric that they work with daily include:

---

### 1. **Data Engineering**
- **Lakehouse**: Combines the capabilities of data lakes and data warehouses, allowing analytics engineers to store, process, and analyze large volumes of structured and unstructured data.
- **Notebooks**: Enables interactive data exploration, transformation, and analysis using languages like SQL, Python, or Spark.

### 2. **Data Warehousing**
- **Warehouse**: Provides a scalable, high-performance SQL-based environment for storing and querying structured data. Analytics engineers use this for building and managing data models, running complex queries, and supporting BI workloads.

### 3. **Data Integration**
- **Dataflows**: Allows engineers to create ETL pipelines for ingesting, transforming, and loading data from various sources into Fabric’s storage.
- **Pipeline**: Orchestrates data movement and transformation across different workloads, automating data processes.

### 4. **Real-Time Analytics**
- **KQL Database (Eventstream)**: Supports real-time data ingestion and analysis using Kusto Query Language (KQL), ideal for streaming analytics scenarios.

### 5. **Business Intelligence**
- **Power BI**: Integrated within Fabric, Power BI enables analytics engineers to build, share, and manage interactive reports and dashboards directly on top of Fabric data sources.

---

**Summary Table:**

| Workload           | Description                                      | Typical Tasks for Analytics Engineers           |
|--------------------|--------------------------------------------------|------------------------------------------------|
| Lakehouse          | Unified storage for structured/unstructured data | Data modeling, transformation, analysis        |
| Warehouse          | SQL-based data warehousing                       | Querying, modeling, supporting BI              |
| Dataflows/Pipeline | ETL and orchestration                            | Data ingestion, transformation, automation     |
| KQL Database       | Real-time analytics                              | Streaming data analysis, event processing      |
| Power BI           | Business intelligence                            | Report/dashboard creation, data visualization  |

---

**Daily Activities:**
- Building and maintaining ETL pipelines (Dataflows, Pipelines)
- Modeling and transforming data in Lakehouse and Warehouse
- Analyzing streaming data with KQL Database/Eventstream
- Creating and sharing BI reports with Power BI

**Learn more:**  
- [Microsoft Fabric workloads overview](https://learn.microsoft.com/en-us/fabric/get-started/fabric-workloads)
- [Lakehouse in Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-overview)
- [Warehouse in Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/data-warehouse/warehouse-overview)
- [Real-Time Analytics in Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/real-time-analytics/overview)
- [Power BI in Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/power-bi/overview)

Let me know if you’d like a deeper dive into any specific workload or how they interact!
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response accurately names all core workloads (Data Engineering, Data Warehouse, Data Integration, Real-Time Analytics, Power BI) and describes their roles, matching the ground truth. It also references OneLake implicitly via Lakehouse and provides learner-focused explanations, summary tables, and links, making it comprehensive and appropriate for training content.
