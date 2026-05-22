## Explore Microsoft Purview data protections for AI apps

Microsoft 365 Copilot has the capability to access data stored within your Microsoft 365 tenant, including mailboxes in Exchange Online and documents in SharePoint or OneDrive. It can also use content from a specific file you're working on in the context of an Office app session, regardless of where that file is stored. For example, local storage, network shares, cloud storage, or a USB stick. When files are open by a user within an app, access is often referred to as "data in use."

Before you deploy Microsoft 365 Copilot, make sure you're familiar with the following details that help you strengthen your data protection solutions:

 -  If content grants a user the right to View usage but not the right to Extract content:
     -  The user can open and view the content in the app, but Copilot can't use or summarize the content unless the user also has the Extract usage right. Copilot can only reference the file with a link.
     -  Copilot doesn't summarize this content. However, it can reference it with a link so the user can then open and view the content outside Copilot.
 -  Just like your Office apps, Microsoft 365 Copilot can access sensitivity labels from your organization, but not other organizations. For more information about labeling support across organizations, see [Support for external users and labeled content](/purview/sensitivity-labels-office-apps#support-for-external-users-and-labeled-content).
 -  An advanced PowerShell setting for sensitivity labels can prevent Office apps from sending content to some connected experiences, which includes Microsoft 365 Copilot.
 -  Copilot can't access unopened documents in SharePoint and OneDrive when they're labeled and encrypted with user-defined permissions. Copilot can access these documents for a user when they're open in the app (data in use).
 -  Sensitivity labels that are applied to groups and sites are known as "container labels." The items in groups and sites don't inherit these container labels. As a result, the items don't display their container label in Copilot and can't support sensitivity label inheritance. For example, consider the following scenario for a team labeled as Confidential:
     -  When the chat messages in its Teams channel are summarized, they don't display the sensitivity label in Business Chat (formerly Microsoft Copilot Graph-grounded chat and Microsoft 365 Chat).
     -  Similarly, content from SharePoint site pages and lists don't display the sensitivity label of their container label.
 -  If you're using SharePoint information rights management (IRM) library settings that restrict users from copying text, usage rights are applied when files are downloaded, but not when they're created or uploaded to SharePoint. If you don't want Copilot to summarize these files when they're at rest, use sensitivity labels that apply encryption without the Extract usage right.
 -  Unlike other automatic labeling scenarios, an inherited label when you create new content replaces a lower priority label that was manually applied.
 -  When an inherited sensitivity label can't be applied, the text isn't added to the destination item. For example:
     -  The destination item is read-only.
     -  The destination item is already encrypted and the user doesn't have permission to change the label (which requires Export or Full Control usage rights).
     -  The inherited sensitivity label isn't published to the user.
 -  If a user asks Copilot to create new content from labeled and encrypted items, label inheritance isn't supported when the encryption is configured for user-defined permissions, or if the encryption was applied independently from the label. The user can't send this data to the destination item.
 -  Because [Double Key Encryption (DKE)](/purview/double-key-encryption) is intended for your most sensitive data that's subject to the strictest protection requirements, Copilot can't access this data. As a result, Copilot can't return items protected by DKE. Also, if a DKE item is open (data in use), you can't use Copilot in the app.
 -  Copilot doesn't currently recognize sensitivity labels that protect Teams meetings and chat. For example:
     -  Data returned from a meeting chat or channel chat doesn't display an associated sensitivity label.
     -  Copying chat data can't be prevented for a destination item.
     -  The sensitivity label can't be inherited. This limitation doesn't apply to meeting invites, responses, and calendar events that are protected by sensitivity labels.
 -  For Business Chat:
     -  When meeting invites have a sensitivity label applied, the label is applied to the body of the meeting invite but not to the metadata, such as date and time, or recipients. As a result, questions that are based just on the metadata return data without the label. For example, "What meetings do I have on Monday?" Questions that include the meeting body, such as the agenda, return the data as labeled.
     -  If content is encrypted independently from its applied sensitivity label, and that encryption doesn't grant the user EXTRACT usage rights (but includes the VIEW usage right), the content can be returned by Copilot and therefore sent to a source item. An example of when this configuration can occur is when a user applies Office restrictions from Information Rights Management when a document is labeled "General" and that label doesn't apply encryption.
     -  When the returned content has a sensitivity label applied, users can't see the **Edit in Outlook** option because this feature isn't currently supported for labeled data.
     -  If you're using the extension capabilities that include plugins and the Microsoft Graph Connector, Business Chat doesn't recognize sensitivity labels and encryption that are applied to this data from external sources. Most of the time this limitation doesn't apply because the data is unlikely to support sensitivity labels and encryption, although one exception is Power BI data. You can always disconnect the external data sources by using the Microsoft 365 admin center to turn off those plugins for users and disconnect connections that use a Graph API connector.

App-specific exceptions include:

 -  **Microsoft 365 Copilot in Outlook**. You must have a minimum version of Outlook to use Microsoft 365 Copilot for encrypted items in Outlook:
     -  **Outlook (Classic) for Windows**. Starting with version 2408 in Current Channel
     -  **Outlook for Mac**. Version 16.86.609+
     -  **Outlook for iOS**. Version 4.2420.0+
     -  **Outlook for Android**. Version 4.2420.0+
     -  **Outlook on the web**. Yes
     -  **New Outlook for Windows**. Yes
 -  **Microsoft 365 Copilot in Microsoft Edge and Windows**. Unless data loss prevention (DLP) is used in Edge, Copilot can reference encrypted content from the active browser tab in Edge when that content doesn't grant the user Extract usage rights. For example, the encrypted content is from Office for the web or Outlook for the web.

Administrators should use Microsoft Purview to mitigate and manage the risks associated with AI usage and implement corresponding protection and governance controls. Microsoft Purview is a comprehensive data governance solution designed to provide robust data protection, compliance management, and information governance within Microsoft 365 Copilot and other AI applications.<br>

The following sections examine Microsoft Purview capabilities that provide data security and compliance controls to accelerate your organization's adoption of Microsoft 365 Copilot and other generative AI apps. If you're new to Microsoft Purview, you might also find an overview of the product helpful: [Learn about Microsoft Purview](/purview/purview?azure-portal=true).

For more general information about security and compliance requirements for Microsoft 365 Copilot, see [Data, Privacy, and Security for Microsoft 365 Copilot](/microsoft-365-copilot/microsoft-365-copilot-privacy?azure-portal=true). For Microsoft Copilot, see the Copilot [Privacy and protections](/copilot/privacy-and-protections?azure-portal=true).

### Microsoft Purview strengthens information protection for Copilot

Microsoft recommends using the following Microsoft Purview capabilities to strengthen your data security and compliance for Microsoft 365 Copilot and Microsoft Copilot:

 -  [Sensitivity labels](/purview/sensitivity-labels?azure-portal=true) and content encrypted by Microsoft Purview Information Protection
 -  [Data classification](/purview/data-classification-overview?azure-portal=true)
 -  [Customer Key](/purview/customer-key-overview?azure-portal=true)
 -  [Communication compliance](/purview/communication-compliance?azure-portal=true)
 -  [Auditing](/purview/audit-solutions-overview?azure-portal=true)
 -  [Content search](/purview/ediscovery-content-search-overview?azure-portal=true)
 -  [eDiscovery](/purview/ediscovery?azure-portal=true)
 -  [Retention and deletion](/purview/retention?azure-portal=true)
 -  [Customer Lockbox](/purview/customer-lockbox-requests?azure-portal=true)

Microsoft 365 Copilot uses existing controls to ensure that data stored in your tenant is never returned to the user or used by a large language model (LLM) if the user doesn't have access to that data. Microsoft 365 provides an extra layer of protection when the data has sensitivity labels from your organization applied to the content:

 -  When a file is open in Word, Excel, PowerPoint, or similarly an email or calendar event is open Outlook, the sensitivity of the data is displayed to users in the app with the label name and content markings (such as header or footer text) that are configured for the label.
 -  When the sensitivity label applies encryption, Copilot only returns the data if the user is assigned the Extract and View usage rights.
 -  This protection extends to data stored outside your Microsoft 365 tenant when it's open in an Office app (data in use). For example, local storage, network shares, and cloud storage.

> [!TIP]
> Microsoft recommends that organizations enable sensitivity labels for SharePoint and OneDrive. You should also familiarize yourself with the file types and label configurations that these services can process. When an organization doesn't enable sensitivity labels for these services, the encrypted files that Microsoft 365 Copilot can access are limited to data in use from Office apps on Windows. For instructions, see [Enable sensitivity labels for Office files in SharePoint and OneDrive](/purview/sensitivity-labels-sharepoint-onedrive-files?azure-portal=true).

Additionally, when you use Business Chat (formerly Graph-grounded chat and Microsoft 365 Chat) that can access data from a broad range of content, the sensitivity of labeled data returned by Microsoft 365 Copilot is made visible to users with the sensitivity label displayed for citations and the items listed in the response. Using the sensitivity labels' priority number that's defined in the Microsoft Purview portal, the latest response in Copilot displays the highest priority sensitivity label from the data used for that Copilot chat.

Although compliance administrators define a sensitivity label's priority, a higher priority number usually denotes higher sensitivity of the content, with more restrictive permissions. As a result, Copilot responses are labeled with the most restrictive sensitivity label.

> [!NOTE]
> If items are encrypted by Microsoft Purview Information Protection but don't have a sensitivity label, Microsoft 365 Copilot doesn't return these items to users if the encryption doesn't include the Extract or View usage rights for the user.

Although DLP policies don't yet support interactions for Microsoft 365 Copilot, data classification for sensitive info types and trainable classifiers are supported to identify sensitive data in user prompts to Copilot, and responses.

> [!TIP]
> If you're not already using sensitivity labels, see [Get started with sensitivity labels](/purview/get-started-with-sensitivity-labels?azure-portal=true).

#### Copilot protection with sensitivity label inheritance

When you use Microsoft 365 Copilot to create new content based on an item that has a sensitivity label applied, the sensitivity label from the source file is automatically inherited, along with the label's protection settings.

For example, consider the following Copilot scenarios:

 -  A user selects **Draft with Copilot** in Word and then selects **Reference a file**.
 -  A user selects **Create presentation from file** in PowerPoint.

In each scenario, the source content has the sensitivity label **Confidential\\Anyone (unrestricted)** applied and that label is configured to apply a footer that displays "Confidential". The new content is automatically labeled **Confidential\\Anyone (unrestricted)** with the same footer.

If multiple files are used to create new content, the sensitivity label with the highest priority is used for label inheritance. As with all automatic labeling scenarios, the user can always override and replace an inherited label (or remove, if you're not using [mandatory labeling](/purview/sensitivity-labels-office-apps#require-users-to-apply-a-label-to-their-email-and-documents?azure-portal=true)).

#### Microsoft Purview protection without sensitivity labels

Even if a sensitivity label isn't applied to content, services and products might use the encryption capabilities from the Azure Rights Management service. As a result, Microsoft 365 Copilot can still check for the View and Extract usage rights before returning data and links to a user, but there's no automatic inheritance of protection for new items.

> [!TIP]
> You get the best user experience when you use sensitivity labels to protect your data, and encryption is applied by a label.

Examples of products and services that can use the encryption capabilities from the Azure Rights Management service without sensitivity labels:

 -  Microsoft Purview Message Encryption
 -  Microsoft Information Rights Management (IRM)
 -  Microsoft Rights Management connector
 -  Microsoft Rights Management SDK

For other encryption methods that don't use the Azure Rights Management service:

 -  Copilot doesn't return S/MIME protected emails.
 -  Copilot isn't available in Outlook when an S/MIME protected email is open.
 -  Copilot can't access password-protected documents unless they're already opened by the user in the same app (data in use).
 -  A destination item doesn't inherit passwords.

> [!NOTE]
> As with other Microsoft 365 services, such as eDiscovery and search, items encrypted with [Microsoft Purview Customer Key](/purview/customer-key-overview?azure-portal=true) or [your own root key (BYOK)](/azure/information-protection/byok-price-restrictions?azure-portal=true) are supported and eligible to be returned by Microsoft 365 Copilot.

### Microsoft Purview supports compliance management for Copilot

Use Microsoft Purview compliance capabilities with enterprise data protection to support your risk and compliance requirements for Microsoft 365 Copilot and Microsoft Copilot.

Interactions with Copilot can be monitored for each user in your tenant. As such, you can use Purview's classification (sensitive info types and trainable classifiers), content search, communication compliance, auditing, eDiscovery, and automatic retention and deletion capabilities by using retention policies.

#### Communication compliance

For communication compliance, you can analyze user prompts and Copilot responses to detect inappropriate or risky interactions or sharing of confidential information. For more information, see [Configure a communication compliance policy to detect for Copilot interactions](/purview/communication-compliance-copilot?azure-portal=true).

:::image type="content" source="../media/communication-compliance-microsoft-365-copilot-149574f6.png" alt-text="Screenshot showing the communication compliance page and all the activities associated with policies related to Microsoft 365 Copilot fraud." lightbox="../media/communication-compliance-microsoft-365-copilot-149574f6.png":::


To configure communication compliance policies for Copilot interactions, see [Create and manage communication compliance policies](/purview/communication-compliance-policies?azure-portal=true).

#### Auditing

When auditing is enabled, details are captured in the unified audit log when users interact with Copilot. Events include how and when users interact with Copilot, in which Microsoft 365 service the activity took place, and references to the files stored in Microsoft 365 that Copilot accessed during the interaction. Auditing also captures whether a sensitivity label applied to these files.

In the **Audit** solution from the Microsoft Purview portal, select **Copilot activities** and **Interacted with Copilot**. You can also select **Copilot** as a workload. For this example, review the following screenshot from the compliance portal.

:::image type="content" source="../media/audit-ai-activities-700c1820.png" alt-text="Screenshot showing the Audit page and the new search tab, with the auditing options to identify user interactions with Copilot.":::


To search the audit log for Copilot interactions, see [Search the audit log](/purview/audit-search?azure-portal=true).

#### Content search

For content search, because user prompts to Copilot and responses from Copilot are stored in a user's mailbox, they can be searched and retrieved when the user's mailbox is selected as the source for a search query. Select and retrieve this data from the source mailbox by selecting from the query builder: **Add condition &gt; Type &gt; Equals any of &gt; Add/Remove more options &gt; Copilot interactions**.

To use content search to find Copilot interactions, see [Search for content](/purview/ediscovery-content-search-overview#search-for-content?azure-portal=true).

#### eDiscovery

Similarly for eDiscovery, you use the same query process to select mailboxes and retrieve user prompts to Copilot and responses from Copilot. After the collection is created and sourced to the review phase in eDiscovery (Premium), this data is available for performing all the existing reviewing actions. These collections and review sets can also be put on hold or exported. If you need to delete this data, see [Search for and delete data for Copilot](/purview/ediscovery-search-and-delete-copilot-data?azure-portal=true).

To use eDiscovery for Copilot interactions, see [Microsoft Purview eDiscovery solutions](/purview/ediscovery?azure-portal=true).

#### Retention policies

For retention policies that support automatic retention and deletion, user prompts to Copilot and responses from Copilot are identified by the location Teams chats and Copilot interactions. Previously named just Teams chats, users don't need to be using Teams chat for this policy to apply to them. Any existing retention policies previously configured for Teams chats now automatically include user prompts and responses to and from Microsoft 365 Copilot and Microsoft Copilot:

:::image type="content" source="../media/retention-location-microsoft-365-copilot-74cf212e.png" alt-text="Screenshot showing updated Teams chats retention location to include interactions for Copilot.":::


For detailed information about this retention works, see [Learn about retention for Copilot](/purview/retention-policies-copilot?azure-portal=true).

As with all retention policies and holds, if more than one policy for the same location applies to a user, the principles of retention resolve any conflicts. For example, the data is retained for the longest duration of all the applied retention policies or eDiscovery holds.

To create or change a retention policy for Copilot interactions, see [Create and configure retention policies](/purview/create-retention-policies?azure-portal=true).

#### Retention labels

For retention labels to automatically retain files referenced in Copilot, select the option for cloud attachments with an auto-apply retention label policy: Apply label to cloud attachments and links shared in Exchange, Teams, Viva Engage, and Copilot. As with all retained cloud attachments, the file version at the time it's referenced is retained.

:::image type="content" source="../media/cloud-attachments-copilot-97222b7b.png" alt-text="Screenshot showing updated cloud attachments option for auto-apply retention label to include interactions for Copilot.":::


For detailed information about how this retention works, see [How retention works with cloud attachments](/purview/retention-policies-sharepoint#how-retention-works-with-cloud-attachments?azure-portal=true). To create an auto-apply retention label policy for files referenced in Copilot, see [Automatically apply a retention label to retain or delete content](/purview/apply-retention-labels-automatically?azure-portal=true).