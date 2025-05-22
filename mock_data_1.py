"""
Mock data scenarios for testing all variations of the sales agent system.
This file contains comprehensive test cases covering:
- Basic scenarios (email/SMS with/without sender)
- Edge cases (empty data, invalid links, special characters)
- Industry-specific scenarios
- Contact name variations
- Knowledge base variations
- Chat history variations
- Extreme edge cases
"""

MOCK_DATA = {
    # =============================================================================
    # BASIC SCENARIOS
    # =============================================================================
    "basic_email_no_sender": {
        "global_context": "CloudSync Pro helps SaaS companies reduce customer churn through AI-powered user behavior analysis and automated retention campaigns. We specialize in companies with 1000+ users experiencing high churn rates.",
        "company_info": "CloudSync Pro - AI-powered customer retention platform. Founded 2019. 200+ SaaS clients. Team of 50+ engineers and data scientists. Based in San Francisco.",
        "knowledge_base": "Recent client success: Helped TechStart reduce churn from 12% to 6.5% in 6 months, saving $2.4M annually. Platform integrates with Salesforce, HubSpot, Intercom. Pricing starts at $299/month for up to 5000 users.",
        "contact_info": "Sarah Johnson, VP of Customer Success at DataFlow Inc. Email: sarah.johnson@dataflow.com. Company: B2B SaaS platform, 2500 users, currently experiencing 15% monthly churn rate. Based in Austin, TX.",
        "chat_history": "No previous contact. Cold outreach.",
        "calendly_link": "https://calendly.com/demo-booking-cloudsync",
        "sender_info": "",  # No sender name - should use company only
        "channel": "email"
    },

    "basic_sms_with_sender": {
        "global_context": "MarketingBoost AI automates content creation and social media management for e-commerce brands, increasing engagement and reducing content creation time.",
        "company_info": "MarketingBoost AI - Content automation platform for e-commerce. Founded 2020. 150+ e-commerce clients. Team of 30+ marketers and engineers. Based in New York.",
        "knowledge_base": "Recent success: Helped FashionForward increase social engagement by 75% and sales by 30% in 4 months. Platform creates product descriptions, social posts, email campaigns. Integrates with Shopify, WooCommerce. Pricing: $199/month.",
        "contact_info": "Mike Chen, Marketing Director at StyleHub Store. Email: mike@stylehub.com. Phone: +1-555-0123. Company: E-commerce fashion retailer, struggling with content creation bandwidth, posting inconsistently on social media.",
        "chat_history": "No previous contact. Cold outreach.",
        "calendly_link": "https://calendly.com/marketingboost-demo",
        "sender_info": "Jessica Rodriguez",  # Sender name provided
        "channel": "sms"
    },

    "basic_email_with_sender": {
        "global_context": "SecureCloud Enterprise provides cybersecurity solutions for mid-market companies, preventing security breaches through AI-powered threat detection and automated response systems.",
        "company_info": "SecureCloud Enterprise - Cybersecurity platform for mid-market. Founded 2018. 300+ clients protected. Team of 75+ security experts. SOC 2 Type II certified. Based in Seattle.",
        "knowledge_base": "Recent case: Protected ManufactureCorp from 47 attack attempts last quarter, saving estimated $3.2M in potential damages. 24/7 monitoring, automated threat response, compliance reporting. Pricing: $199/user/month.",
        "contact_info": "Jennifer Walsh, IT Director at TechManufacturing Ltd. Email: j.walsh@techmanufacturing.com. Company: Manufacturing company, 150 employees, recently experienced minor security incident, needs better protection.",
        "chat_history": "No previous contact. Cold outreach.",
        "calendly_link": "https://calendly.com/securecloud-consultation",
        "sender_info": "Alex Thompson",  # Sender name provided
        "channel": "email"
    },

    "basic_sms_no_sender": {
        "global_context": "DataInsights Pro helps businesses make better decisions through advanced analytics and reporting dashboards.",
        "company_info": "DataInsights Pro - Business analytics platform. Founded 2021. 100+ enterprise clients. Team of 25+ data scientists. Based in Chicago.",
        "knowledge_base": "Recent implementation: Helped RetailChain optimize inventory management, reducing waste by 25% and improving profit margins. Platform provides real-time dashboards, predictive analytics, custom reporting. Pricing: $149/month per user.",
        "contact_info": "Robert Martinez, Operations Manager at Local Restaurant Chain. Email: r.martinez@localrestaurants.com. Company has 5 locations, struggles with inventory management and waste.",
        "chat_history": "No previous contact. Cold outreach.",
        "calendly_link": "https://calendly.com/datainsights-demo",
        "sender_info": "",  # No sender name
        "channel": "sms"
    },

    # =============================================================================
    # CONTACT NAME VARIATIONS
    # =============================================================================
    "no_contact_name_email": {
        "global_context": "InventoryTracker Pro automates inventory management for retail businesses, preventing stockouts and reducing excess inventory costs.",
        "company_info": "InventoryTracker Pro - Inventory management software. Founded 2020. 200+ retail stores served. Team of 30+ retail tech specialists. Based in Atlanta.",
        "knowledge_base": "Recent optimization: SportingGoods Store reduced stockouts by 90% and excess inventory by 40%. Features include automated reordering, demand forecasting, supplier integration. Pricing: $99/month per location.",
        "contact_info": "Company: Electronics Retail Chain. Email: info@electronicschain.com. Website: www.electronicschain.com. No specific contact name provided. Company has 8 locations, struggles with inventory management across stores.",
        "chat_history": "No previous contact. Cold outreach.",
        "calendly_link": "https://calendly.com/inventorytracker-demo",
        "sender_info": "Maria Garcia",
        "channel": "email"
    },

    "partial_contact_name_sms": {
        "global_context": "WebSecurity Shield protects websites from cyber attacks through automated monitoring and threat prevention.",
        "company_info": "WebSecurity Shield - Website security platform. Founded 2019. 400+ websites protected. Team of 50+ cybersecurity experts. Based in Austin.",
        "knowledge_base": "Recent protection: E-commerce site blocked 250+ malicious attacks in one month, preventing potential data breach. Features include malware scanning, firewall protection, SSL monitoring. Pricing: $29/month per website.",
        "contact_info": "J. Rodriguez, Web Developer at CreativeDesign Agency. Email: j.rodriguez@creativedesign.com. Agency manages 20+ client websites, recently had one site compromised.",
        "chat_history": "No previous contact. Cold outreach.",
        "calendly_link": "https://calendly.com/websecurity-consultation",
        "sender_info": "Kevin Park",
        "channel": "sms"
    },

    "unusual_contact_name_email": {
        "global_context": "AI-VideoGen creates personalized video content for marketing campaigns using artificial intelligence.",
        "company_info": "AI-VideoGen - Automated video creation platform. Founded 2022. 80+ marketing agencies as clients. Team of 20+ AI engineers. Based in Los Angeles.",
        "knowledge_base": "Recent success: Helped CreativeAgency produce 500+ personalized videos, increasing campaign engagement by 60%. Platform supports multiple languages, custom branding, bulk generation. Pricing: $99/month for unlimited videos.",
        "contact_info": "Dr. Maria-Elena Gonzalez-Smith, Chief Marketing Officer at InnovativeTech Solutions. Email: me.gonzalez@innovativetech.com. Company specializes in B2B software, looking to modernize their video marketing approach.",
        "chat_history": "No previous contact. Cold outreach.",
        "calendly_link": "https://calendly.com/ai-videogen-demo",
        "sender_info": "David Kim",
        "channel": "email"
    },

    "single_name_contact": {
        "global_context": "EventPlanner Pro manages event registration, ticketing, and attendee communication for corporate events and conferences.",
        "company_info": "EventPlanner Pro - Event management platform. Founded 2021. 150+ events managed. Team of 25+ event specialists. Based in Las Vegas.",
        "knowledge_base": "Recent event: TechConf 2024 managed 5000+ attendees with 99% satisfaction rate. Features include registration pages, payment processing, check-in app, networking tools. Pricing: $199/month plus $2 per ticket.",
        "contact_info": "Madonna, Event Coordinator at CorporateEvents LLC. Email: madonna@corporateevents.com. Company organizes 50+ corporate events annually, currently using multiple disconnected tools.",
        "chat_history": "No previous contact. Cold outreach.",
        "calendly_link": "https://calendly.com/eventplanner-pro-demo",
        "sender_info": "Jennifer Smith",
        "channel": "email"
    },

    # =============================================================================
    # EMPTY/MINIMAL DATA SCENARIOS
    # =============================================================================
    "minimal_all_empty": {
        "global_context": "",
        "company_info": "",
        "knowledge_base": "",
        "contact_info": "",
        "chat_history": "",
        "calendly_link": "",
        "sender_info": "",
        "channel": "email"
    },

    "minimal_only_company": {
        "global_context": "",
        "company_info": "TechSolutions Inc - Software development company. Founded 2018. Based in Portland.",
        "knowledge_base": "",
        "contact_info": "",
        "chat_history": "",
        "calendly_link": "https://calendly.com/techsolutions-demo",
        "sender_info": "",
        "channel": "sms"
    },

    "minimal_only_contact": {
        "global_context": "",
        "company_info": "",
        "knowledge_base": "",
        "contact_info": "John Doe, CEO at StartupCorp. Email: john@startupcorp.com. Looking for business solutions.",
        "chat_history": "",
        "calendly_link": "https://calendly.com/meeting",
        "sender_info": "",
        "channel": "email"
    },

    "minimal_only_global_context": {
        "global_context": "We help businesses grow through technology solutions and digital transformation.",
        "company_info": "",
        "knowledge_base": "",
        "contact_info": "",
        "chat_history": "",
        "calendly_link": "https://calendly.com/consultation",
        "sender_info": "Mike Johnson",
        "channel": "sms"
    },

    # =============================================================================
    # CALENDLY LINK VARIATIONS
    # =============================================================================
    "invalid_calendly_link": {
        "global_context": "WebDesign Pro creates modern, responsive websites for small businesses.",
        "company_info": "WebDesign Pro - Website development agency. Founded 2020. 150+ websites built. Team of 12+ designers and developers. Based in Miami.",
        "knowledge_base": "Recent project: Built e-commerce site for LocalStore, increasing online sales by 200% in 3 months. Specializes in Shopify, WordPress, custom development. Pricing: $2,500 for basic website.",
        "contact_info": "Amanda Rodriguez, Owner of Boutique Fashion Store. Email: amanda@boutiquefashion.com. Looking to create first e-commerce website.",
        "chat_history": "No previous contact. Cold outreach.",
        "calendly_link": "not-a-valid-url",  # Invalid URL
        "sender_info": "Carlos Martinez",
        "channel": "email"
    },

    "missing_calendly_link": {
        "global_context": "FitnessApp Pro helps gym owners manage memberships and track member progress through mobile app integration.",
        "company_info": "FitnessApp Pro - Gym management software. Founded 2021. 75+ gyms using platform. Team of 15+ fitness tech specialists. Based in Denver.",
        "knowledge_base": "Recent implementation: PowerGym increased member retention by 40% and reduced admin time by 60%. Features include member check-ins, progress tracking, payment processing. Pricing: $89/month per location.",
        "contact_info": "Robert Johnson, Owner of CrossFit Denver. Email: rob@crossfitdenver.com. Currently using spreadsheets to track members, looking for better solution.",
        "chat_history": "No previous contact. Cold outreach.",
        "calendly_link": "",  # Empty calendly link
        "sender_info": "Lisa Chen",
        "channel": "sms"
    },

    "malformed_calendly_link": {
        "global_context": "PhotoEditor AI enhances photos automatically using artificial intelligence for photographers and content creators.",
        "company_info": "PhotoEditor AI - Photo enhancement platform. Founded 2022. 500+ photographers using service. Team of 15+ AI specialists. Based in San Diego.",
        "knowledge_base": "Recent results: Wedding photographer improved photo quality by 80% and reduced editing time by 70%. Features include automatic color correction, noise reduction, portrait enhancement. Pricing: $49/month for unlimited edits.",
        "contact_info": "Ashley Miller, Professional Photographer at Miller Photography Studio. Email: ashley@millerphotos.com. Spends 10+ hours weekly editing photos manually.",
        "chat_history": "No previous contact. Cold outreach.",
        "calendly_link": "https://invalid-calendly-url-missing-com/demo",  # Malformed URL
        "sender_info": "Ryan Taylor",
        "channel": "email"
    },

    # =============================================================================
    # CHAT HISTORY VARIATIONS
    # =============================================================================
    "with_previous_contact": {
        "global_context": "LegalTech AI automates contract review and legal document analysis for law firms and corporate legal departments.",
        "company_info": "LegalTech AI - Legal automation platform. Founded 2019. 200+ law firms as clients. Team of 40+ legal tech experts. Based in Washington DC.",
        "knowledge_base": "Recent case study: BigLaw Firm reduced contract review time by 80% and caught 95% more compliance issues. Platform supports multiple contract types, risk assessment, clause library. Pricing: $199/user/month.",
        "contact_info": "Patricia Williams, General Counsel at MegaCorp Industries. Email: p.williams@megacorp.com. Company handles 500+ contracts monthly, struggling with review bottlenecks.",
        "chat_history": "Previous email sent 2 weeks ago introducing our platform. Contact opened email but didn't respond. Follow-up call scheduled but contact didn't answer.",
        "calendly_link": "https://calendly.com/legaltech-ai-demo",
        "sender_info": "Michael Thompson",
        "channel": "email"
    },

    "multiple_touchpoints": {
        "global_context": "CloudBackup Enterprise provides automated data backup and disaster recovery solutions for businesses.",
        "company_info": "CloudBackup Enterprise - Data protection platform. Founded 2018. 500+ businesses protected. Team of 60+ cloud engineers. 99.9% uptime guarantee. Based in Austin.",
        "knowledge_base": "Recent recovery: Helped ConstructionCorp recover from ransomware attack in 4 hours, preventing $500K in downtime costs. Features include real-time backup, one-click recovery, compliance reporting. Pricing: $49/month per TB.",
        "contact_info": "Steven Martinez, IT Manager at ManufacturingPlus. Email: s.martinez@manufacturingplus.com. Company experienced data loss incident last month, urgently needs backup solution.",
        "chat_history": "1st contact: LinkedIn message sent, got positive response. 2nd contact: Phone call, discussed needs briefly. 3rd contact: Sent proposal via email. Contact requested demo but hasn't scheduled yet.",
        "calendly_link": "https://calendly.com/cloudbackup-demo",
        "sender_info": "Rachel Green",
        "channel": "email"
    },

    "negative_previous_interaction": {
        "global_context": "CyberTraining Academy provides cybersecurity training and certification programs for IT professionals.",
        "company_info": "CyberTraining Academy - Cybersecurity education platform. Founded 2020. 1000+ professionals certified. Team of 20+ cybersecurity instructors. Based in Washington DC.",
        "knowledge_base": "Recent success: TechCorp's IT team achieved 100% certification rate, improving security posture significantly. Programs include hands-on labs, expert instruction, career placement assistance. Pricing: $299/course or $999/year unlimited access.",
        "contact_info": "James Wilson, IT Director at SecureBank Corp. Email: j.wilson@securebank.com. Bank requires all IT staff to have cybersecurity certifications within 6 months.",
        "chat_history": "Previous outreach attempt resulted in contact expressing they were 'not interested at this time' and asking to be removed from communications. That was 6 months ago.",
        "calendly_link": "https://calendly.com/cybertraining-consultation",
        "sender_info": "Sandra Kim",
        "channel": "email"
    },

    "warm_referral": {
        "global_context": "ProjectManager Elite helps construction companies manage projects, track progress, and coordinate teams more effectively.",
        "company_info": "ProjectManager Elite - Construction project management software. Founded 2019. 300+ construction companies using platform. Team of 40+ construction tech specialists. Based in Houston.",
        "knowledge_base": "Recent project: SkyHigh Construction completed 20% more projects on time and reduced costs by 15%. Features include Gantt charts, resource allocation, mobile apps for field teams, budget tracking. Pricing: $79/user/month.",
        "contact_info": "Tom Anderson, Project Manager at BuildRight Construction. Email: t.anderson@buildright.com. Company manages 15+ concurrent construction projects, struggling with coordination and delays.",
        "chat_history": "Contact was referred by our existing client, MegaBuild Inc. MegaBuild's PM spoke highly of our platform during industry conference. Contact expressed strong interest in scheduling demo.",
        "calendly_link": "https://calendly.com/projectmanager-elite-demo",
        "sender_info": "Marcus Rodriguez",
        "channel": "email"
    },

    # =============================================================================
    # SENDER INFO VARIATIONS
    # =============================================================================
    "long_sender_name": {
        "global_context": "E-commerce Analytics tracks customer behavior and optimizes online store performance for retail businesses.",
        "company_info": "E-commerce Analytics - Retail optimization platform. Founded 2020. 300+ online stores optimized. Team of 35+ data analysts. Based in San Francisco.",
        "knowledge_base": "Recent optimization: OnlineFashion increased conversion rate by 45% and average order value by 30%. Platform provides heat maps, A/B testing, customer journey analysis. Pricing: $149/month for standard plan.",
        "contact_info": "Jennifer Thompson-Rodriguez, E-commerce Director at TrendyClothing Co. Email: j.thompson@trendyclothing.com. Store traffic is high but conversion rates are low.",
        "chat_history": "No previous contact. Cold outreach.",
        "calendly_link": "https://calendly.com/ecommerce-analytics-demo",
        "sender_info": "Alexandra Marie Constantinopolous-Jefferson",  # Very long name
        "channel": "email"
    },

    "sender_with_title": {
        "global_context": "HR-AutoPilot streamlines recruitment and employee onboarding processes through intelligent automation.",
        "company_info": "HR-AutoPilot - Human resources automation. Founded 2021. 150+ HR departments using platform. Team of 25+ HR tech specialists. Based in Chicago.",
        "knowledge_base": "Recent implementation: TechStartup reduced hiring time by 70% and improved new hire satisfaction by 85%. Features include applicant tracking, automated scheduling, digital onboarding. Pricing: $99/user/month.",
        "contact_info": "Thomas Anderson, VP of Human Resources at GrowthCorp. Email: t.anderson@growthcorp.com. Company is rapidly scaling and struggling with manual HR processes.",
        "chat_history": "No previous contact. Cold outreach.",
        "calendly_link": "https://calendly.com/hr-autopilot-consultation",
        "sender_info": "Dr. Sarah Williams, VP of Sales",  # Sender with title
        "channel": "sms"
    },

    "sender_with_credentials": {
        "global_context": "FinanceTracker Pro provides accounting and financial management software for small and medium businesses.",
        "company_info": "FinanceTracker Pro - Financial management platform. Founded 2018. 400+ businesses managing finances. Team of 30+ financial software experts. Based in New York.",
        "knowledge_base": "Recent implementation: LocalCafe streamlined bookkeeping and reduced tax preparation time by 80%. Features include invoicing, expense tracking, financial reporting, tax integration. Pricing: $39/month for basic plan.",
        "contact_info": "Mark Johnson, Owner of Johnson's Auto Repair Shop. Email: mark@johnsonsauto.com. Shop has been using paper receipts and Excel spreadsheets for accounting.",
        "chat_history": "No previous contact. Cold outreach.",
        "calendly_link": "https://calendly.com/financetracker-demo",
        "sender_info": "CPA Jennifer Martinez, MBA",  # Sender with credentials
        "channel": "email"
    },

    # =============================================================================
    # INDUSTRY-SPECIFIC SCENARIOS
    # =============================================================================
    "healthcare_industry": {
        "global_context": "MedRecord AI digitizes and organizes patient records for healthcare providers, ensuring HIPAA compliance and improving patient care efficiency.",
        "company_info": "MedRecord AI - Healthcare data management. Founded 2019. 100+ clinics and hospitals served. HIPAA certified. Team of 30+ healthcare IT specialists. Based in Boston.",
        "knowledge_base": "Recent implementation: City Hospital reduced patient record retrieval time by 90% and eliminated filing errors. Features include voice-to-text transcription, automated coding, secure cloud storage. Pricing: $149/provider/month.",
        "contact_info": "Dr. Emily Parker, Chief Medical Officer at Regional Medical Center. Email: e.parker@regionalmed.com. Hospital handles 1000+ patients daily, struggling with paper-based records system.",
        "chat_history": "No previous contact. Cold outreach.",
        "calendly_link": "https://calendly.com/medrecord-ai-consultation",
        "sender_info": "Marcus Johnson",
        "channel": "email"
    },

    "education_industry": {
        "global_context": "EduTech Learning creates interactive online courses and learning management systems for educational institutions.",
        "company_info": "EduTech Learning - Educational technology platform. Founded 2020. 200+ schools using platform. Team of 40+ education specialists. Based in Portland.",
        "knowledge_base": "Recent success: Lincoln High School improved student engagement by 60% and test scores by 25% using our interactive modules. Platform includes video lectures, quizzes, progress tracking, parent portals. Pricing: $5/student/month.",
        "contact_info": "Principal Maria Gonzalez, Roosevelt Elementary School. Email: m.gonzalez@rooseveltelementary.edu. School transitioning to hybrid learning model, needs better online platform.",
        "chat_history": "No previous contact. Cold outreach.",
        "calendly_link": "https://calendly.com/edutech-learning-demo",
        "sender_info": "Jennifer Park",
        "channel": "email"
    },

    "real_estate_industry": {
        "global_context": "PropertyManager Pro automates property management tasks including rent collection, maintenance requests, and tenant communication for real estate professionals.",
        "company_info": "PropertyManager Pro - Real estate management software. Founded 2018. 400+ property managers using platform. Team of 25+ real estate tech experts. Based in Phoenix.",
        "knowledge_base": "Recent case: Sunset Properties reduced administrative time by 50% and improved tenant satisfaction by 40%. Features include online rent payments, maintenance tracking, financial reporting. Pricing: $25/unit/month.",
        "contact_info": "Richard Davis, Property Manager at Metro Apartments LLC. Email: r.davis@metroapartments.com. Manages 150 units across 5 properties, using outdated manual processes.",
        "chat_history": "No previous contact. Cold outreach.",
        "calendly_link": "https://calendly.com/propertymanager-pro-demo",
        "sender_info": "",  # No sender name
        "channel": "sms"
    },

    "manufacturing_industry": {
        "global_context": "ManufacturingOptimizer streamlines production processes and reduces waste for manufacturing companies through IoT sensors and AI analytics.",
        "company_info": "ManufacturingOptimizer - Industrial automation platform. Founded 2019. 150+ factories optimized. Team of 50+ industrial engineers. Based in Detroit.",
        "knowledge_base": "Recent optimization: SteelWorks Inc reduced production waste by 30% and increased efficiency by 25%. Platform includes real-time monitoring, predictive maintenance, quality control automation. Pricing: $199/machine/month.",
        "contact_info": "Carol Peterson, Operations Director at Precision Manufacturing Corp. Email: c.peterson@precisionmfg.com. Factory produces automotive parts, experiencing quality issues and downtime.",
        "chat_history": "No previous contact. Cold outreach.",
        "calendly_link": "https://calendly.com/manufacturing-optimizer-consultation",
        "sender_info": "David Chen",
        "channel": "email"
    },

    # =============================================================================
    # EXTREME EDGE CASES
    # =============================================================================
    "very_long_contact_info": {
        "global_context": "RestaurantTech POS provides advanced point-of-sale systems with inventory management, staff scheduling, and customer loyalty programs for restaurants.",
        "company_info": "RestaurantTech POS - Restaurant management platform. Founded 2019. 250+ restaurants using system. Team of 35+ hospitality tech specialists. Based in New Orleans.",
        "knowledge_base": "Recent implementation: Cajun Kitchen increased order accuracy by 95% and reduced wait times by 30%. System includes mobile ordering, kitchen display, analytics dashboard, loyalty program integration. Pricing: $79/month per terminal.",
        "contact_info": "Chef Antoine Baptiste-Boudreaux III, Owner and Head Chef at The Authentic Louisiana Creole Kitchen & Seafood House Restaurant located at 1234 Magazine Street in the historic French Quarter district of New Orleans, Louisiana. Email: chef.antoine@authenticcreole.com. Phone: +1-504-555-0199. Restaurant has been family-owned for 3 generations, currently using old cash register system, serves 200+ customers daily, specializes in traditional Creole and Cajun cuisine, has 15 staff members, open 7 days a week from 11 AM to 10 PM, looking to modernize operations while maintaining authentic character.",
        "chat_history": "No previous contact. Cold outreach.",
        "calendly_link": "https://calendly.com/restauranttech-pos-demo",
        "sender_info": "Marie Thibodaux",
        "channel": "email"
    },

    "special_characters_in_names": {
        "global_context": "MobileApp Builder helps businesses create custom mobile apps without coding knowledge.",
        "company_info": "MobileApp Builder - No-code app development platform. Founded 2021. 150+ apps published. Team of 20+ mobile developers. Based in Silicon Valley.",
        "knowledge_base": "Recent launch: Local Pizza Shop app increased online orders by 80% and customer retention by 50%. Platform includes drag-and-drop interface, push notifications, payment integration. Pricing: $99/month for basic app.",
        "contact_info": "François O'Brien-Müller, CEO at Café François & Co. Email: francois@cafefrancois.com. Owns chain of 3 coffee shops, wants to create loyalty app for customers.",
        "chat_history": "No previous contact. Cold outreach.",
        "calendly_link": "https://calendly.com/mobileapp-builder-consultation",
        "sender_info": "José María Rodríguez-Santos",  # Special characters in sender name
        "channel": "sms"
    },

    "numbers_in_company_names": {
        "global_context": "24/7 Support AI provides automated customer service chatbots that handle common inquiries and escalate complex issues to human agents.",
        "company_info": "24/7 Support AI - Customer service automation. Founded 2020. 180+ businesses automated. Team of 30+ AI specialists. Based in Seattle.",
        "knowledge_base": "Recent deployment: TechCorp's chatbot handles 85% of customer inquiries automatically, reducing support costs by 60%. Features include natural language processing, multi-language support, CRM integration. Pricing: $199/month for up to 1000 conversations.",
        "contact_info": "Sarah Johnson, Customer Service Manager at 123-Tech Solutions Inc. Email: sarah@123techsolutions.com. Company receives 500+ support tickets daily, current team is overwhelmed.",
        "chat_history": "No previous contact. Cold outreach.",
        "calendly_link": "https://calendly.com/24-7-support-ai-demo",
        "sender_info": "Alex Johnson-2024",  # Numbers in sender name
        "channel": "email"
    },

    # =============================================================================
    # KNOWLEDGE BASE VARIATIONS
    # =============================================================================
    "no_knowledge_base": {
        "global_context": "SocialMedia Scheduler automates social media posting across multiple platforms for businesses and influencers.",
        "company_info": "SocialMedia Scheduler - Social media automation tool. Founded 2022. 100+ users actively posting. Team of 15+ social media experts. Based in Nashville.",
        "knowledge_base": "",  # Empty knowledge base
        "contact_info": "Instagram influencer @FashionGuru with 50K followers. Email: contact@fashionguru.com. Currently posting manually, wants to optimize posting schedule.",
        "chat_history": "Found contact through Instagram, no previous business contact.",
        "calendly_link": "https://calendly.com/socialmedia-scheduler-demo",
        "sender_info": "Taylor Swift Johnson",  # Potentially confusing name
        "channel": "email"
    }

}