import re

html_file = 'index.html'
with open(html_file, 'r') as f:
    content = f.read()

# Slide 1:
content = content.replace(
    '<!-- Abstract center graphic -->',
    '<div class="slide-image-container"><img src="images/slide_1_img_2.png" class="slide-image hero" alt="Adoptforce Hero"></div>\n            <!-- Abstract center graphic -->'
)

# Slide 3:
content = content.replace(
    '<!-- SLIDE 3: CORE CAPABILITIES -->\n        <div class="slide">\n            <h2 style="margin-top: 2rem;">What We Deliver</h2>\n            <p class="subtitle">Integrated services that move from strategy through architecture, product delivery, and long-term optimization.</p>',
    '<!-- SLIDE 3: CORE CAPABILITIES -->\n        <div class="slide">\n            <h2 style="margin-top: 2rem;">What We Deliver</h2>\n            <p class="subtitle">Integrated services that move from strategy through architecture, product delivery, and long-term optimization.</p>\n            <div class="slide-image-container"><img src="images/slide_3_img_0.png" class="slide-image" alt="Core Capabilities"></div>'
)

# Slide 4:
content = content.replace(
    '<div class="flow-diagram">',
    '<div class="slide-image-container"><img src="images/slide_4_img_0.png" class="slide-image" alt="AppExchange Flow"></div>\n            <div class="flow-diagram">'
)

# Slide 5:
content = content.replace(
    '<div class="flow-diagram" style="margin: 2rem 0;">',
    '<div class="slide-image-container"><img src="images/slide_5_img_0.png" class="slide-image" alt="GTM Acceleration"></div>\n            <div class="flow-diagram" style="margin: 2rem 0;">'
)

# Slide 6:
content = content.replace(
    '<!-- Abstract Phone Mockup -->',
    '<img src="images/slide_6_img_0.png" class="slide-image hero" alt="Mobile Apps" style="max-height: 450px;">\n                    <!-- Abstract Phone Mockup -->'
)

# Slide 7:
content = content.replace(
    '<!-- SLIDE 7: AI & AUTOMATION -->\n        <div class="slide">\n            <h2 style="margin-top: 2rem;">AI-Powered Salesforce Operations</h2>\n            <p class="subtitle" style="margin-bottom: 1.5rem;">Adoptforce integrates the world\'s most powerful AI tools directly into Salesforce workflows — turning your CRM into an intelligent, proactive system of action.</p>',
    '<!-- SLIDE 7: AI & AUTOMATION -->\n        <div class="slide">\n            <h2 style="margin-top: 2rem;">AI-Powered Salesforce Operations</h2>\n            <p class="subtitle" style="margin-bottom: 1.5rem;">Adoptforce integrates the world\'s most powerful AI tools directly into Salesforce workflows — turning your CRM into an intelligent, proactive system of action.</p>\n            <div class="slide-image-container"><img src="images/slide_7_img_0.png" class="slide-image" alt="AI Operations"></div>'
)

# Slide 8:
content = content.replace(
    '<!-- SLIDE 8: DIGITAL TRANSFORMATION APPROACH -->\n        <div class="slide">\n            <h2 style="margin-top: 2rem;">4-Step Transformation Journey</h2>\n            <p class="subtitle">A pragmatic delivery framework designed to discover value, shape the roadmap, build with confidence, and scale with intelligence.</p>',
    '<!-- SLIDE 8: DIGITAL TRANSFORMATION APPROACH -->\n        <div class="slide">\n            <h2 style="margin-top: 2rem;">4-Step Transformation Journey</h2>\n            <p class="subtitle">A pragmatic delivery framework designed to discover value, shape the roadmap, build with confidence, and scale with intelligence.</p>\n            <div class="slide-image-container"><img src="images/slide_8_img_0.png" class="slide-image" alt="Transformation Journey"></div>'
)

