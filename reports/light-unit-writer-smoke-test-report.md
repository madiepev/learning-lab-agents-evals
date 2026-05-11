# Smoke Test Report: light-unit-writer

**Date:** 2026-05-11
**Test file:** smoke-test.jsonl
**Total questions:** 11
**Pass rate:** 10/11 (91%)

## Summary

| Criterion | Average | Min | Max |
|-----------|---------|-----|-----|
| Accuracy | 4.4 | 2 | 5 |
| Completeness | 4.5 | 2 | 5 |
| Tone | 5.0 | 5 | 5 |

## Details

### Q1: What platform should developers use to build and deploy AI agents on Microsoft Azure?

- **Ground truth:** Developers should use Microsoft Foundry to build, evaluate, and deploy AI agents on Azure.
- **Response:** Developers use **Azure AI Studio** to build and deploy AI agents on Microsoft Azure. Azure AI Studio provides an integrated platform for creating, training, testing, and deploying AI solutions—including conversational agents, copilots, and generative AI applications. It offers tools for prompt engineering, orchestration, data management, and seamless integration with Azure services.

> [!TIP]
> Azure AI Studio is designed for both code-first and low-code experiences, making it accessible to a wide range of developers and data scientists.

**Learn more:**  
- [Azure AI Studio documentation](https://learn.microsoft.com/en-us/azure/ai-studio/)  
- [Build AI agents with Azure AI Studio](https://learn.microsoft.com/en-us/azure/ai-studio/agents/overview)
- **Scores:** Accuracy: 2 | Completeness: 2 | Tone: 5
- **Verdict:** FAIL
- **Notes:** The response incorrectly identifies Azure AI Studio as the platform for building and deploying AI agents, while the ground truth specifies Microsoft Foundry. The response is detailed and learner-focused, but misses the key product name and associated facts, resulting in low accuracy and completeness scores.

### Q2: What is the Azure service that provides vision, speech, language, and decision AI capabilities?

- **Ground truth:** Azure AI Services provides pre-built AI capabilities including vision, speech, language, and decision APIs.
- **Response:** The Azure service that provides vision, speech, language, and decision AI capabilities is **Azure Cognitive Services**.

Azure Cognitive Services is a collection of pre-built APIs and SDKs that let you add intelligent features to your applications without requiring deep AI expertise. These services cover areas such as:

- **Vision**: Image analysis, object detection, OCR, facial recognition
- **Speech**: Speech-to-text, text-to-speech, speech translation
- **Language**: Text analytics, translation, conversational AI, sentiment analysis
- **Decision**: Anomaly detection, content moderation, personalizer

You can use these services individually or combine them to build rich, AI-powered solutions.
- **Scores:** Accuracy: 4 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response uses 'Azure Cognitive Services' instead of 'Azure AI Services', which is the updated branding. However, the technical details and capabilities are correct and comprehensive. The tone is learner-focused and clear.

### Q3: Which Azure service enables full-text search, semantic search, and vector search over enterprise content?

- **Ground truth:** Azure AI Search enables full-text search, semantic search, and vector search over enterprise content.
- **Response:** Azure Cognitive Search enables full-text search, semantic search, and vector search over enterprise content. This service lets you index, query, and analyze structured and unstructured data, providing advanced search capabilities such as natural language processing, semantic ranking, and similarity search using vectors. Azure Cognitive Search is designed for scenarios where you need to build rich search experiences across documents, databases, or other content sources within your organization.
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response uses 'Azure Cognitive Search,' which is the former name for 'Azure AI Search.' Both refer to the same service, and Microsoft documentation still references both names. The response accurately describes the service's capabilities and is learner-focused.

### Q4: What is the Microsoft unified SaaS analytics platform that brings together data engineering, data warehousing, and business intelligence?

- **Ground truth:** Microsoft Fabric is the unified SaaS analytics platform that integrates data engineering, data warehousing, data science, real-time intelligence, and Power BI.
- **Response:** The Microsoft unified SaaS analytics platform that brings together **data engineering**, **data warehousing**, and **business intelligence** is **Microsoft Fabric**.

**Microsoft Fabric** is an end-to-end analytics platform as a service (SaaS) that unifies data integration, engineering, warehousing, real-time analytics, and business intelligence. It combines capabilities from Power BI, Azure Synapse Analytics, and Azure Data Factory into a single, integrated solution.

> [!NOTE]
> Microsoft Fabric enables organizations to manage the entire analytics lifecycle—from ingesting and transforming data to building reports and dashboards—all within one platform.

**Learn more:**  
- [What is Microsoft Fabric?](https://learn.microsoft.com/en-us/fabric/overview/)  
- [Microsoft Fabric documentation](https://learn.microsoft.com/en-us/fabric/)
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response correctly identifies Microsoft Fabric as the unified SaaS analytics platform and expands on its features, including integration of Power BI, Azure Synapse Analytics, and Azure Data Factory. It covers all key points from the ground truth and uses a learner-focused, informative tone with helpful links.

### Q5: What Azure service uses machine learning to extract text, tables, and key-value pairs from documents?

- **Ground truth:** Azure AI Document Intelligence uses machine learning models to extract structured data including text, tables, and key-value pairs from documents.
- **Response:** Azure Form Recognizer uses machine learning to extract text, tables, and key-value pairs from documents. This service is part of Azure AI Document Intelligence and lets you analyze and process documents such as invoices, receipts, contracts, and forms. Form Recognizer can handle both structured and unstructured documents, providing results like extracted text, detected tables, and identified key-value pairs for downstream automation or analysis.
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response correctly identifies Azure Form Recognizer as the service, notes its integration with Azure AI Document Intelligence, and explains its capabilities. All key points from the ground truth are covered, and the tone is clear and learner-focused.

### Q6: What is the low-code tool in Microsoft Power Platform used to build custom business applications?

- **Ground truth:** Power Apps is the low-code tool within Microsoft Power Platform that enables users to build custom business applications with minimal coding.
- **Response:** The low-code tool in Microsoft Power Platform used to build custom business applications is **Microsoft Power Apps**.

Power Apps lets you create custom apps for your business needs with minimal coding. You can design user interfaces, connect to data sources, automate workflows, and deploy apps across web and mobile devices—all within a visual, drag-and-drop environment. This makes it accessible for both professional developers and business users to quickly build solutions tailored to their organization.
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response correctly identifies Power Apps, explains its low-code nature, and elaborates on its features and accessibility. The tone is learner-focused and clear, matching training content style.

### Q7: What is the Microsoft low-code tool for building and publishing AI-powered chatbots and copilots?

- **Ground truth:** Microsoft Copilot Studio is the low-code tool for building, testing, and publishing AI-powered chatbots and copilots.
- **Response:** The Microsoft low-code tool for building and publishing AI-powered chatbots and copilots is **Microsoft Copilot Studio**.

Copilot Studio lets you create, customize, and deploy conversational AI experiences—including chatbots and copilots—using a visual, low-code interface. You can integrate AI capabilities, connect to data sources, and publish your bots across multiple channels such as Microsoft Teams, websites, and more.

> [!TIP]
> Copilot Studio was formerly known as Power Virtual Agents. It now offers enhanced AI integration and copilot creation features.

**Learn more:**  
- [Microsoft Copilot Studio documentation](https://learn.microsoft.com/en-us/copilot-studio/)  
- [Build AI-powered copilots with Copilot Studio](https://learn.microsoft.com/en-us/copilot-studio/overview)
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response correctly identifies Microsoft Copilot Studio, explains its features, mentions its previous name (Power Virtual Agents), and provides helpful links. The tone is learner-focused and appropriate for training content.

### Q8: Which Azure service provides NLP features such as sentiment analysis, named entity recognition, and conversational language understanding?

- **Ground truth:** Azure AI Language provides NLP features including sentiment analysis, named entity recognition, key phrase extraction, and conversational language understanding.
- **Response:** Azure Cognitive Services provides NLP features such as sentiment analysis, named entity recognition, and conversational language understanding. Specifically, the **Azure Language service** (formerly known as Text Analytics and Language Understanding [LUIS]) offers these capabilities:

- **Sentiment analysis**: Determines the sentiment (positive, negative, neutral, mixed) of text.
- **Named entity recognition**: Identifies entities like people, organizations, locations, dates, and more within text.
- **Conversational language understanding**: Enables applications to understand user intent and extract relevant information from conversations.

You access these features through the Azure Language service APIs, which are part of Azure Cognitive Services.
- **Scores:** Accuracy: 4 | Completeness: 4 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response correctly identifies Azure Language service as the provider of NLP features and mentions its previous names (Text Analytics, LUIS), which is helpful. However, it refers to 'Azure Cognitive Services' as the provider, which is technically the umbrella, not the specific service. It omits 'key phrase extraction' from the list of features. The tone is clear, learner-focused, and appropriate for training content.

### Q9: What Azure service provides image analysis, optical character recognition, and spatial analysis capabilities?

- **Ground truth:** Azure AI Vision provides image analysis, optical character recognition (OCR), face detection, and spatial analysis capabilities.
- **Response:** Azure Cognitive Services provides image analysis, optical character recognition (OCR), and spatial analysis capabilities. Specifically, the **Computer Vision** API within Azure Cognitive Services enables you to analyze images, extract text from images (OCR), and perform spatial analysis such as detecting objects, faces, and their locations within an image.

- **Image analysis**: Identifies objects, people, text, and more in images.
- **Optical character recognition (OCR)**: Extracts printed and handwritten text from images and documents.
- **Spatial analysis**: Detects and analyzes spatial relationships, such as identifying people’s locations in a room or tracking movement (often used in conjunction with Azure Video Analyzer or Computer Vision spatial analysis features).

> [!TIP]
> Azure Cognitive Services Computer Vision API is the primary service for these tasks. For advanced spatial analysis in video streams, Azure Video Analyzer (formerly Azure Media Analytics) and Computer Vision spatial analysis features can be used.

**Learn more:**
- [Azure Cognitive Services Computer Vision](https://learn.microsoft.com/azure/cognitive-services/computer-vision/)
- [Spatial analysis in Azure Cognitive Services](https://learn.microsoft.com/azure/cognitive-services/computer-vision/spatial-analysis-overview)
- [OCR with Computer Vision](https://learn.microsoft.com/azure/cognitive-services/computer-vision/overview-ocr)
- **Scores:** Accuracy: 3 | Completeness: 3 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response uses 'Azure Cognitive Services' and 'Computer Vision API' instead of the updated 'Azure AI Vision' branding, which is the correct and current product name per the ground truth. It covers the main capabilities (image analysis, OCR, spatial analysis) but omits 'face detection' and doesn't clarify the branding change. The tone is learner-focused and appropriate for training content.

### Q10: How is business intelligence and reporting integrated in Microsoft Fabric?

- **Ground truth:** Microsoft Fabric includes Power BI as its business intelligence and reporting experience, providing a unified analytics platform where reports and semantic models coexist with data engineering and data science workloads.
- **Response:** Business intelligence (BI) and reporting are core capabilities integrated throughout Microsoft Fabric, enabling organizations to analyze, visualize, and share data insights across their entire data estate. In the context of a real-world scenario—such as a retail company tracking sales and inventory—Fabric lets you connect data sources, build interactive reports, and empower decision-makers with actionable information. Here, you learn how BI and reporting are woven into Fabric’s architecture, the main tools involved, and the workflow for delivering insights.

| Aspect | Explanation |
|--------|-------------|
| BI tools in Fabric | Power BI is natively integrated, providing data modeling, visualization, and dashboarding directly within Fabric workspaces. |
| Data connectivity | Fabric unifies data from sources like OneLake, Data Warehouses, Lakehouses, and external systems, making it accessible for reporting. |
| Workflow integration | You can build reports on top of data pipelines, notebooks, or real-time streams, supporting end-to-end analytics scenarios. |
| Collaboration & sharing | Reports and dashboards are published, shared, and embedded across Microsoft 365 apps, enabling broad access to insights. |
| Governance & security | Fabric enforces data access controls, lineage tracking, and compliance policies for BI artifacts. |

## Power BI as the central reporting engine

Power BI is the primary BI and reporting tool within Microsoft Fabric. Its deep integration means you can create, edit, and publish reports directly in Fabric workspaces, leveraging data from OneLake, Lakehouses, Data Warehouses, and other sources.

With Power BI, you build interactive dashboards, perform ad-hoc analysis, and visualize data trends. The experience is unified—whether you’re working with structured or unstructured data, you access it through Fabric’s data items and connectors.

:::image type="content" source="./media/fabric-powerbi-integration.png" alt-text="Diagram showing Power BI integrated with Fabric data sources like OneLake, Lakehouse, and Data Warehouse.":::

## Unified data access for reporting

Fabric’s architecture centralizes data storage and access, making it easier to build reports across diverse datasets. OneLake acts as a single data lake for all Fabric workloads, so BI tools can query data without complex movement or duplication.

You connect Power BI reports to Lakehouses, Data Warehouses, and even real-time event streams. This unified access lets you create comprehensive reports that combine historical, operational, and streaming data.

| Data Source | Reporting Integration |
|-------------|----------------------|
| OneLake | Direct query and import for Power BI reports |
| Lakehouse | Semantic models for BI, supporting large-scale analytics |
| Data Warehouse | High-performance reporting with T-SQL and Power BI |
| Real-time streams | Live dashboards and alerts for operational monitoring |

## Collaboration and governance for BI artifacts

Fabric supports collaboration by allowing teams to co-author, share, and embed reports across Microsoft 365 apps like Teams and SharePoint. You manage access through workspace roles and data security policies, ensuring only authorized users view sensitive information.

Governance features include data lineage tracking, audit logs, and compliance controls. These capabilities help organizations maintain trust and accountability for BI and reporting assets.

> [!TIP]
> Use workspace-level permissions and sensitivity labels to protect confidential reports and dashboards.

## End-to-end analytics workflow

BI and reporting in Fabric are part of an end-to-end analytics workflow. You ingest and transform data with pipelines or notebooks, store it in Lakehouses or Data Warehouses, and then build Power BI reports—all within the same platform.

This integration streamlines the process from raw data to actionable insights, reducing complexity and accelerating decision-making.

Now that you understand how business intelligence and reporting are integrated in Microsoft Fabric, you can explore how to build and publish Power BI reports using Fabric’s unified data sources in the next unit.
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response accurately identifies Power BI as the integrated BI and reporting tool in Microsoft Fabric, describes its deep integration, and explains how reports and semantic models coexist with other workloads. It covers all key points from the ground truth and expands with relevant details, maintaining a learner-focused and engaging tone suitable for training content.

### Q11: What are the core workloads integrated within Microsoft Fabric that an analytics engineer works with daily?

- **Ground truth:** Within the unified Fabric platform—which integrates Data Factory, Data Engineering, Data Science, Data Warehouse, Real-Time Intelligence, Power BI, and OneLake into a single SaaS analytics environment—the analytics engineer's daily work spans several interconnected areas.
- **Response:** Analytics engineers working with Microsoft Fabric interact with several core workloads that streamline data integration, transformation, analysis, and visualization. In a typical enterprise scenario—such as a retail company optimizing sales and inventory—these workloads help you move data from source systems, transform it for reporting, and deliver insights to business users. Here, you learn the main Fabric workloads and their roles in an analytics workflow.

| Workload      | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| Data Engineering | Enables large-scale data ingestion, transformation, and orchestration using Spark and pipelines. |
| Data Science     | Supports machine learning, predictive analytics, and model training with integrated ML tools.     |
| Data Warehouse   | Provides scalable, structured storage for analytics-ready data using SQL-based warehouses.         |
| Real-Time Analytics | Handles streaming data, event processing, and near real-time dashboards.                       |
| Power BI         | Delivers interactive reports, dashboards, and self-service analytics for business users.          |
| Data Integration | Connects, moves, and transforms data across sources using pipelines and connectors.               |

## Data engineering for scalable transformation

Data engineering workloads let you build and manage data pipelines that ingest, clean, and transform raw data. With Fabric’s Spark-powered notebooks and pipelines, you automate complex ETL (extract, transform, load) processes. For example, you can schedule nightly jobs to pull sales transactions from point-of-sale systems, standardize formats, and load them into a central data lake.

| Task                | Fabric Feature            |
|---------------------|--------------------------|
| Ingest raw data     | Dataflows, pipelines     |
| Transform datasets  | Spark notebooks, scripts |
| Automate workflows  | Scheduling, triggers     |

This workload forms the backbone of your analytics environment, ensuring data is reliable and ready for downstream analysis.

## Data warehouse for structured analytics

The data warehouse workload provides a centralized, scalable repository for analytics-ready data. Fabric’s SQL-based warehouses let you store cleansed, structured data that supports business intelligence and reporting. You can define tables, relationships, and indexes to optimize query performance.

| Feature             | Benefit                   |
|---------------------|--------------------------|
| SQL compatibility   | Familiar querying         |
| Scalability         | Handles large datasets    |
| Integration         | Connects to Power BI      |

This workload is ideal for storing historical sales, inventory, and customer data, enabling fast, reliable reporting.

## Power BI for visualization and insights

Power BI workloads let you create interactive dashboards and reports that deliver actionable insights to business users. With direct integration to Fabric’s data warehouse and real-time analytics, you can visualize trends, monitor KPIs, and enable self-service exploration.

| Visualization Type  | Use Case                  |
|---------------------|---------------------------|
| Dashboards          | Monitor sales performance |
| Reports             | Analyze inventory trends  |
| Self-service        | Explore customer data     |

Power BI connects seamlessly to other Fabric workloads, making it easy to turn raw data into business value.

## Real-time analytics for immediate action

Real-time analytics workloads process streaming data from sources like IoT devices, social media, or transaction logs. Fabric supports event processing and real-time dashboards, letting you react quickly to operational changes.

| Source              | Real-Time Use Case        |
|---------------------|--------------------------|
| IoT sensors         | Monitor equipment status  |
| Transaction logs    | Detect fraud             |
| Social media        | Track sentiment          |

This workload is essential for scenarios where immediate insights drive business decisions.

Now that you understand the core workloads in Microsoft Fabric, you can explore how these components work together to deliver end-to-end analytics solutions in the next unit.
- **Scores:** Accuracy: 5 | Completeness: 5 | Tone: 5
- **Verdict:** PASS
- **Notes:** The response accurately names and describes all core workloads integrated within Microsoft Fabric, including Data Engineering, Data Science, Data Warehouse, Real-Time Analytics, Power BI, and Data Integration. It provides detailed explanations and practical examples, covering all points from the ground truth. The tone is learner-focused, clear, and appropriate for training content.
