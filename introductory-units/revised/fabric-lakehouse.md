## Describe how a Microsoft Fabric lakehouse organizes data

A Microsoft Fabric lakehouse gives you one place to store raw data and structured data side by side. That matters because analytics work usually starts with messy source data and ends with reporting or exploration. A lakehouse lets you move through that path without switching systems.

The basic idea is simple: keep raw files when you need flexibility, and keep tables when you need reliable querying. With that split, you can preserve source data for later use while also creating a cleaner layer for analysis.

## Separate files from tables

A lakehouse has two main areas: Files and Tables. The Files area is where you keep data in its original form. That might be CSV files, JSON documents, images, or other source content that you still want to process later.

The Tables area is where you store structured data in Delta Lake format. These tables support SQL queries, schema enforcement, and ACID transactions, which makes them better for reporting and repeated analysis. In other words, Files help you keep data flexible, and Tables help you make it dependable.

| Area | Best for |
| --- | --- |
| Files | Raw input, staging, and content you may need to reprocess later. |
| Tables | Structured analytics, reporting, and governed queries. |

That separation also makes your workflow easier to reason about. You can ingest data into Files first, transform it, and then load the results into Tables when you are ready to query it.

## Use Delta Lake for reliable analytics

Delta Lake is the storage layer that gives lakehouse tables their reliability. It adds a transaction log on top of Parquet files, so changes are tracked and previous versions can be queried if needed.

That gives you three practical benefits. First, multiple people can read and write safely. Second, the schema stays consistent. Third, you can update or delete data without treating the lakehouse like a pile of static files.

Those capabilities matter most when your data changes over time. A lakehouse is useful not just because it stores data, but because it keeps that data trustworthy as more people and tools use it.

> [!NOTE]
> The value of a lakehouse is not just storage. It is the ability to keep raw and curated data connected without losing reliability.

## Protect access and extend the data

Once your data is organized, you still need to control who sees it. Fabric supports workspace roles for broad access, item sharing for narrower access, and SQL-level controls such as row-level and column-level security for more specific protection.

That security model lets you share the same lakehouse with different audiences. Analysts can query the tables, report authors can build visuals, and governed teams can restrict access to only the rows or columns they need.

This becomes especially important when the lakehouse feeds other experiences. Well-structured tables can support Power BI, semantic models, and AI features that depend on consistent data. So the real value of a lakehouse is not only storage. It is a reliable base for everything that uses the data next.
