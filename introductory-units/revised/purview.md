## Describe how Microsoft Purview helps protect Copilot data

Microsoft Purview helps you protect the data that Microsoft 365 Copilot and other AI experiences can access. That matters because AI tools are most useful when they can work with business content, but that same access also creates governance and compliance questions.

The basic pattern is straightforward: use protection to control what content can be returned, use compliance tools to monitor how it is used, and use retention to keep or delete it according to policy. That gives you a practical way to support AI use without losing control of sensitive information.

## Start with sensitivity labels

Sensitivity labels are the first layer of protection. When content is labeled and encrypted, Copilot can only return it if the user has the right usage rights, such as View and Extract.

This makes the label part of the access decision, not just a visual marker. If a user can open a file but cannot extract its content, Copilot respects that boundary. The same idea applies to labeled content in SharePoint, OneDrive, and Office apps when the file is in use.

For example, suppose someone opens a proposal labeled Confidential in Word and asks Copilot to summarize it. If the label grants View but not Extract, Copilot can show the file and link to it, but it cannot return the protected text in the response. If the label grants both View and Extract, Copilot can use the content in the response.

| Usage right | What Copilot can do |
| --- | --- |
| View only | Open or reference the file, but not summarize the protected text. |
| View and Extract | Use the protected content in the response, subject to the label policy. |

In practice, that means labels help you protect the content before you have to investigate a problem. They are the simplest way to keep protection attached to the data itself.

If you are setting this up, the practical sequence is:

1. Apply a sensitivity label to the content.
2. Make sure the label includes the right encryption and usage rights.
3. Test the result with a user who has View only and another who has View and Extract.
4. Confirm that Copilot returns only the content each user is allowed to access.

## Use Purview to monitor and investigate activity

Once content is protected, Purview gives you ways to see how Copilot is being used. Auditing records interactions in the unified audit log, including when users interact with Copilot and what files it accessed.

Communication compliance adds another layer by helping you review prompts and responses for risky or inappropriate interactions. Content search and eDiscovery let you find Copilot interactions when you need to investigate or export them.

These tools build on each other. Auditing tells you what happened, compliance helps you review it, and search or eDiscovery helps you retrieve it when you need a deeper look.

If you are investigating one Copilot interaction, the workflow is usually: check the audit log first, review the prompt or response in communication compliance if needed, and then use content search or eDiscovery to collect the related items.

| Tool | What it helps you do |
| --- | --- |
| Auditing | See who interacted with Copilot and what content it touched. |
| Communication compliance | Review prompts and responses for risk or policy issues. |
| Content search and eDiscovery | Find and export interactions when you need a deeper investigation. |

## Retain the content you need

Purview also helps you control how long Copilot interactions are kept. Retention policies can include Copilot interactions, and retention labels can preserve files that Copilot references.

That matters because AI interactions are often part of the business record, not just a temporary chat. If your organization needs to keep those interactions for legal, regulatory, or operational reasons, retention gives you a policy-based way to do it. In practice, this means the message or file can be preserved even after the user moves on, which makes Copilot activity easier to govern later.

Now you have a simple model to work from: label the content, monitor the activity, and retain the records that matter. That sequence gives you a clear path for protecting Copilot use without turning governance into a separate workflow.
