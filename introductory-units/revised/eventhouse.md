## Get started with an Eventhouse

An Eventhouse gives you a place to work with streaming and time-oriented data in Microsoft Fabric. When you create one, Fabric also creates a default KQL database, which is where you store and query the data.

That setup matters because it gives you a clear starting point. You can ingest data, query it, and share it without first assembling separate infrastructure for storage and analysis.

## Ingest data into a KQL database

The first step is usually to bring data into the database. Eventhouse supports several input paths, including local files, Azure storage, Event Hubs, Fabric Eventstream, OneLake, and common connector-based sources.

That flexibility helps you match the source to the workload. You can land batch data, connect to streaming sources, or pull from another service when you already have data elsewhere.

If you need to reuse data that already exists in another KQL database, you can also create database shortcuts. That lets you query external data without copying it into a second location.

## Query data with KQL

Once the data is in place, you use KQL or T-SQL in a KQL queryset to explore it. KQL is built as a pipeline, so each step refines the results from the previous step.

That means the order of the query matters. You can start with a table, filter the rows, choose the columns you need, and then summarize the results. The pattern is easy to read once you see it in practice.

For example, a simple query might start with a table, filter to the records you want, and then return a small sample. That is a practical way to check the shape of the data before you build something more complex.

```kql
TaxiTrips
| where fare_amount > 20
| project trip_id, pickup_datetime, fare_amount
| take 10
```

This kind of query makes the pipeline idea concrete. You start broad, narrow the result, and then return only the columns and rows you need.

## Make the data easier to use

Eventhouse also helps you make data available beyond the query surface. OneLake availability lets you expose selected databases or tables to other Fabric experiences such as Lakehouse, Warehouse, and Power BI.

That makes the Eventhouse more than a query tool. It becomes part of a broader analytics path where streaming data can feed reporting, exploration, and downstream workloads.

If Copilot is enabled, it can also help you generate KQL. That is useful when you know the question you want to ask but want help turning it into a query.

Now you have the basic Eventhouse flow: ingest data, query it, and make it available to the rest of Fabric.
