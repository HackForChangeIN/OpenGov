# Overview
OpenGov is a platform for Indian Citizens to understand the proceedings of the government and connect with their representatives in a meaningful manner. 

To than end, our focus is on information collection & visualization and citizen connect.

# Features (Phase 0)
    - Home
        - Recent Parliamentary Activity
        - Recent Social Activity
        - Recent Activity on the platform
    
    - Information Pages
        - Legislators
            - Profile
                - Education
                - Declared Assets
                - Contact Information
                - Constituency

            - Parliamentary Activity 
                - Bill Votes
                - Questions and Answers
                - Attendance            
        
            -     - Social Activity
                - New Mentions
        - Bills
            - Sector Wise*
        
        - Committees
    
    - Search
        - Search Results
        - 
        - 
    - Legislator
        - Login
        - Claim Profile
        - Update his mission / purpose
        - Answer Questions
    
    - Journalist(s)
        - Login / Register
        - Ask Questions
        - Contribute to OpenGov
  
# Application Overview

BASE_URL https://www.opengov.in/

*Legislators*
/legislators
    - An alphabetized list of all the legislators across all terms
    - A citizen can filter this list based on the term, party or constituency and so on

/legislators/:legislator-name
    - Legislator details
        - Background
    - Legislator Activity
        - MPLADS
        - Question & Answers
        - 

*Debates*

*Bills*
/bills
    - An alphabetized list of all the legislators across all terms
    - Citizens can filter this list based on the tags, or year etc.
    - 

*Questions & Answers*
/questions-and-answers
    - An alphabetized list of all the legislators across all terms
    - Citizens can filter this list based topic etc.

*Petitions*
/petitions
/petitions/:petition-title
/petitions/new
    - Idea is to let a citizen create a petition and let other citizens sign it, similar to change.org
    - 

*Committees*
    - Reports