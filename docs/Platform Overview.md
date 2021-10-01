# Overview
OpenGov is a platform for Indian Citizens to understand the proceedings of the government and connect with their representatives in a meaningful manner. 
To that end, our focus is on information collection & visualization and citizen connect. India Insider is the tools which actually visualize all the parlimentary information like bills, debates, questions, parliamentary commites along with details of all the legislators. We are trying to make information about the  govt. more accessible, understandable, and actionable for public.

# Features of India Insider (Phase 0)
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
                - Political History
                - Social Profile
                    - Caste
                    - Religion

            - Parliamentary Activity
                - Bill Votes
                - Questions and Answers
                - Attendance            
        
            - Social Activity
                - New Mentions
        - Bills
            - Sector Wise*
        
        - Committees
        
        - Parties
            - Political Contributions
    
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

BASE_URL https://www.opengov.in/india-insider/

# Legislators  
    /legislators
        - An alphabetized list of all the legislators across all terms
        - A citizen can filter this list based on the term, party or constituency and so on

    /legislators/:legislator-name
        - Legislator details
            - Personal details
            - Educational details  
            - Address
            - Contact
            - Assests and liabilities  
            - Criminal cases 
            - Attendance in parliament session wise
        - Legislator Activity
            - MPLADS
            - Question & Answers
            - Participation debates 
            - Bill presentation 
    /legislators/house/:house-name/  
        - It will show a list all the legislator belongs that house in the current term.

    /legislators/term/:term-name/  
        - It will show a list all the legislator of loksabha in the selected term.

    /legislators/session/:session-name/  
        - It will show a list all the legislator of Rajyasabha in the selected session.

    /legislators/house/:house-name/party/:party-name  
        - It will show a list of legislator belongs to that political party in that specific house.
        - It will also show some details of that political party like Party symbol,founder name,Party president and year of establishment.

    /legislators/house/:house-name/state/:state-name/  
         - It will show a list of legislator belongs to that state in that specific house.  

    /legislators/house/:house-name/constituency/constituency-name 
        - It will show a list of all the legislator which are elected to that house like loksabha or rajyasabha across all the terms along with their party name.


# Debates    
    /debates  
        - All the debates which are occurred in both houses along with participants names.
    /debates/year/:year/  
        - It will show all the debates which occurred in that specific year.  
    /debates/legislator/:legislator-name/  
        - It will show all the debates in which that particular legislator participated.  
    /debates/type/:type/  
        - It will show all the debates basing on the type which selected.
    /debates/house/:house-name/  
        - It will show debates based the house which is selected.
   

# Bills  
    /bills
        - All the bills which are presented in both the house with their status. 
    /bills/year/:year/  
        - It will show all the bills which are presented in that year in both houses.
    /bills/type/:type/  
        - It will show bills based on their type selected
    /bills/status/:status/  
        - It will show based on their status selected.
        - Bills have various status like Assented,Passed and so on.


# Questions & Answers  
    /questions-and-answers
        - A list of all the questions in datewise manner.
    /questions/house/:house/  
        -Questions can be viewed based on the house in which it was asked along with who asked and all other things.
    /questions/type/:type/ 
        - Questions can be viewed based on its type like starred or unstarred.  
    /questions/ministry/:ministry/  
        - we can see the question based on the ministry to which question is related.
    /questions/legislator/:legislator-name/  
        - It will show all the questions asked by the particular legislator.  


# Petitions  
    /petitions
    /petitions/:petition-title
    /petitions/new
        - Idea is to let a citizen create a petition and let other citizens sign it, similar to change.org
        - 

# Committees  
    - Reports