# Slide 10:
content = content.replace(
    '<!-- SLIDE 10: INDUSTRIES SERVED -->\n        <div class="slide">\n            <h2 style="margin-top: 2rem;">Industry Expertise</h2>\n            <p class="subtitle" style="margin-bottom: 2rem;">Deep domain knowledge across regulated, high-growth, and operations-intensive sectors — with Salesforce + AI patterns tailored to each.</p>',
    '<!-- SLIDE 10: INDUSTRIES SERVED -->\n        <div class="slide">\n            <h2 style="margin-top: 2rem;">Industry Expertise</h2>\n            <p class="subtitle" style="margin-bottom: 2rem;">Deep domain knowledge across regulated, high-growth, and operations-intensive sectors — with Salesforce + AI patterns tailored to each.</p>\n            <div class="slide-image-container"><img src="images/slide_10_img_0.png" class="slide-image" alt="Industries Served"></div>'
)

# Slide 13:
content = content.replace(
    '<!-- SLIDE 13: SALESFORCE CERTIFICATIONS -->\n        <div class="slide">\n            <h2 style="margin-top: 2rem;">Salesforce Certifications & Enterprise Expertise</h2>\n            <p class="subtitle">Our team holds the industry\'s most comprehensive certification portfolio — spanning every Salesforce cloud, architecture tier, and specialty domain.</p>',
    '<!-- SLIDE 13: SALESFORCE CERTIFICATIONS -->\n        <div class="slide">\n            <h2 style="margin-top: 2rem;">Salesforce Certifications & Enterprise Expertise</h2>\n            <p class="subtitle">Our team holds the industry\'s most comprehensive certification portfolio — spanning every Salesforce cloud, architecture tier, and specialty domain.</p>\n            <div class="slide-image-container"><img src="images/slide_13_img_0.png" class="slide-image" alt="Certifications"></div>'
)

# Slide 14:
content = content.replace(
    '<!-- SLIDE 14: FUTURE VISION -->\n        <div class="slide" style="background: radial-gradient(circle at center, rgba(0, 180, 216, 0.1) 0%, var(--bg-primary) 70%);">\n            <h2 style="margin-top: 2rem; text-align: center;">Where We Are Headed</h2>\n            <p class="subtitle" style="text-align: center; margin: 0 auto 3rem auto;">Adoptforce is actively positioning to lead the next frontier — helping enterprises transition from passive CRM systems of record to proactive, AI-powered systems of action.</p>',
    '<!-- SLIDE 14: FUTURE VISION -->\n        <div class="slide" style="background: radial-gradient(circle at center, rgba(0, 180, 216, 0.1) 0%, var(--bg-primary) 70%);">\n            <h2 style="margin-top: 2rem; text-align: center;">Where We Are Headed</h2>\n            <p class="subtitle" style="text-align: center; margin: 0 auto 3rem auto;">Adoptforce is actively positioning to lead the next frontier — helping enterprises transition from passive CRM systems of record to proactive, AI-powered systems of action.</p>\n            <div class="slide-image-container"><img src="images/slide_14_img_0.png" class="slide-image" alt="Future Vision"></div>'
)

# Slide 15:
content = content.replace(
    '<!-- SLIDE 15: WHY ADOPTFORCE (DIFFERENTIATORS) -->\n        <div class="slide">\n            <h2 style="margin-top: 2rem;">Why Choose Adoptforce</h2>\n            <p class="subtitle">Enterprise-grade delivery capability with the speed and agility to help your team launch, iterate, and scale — without slowing the business.</p>',
    '<!-- SLIDE 15: WHY ADOPTFORCE (DIFFERENTIATORS) -->\n        <div class="slide">\n            <h2 style="margin-top: 2rem;">Why Choose Adoptforce</h2>\n            <p class="subtitle">Enterprise-grade delivery capability with the speed and agility to help your team launch, iterate, and scale — without slowing the business.</p>\n            <div class="slide-image-container"><img src="images/slide_15_img_0.png" class="slide-image" alt="Why Choose Us"></div>'
)

with open(html_file, 'w') as f:
    f.write(content)
