#Used Mistral ai api for better accuracy and effective keyword generation.
#Usage (In colab just do the following)
'''!pip install colab-env -qU
    import colab env
    %env MISTRAL_API_KEY=4svjeMnKMRHeZrA1FQ1GOlGSCuMDF667
'''
#Usage (In pycharm just do the following)
'''
Go to edit configuration,
Add a new configuration of python
Select this script
add environment variables as:    MISTRAL_API_KEY    4svjeMnKMRHeZrA1FQ1GOlGSCuMDF667
'''

from mistralai import Mistral
import os

API_KEY = os.getenv("MISTRAL_API_KEY", "")

# Job title and description
job_title = "Technology Specialist - Data & AI"
job_description = """
Are you passionate about helping customers transform their businesses? Microsoft is at the forefront of this transformation; come and help organizations rethink aspects of their business in a way that sets them and their people up for success. We enable customer transformation by leading the global sales strategy, enabling technical sales, driving sales motion innovation and revenue execution for the Data & AI Commercial Solution Area.



The main goal of Microsoft Technology Specialists (TS) is to win the technical decision of customers to purchase and use Microsoft technology and cloud services, for both Relational and Non-Relational scenarios, open source databases and Azure Analytics platform including Azure Cosmos DB, and Microsoft Fabric and AI Platform. The TS is expected to help the customers’ technical evaluators and decision makers to take the best decisions, as well as find new opportunities through their contacts and engagements for sales specialists to pursue. As a TS, you work within a virtual team of technical, partner and consulting resources to help educate your customers at a technical level, demonstrate, and prove our solutions, and win the technical decision, allowing the team to achieve/exceed quarterly sales targets in your accounts. Being part of this team will allow you to maintain and develop your deep technical expertise across Microsoft and non-Microsoft cloud-based technologies.



Microsoft’s mission is to empower every person and every organization on the planet to achieve more. As employees we come together with a growth mindset, innovate to empower others, and collaborate to realize our shared goals. Each day we build on our values of respect, integrity, and accountability to create a culture of inclusion where everyone can thrive at work and beyond.

Qualifications
Required/Minimum Qualifications:
Solid technical pre-sales or technical consulting experience.
Experience from data team (e.g., Data Analyst or Data architect or Data Scientist).
Master's OR Bachelor's Degree in Computer Science, Information Technology, or related field AND solid technical pre-sales or technical consulting experience OR equivalent experience.
General understandings of Microsoft's data portfolio and the platform capabilities.

Additional Or Preferred Qualifications:
Solid experience on AI platform with strong knowledge on Machine Learning, Vector database, new App architecture, RAG.
Certification in relevant technologies or disciplines (e.g. AI-102).
Experience from technical presales team from other data company.



Responsibilities
Lead technical discussions with customers leveraging processes and tools, demos, and programs; using consultative sales methodology and technical expertise to understand the customer needs and demonstrate how Microsoft solutions can address them; establish rules of engagement (e.g., role boundaries, handoff strategies) for extended teams.
Build technical strategy: map the agreed customer vision into a strategy, resolve concerns, prevent & remove technical blockers, validating a strong business case for investment and translated technology complexity into business impact. Work with the customer, account team, and partners to orchestrate a roadmap for implementation using Microsoft Analytics Governance (MAG) framework. Educate our customers on the NoSQL value proposition in general and particularly on Azure Cosmos DB. Empower our customer on AI Discussion and drive conversation around AI Responsible topics.
Design the solution using your technical knowledge, architectural approach, consultancy skills and our methodology to win a customer’s technical decision and meet the customer’s needs. Ensure technical decision makers agree with proposed architecture. Drive POCs/pilots to create momentum for MVPs, infusing key AI technologies where appropriate and being technically proficient to conduct and complete a POC with hands-on-skills. Articulate the end-to-end architecture, including both Apps and Data services (Azure Cosmos DB & OSS DB)
Identify new opportunities within customer engagement.
Be the Trusted advisor and use proactive effort to find and understand customers’ pain points, and design and offer solutions (with business case) to technical leaders.
Be the Voice of Customer to share insights and best practices with Engineering, to remove key blockers and drive product improvements.
Maintain and grow expertise in Data Modernization (Azure Cosmos DB and Open Source DB), Analytics & Data warehousing scenarios including Intelligent Data Platform (Azure SQL DW, Azure Data Lake, Azure Synapse Analytics/Azure Databricks, Power BI), and AI technologies (Azure OpenAI Services, Azure Cognitive Services, Azure Machine Learning) while keeping up to date with market trends and competitive insights; collaborate and share with the Data & AI technical community.
Be an Azure platform evangelist for AI scenarios.
Scale through partners, acting as liaison between the partner and account team and facilitating partner resources and processes; supporting partner technical capacity by identifying skill and resource gaps and providing feedback to internal teams.
Develop customer technical skilling plan in collaboration with customer and account team."""
def postprocess(text):
    lines = text.split('\n')
    word_list = []
    for line in lines:
        line = line.strip()
        if line.startswith('-'):
            word = line[1:]
            word_list.append(word)

    return word_list
# Function to generate keywords
def generate_keywords(job_title, job_description):
    s = Mistral(api_key=API_KEY)

    prompt = f'Generate plain list of keywords without anything else related to the job title "{job_title}" from the following job description: {job_description}'

    res = s.chat.complete(model="mistral-large-latest", messages=[
        {
            "content": prompt,
            "role": "user",
        },
    ])

    if res is not None:
        return res.choices[0].message.content
    else:
        print("Error: No response received.")
        return None

# Generate keywords
keywords = postprocess(generate_keywords(job_title, job_description))
print("Generated Keywords:", keywords)

