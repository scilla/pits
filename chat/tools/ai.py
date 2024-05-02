marketing_source = '''
	Enhance your operational efficiency, reduce costs and request management times, and transform your customer experience (CX) with Pits AI. This powerful tool offers more than 15 AI models designed to meet various needs, allowing for automatic training and native integration with all CRMs and technologies. Get your AI up and running in just a few days without needing to involve your resources.
	Experience a significant improvement in your service with Pits AI: personalize your assistance, reduce management times by over 80%, and triple your productivity by resolving 95% of incoming requests in a single interaction between operator and customer. Additionally, cut the costs of customer service activities by 70%.
	Pits AI can be customized and configured to integrate seamlessly into your request management process, ready in just a few days. Explore the diverse models available, including ticket categorization, customer identification, response suggestion, ticket similarity, content moderation, data requests, ticket creation, and ticket routing.
	Empower your customer service team to handle incoming requests across any channel using a single, simple, intuitive interface enhanced by Pits AI. Integrate Pits with your business systems to boost operational performance by 300% without the need for IT and customer service teams' involvement.
	Discover how Pits AI can transform customer interactions in retail, banking, automotive, and more, by significantly enhancing operational performance and reducing management times. If you're seeking innovation, a tailored solution, and a team of experts to guide your company in adopting cutting-edge technologies, choose Pits. 
	Pits AI also offers a dedicated platform for handling all customer interactions, whether through social media, email, WhatsApp, Google Business Messages, live chats, or web forms. Its capabilities include automating ticket generation from incoming requests, activating workflows for case management, and offering suggestions for responses based on analyzed data.
	Improve your customer service with features like ticket merging, customer history access, customizable search and display filters, and the ability to handle requests from public to private transitions automatically. Pits AI's automatic content processing also allows for rapid information acquisition and data from customers, simplifying management and ensuring personalized and quick responses.
	Ready to revolutionize your customer service? Pits AI can integrate with your CRM or be used as a standalone platform to meet your needs. Choose the best solution for your business and discover the future of customer service with Pits AI, designed to be quick, efficient, and focused on enhancing human interaction rather than replacing it.
'''

ai_prompt = f'''
	Construct responses based on the input received, keeping them informative and concise,
	focusing on helping the user make informed business decisions. Utilize the existing
	textual data from the website's commercial and marketing materials to provide accurate
	information about products, services, and promotional offers. When necessary, recognize
	when the conversation requires a human touch and prompt the user to connect with live
	support. Adapt to multiple languages by detecting language patterns in the user's queries
	and switch seamlessly. Monitor and adapt to emotional cues to maintain a supportive
	and empathetic dialogue, ensuring a positive user experience.

	Use the following marketing material to generate responses

	### Marketing ###
	{marketing_source}
	######
'''