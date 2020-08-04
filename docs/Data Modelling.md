------------------------------------------------------------------------------------------------------
OpenGov Modelling
------------------------------------------------------------------------------------------------------ 
## Central Legislatures | central legislatures
    Name | String | name | required | Ex: Rajya Sabha, Lok Sabha, Vidhan Sabha
    Type | String | type | required | Ex: Upper, Lower

## State Legislatures | state_legislatures
    Name | String | name | required | Ex: Telangana Legislative Assembly, Telangana Legislative Council
    Type | String | type | required | Ex: Upper, Lower
    State | Integer | state_id | required | Ex: Empty means its at central level, existing state id means its at state level

## States  | states  
    Name  | String  | name  |  required  

## Parliamentary Constituencies  | parliamentary_constituencies  
    Constituency Number  | Integer  |  constituency_number  |  required
    Name  |  String  | name  |  required  
    State  |  Integer  |  state_id  | required  

## Assembly Constituencies  | Assembly constituencies
    Constituency Number  | Integer  |  constituency_number  |  required
    Name  |  String  | name  |  required  
    State  |  Integer  |  state_id  | required  

## Terms  |  terms
    Term Name  |  String  |  term_name  |  required  | ex: 17th term, 153rd, 
    Starting Year  |  String  |  start_year  |  required  
    End Year  |  String  |  end_year  |  required
    House | integer | house_id | required

## Sittings | sittings
    Sitting Name  |  String  |  sitting_name  |  required  | ex: 17th term, 153rd, 
    Starting Year  |  String  |  start_year  |  required  
    End Year  |  String  |  end_year  |  required
    House |     

##  Parliamentary Sessions  |  parliamentary_sessions
    Session Id  | Integer  | session_id  | required
    Session Type  |  String   | type  |  required  | Possible values ex: Budget session,Monsoon session, Winter session  
    Term  | Integer  |  term  |  required  
    Starting Date  |  String  | start_date  |  required  
    End Date  | String  | end_date  |  required  

## Assembly Sessions | assembly_sessions

##  Parties  |  parties  
    Party Id  |  Integer  |  party_id  |  required  
    Party Name  |  String  |  party_name  |  required  
    Acronym  |  String  |  acronym  |  required   
    Type  |  String  |  type  |  required  |  Possible Values  Ex: National Level, State level, Regional   
    Symbols  |  Image  |  symbol  |  required  
    Founded  |  String |  founded  |  required  
    Founder Name  |  String  |  founder_name  |  required  
    President Name  |  String  |  president_name  |  required  
    Website  |  String  |  website  |  required  

## Legislators  |  legislators  
    Legislator Id  |  Integer  | legislator_id  |  required  
    Name  |  String  |  name  |  required  
    DOB |  Integer  |  dob  |  required  
    Qualification  |  String  |  qualification  |  required  
    Gender  |  String  |  gender  |  required  
    Social Class  |  String  |  social_class  |  required  | Possible values  Ex: General,OBC,SC,ST 
    Contact Number  |  String  |  contact_number  |  required  
    Email  |  String  |  email  |  required  
    Profession  |  String   |  profession  |  required  
    Criminal Cases  |  Integer  |  criminal_cases  |  required 
    Photo  |  Image  |  photo  |  required  
    Present Address  |  Text  |  present_address  |  required  
    Permanent Address  |  Text  |  permanent_address  |  required   
    Party Name  |  Integer  |  party_id  |  required  
    State  |  Integer  |  state_id  |  required  
    Constituency  |  Integer  |  constituency_id  |  required  
    Term  |  Integer  |  term_id  |  required  
    House  |  String  |  house  |  required  |  Possible values  Ex: Loksabha, Rajyasabha 
    *Assests

## Questions  |  questions  
    Question Id  |  Integer  |  question_id  |  required  
    Title  |  Text  |  title  |  required  
    Answer  |  Text  |  answer  |  required  
    Question Type  |  String  |  type  |  required  |  Possible Values  Ex: Starred, Unstarred 
    Asked By  |  Integer  | legislator_id  |  required  
    *Category(Ministry)  | String  |  category  |  required  
    Date  |  String  |  date  |  required  
    Subject  |  String  |  subject  |  required  
    Session  |  Integer  |  session_id  |  required  
    Term  |  Integer  |  term_id  |  required
    House  |  String  |  house  |  required  |  Possible values  Ex: Loksabha, Rajyasabha  
    * External Link  |  String  |  link  |  required  

## Bills  |  bills  
    Bill Id  |  Integer  |  bill_id  |  required  
    Title  |  Text   |  title  |  required  
    House  |  String  |  house  |  required  |  Possible values  Ex: Loksabha, Rajyasabha  
    Type  |  String  |  type  |  required  |   Possible values  Ex: Government ,Private Member  
    Status  |  String  |  status |  required  |  Possible Values  Ex: Assented,Passed,Pending,Withdrawn,Negatived,Lapsed  
    Introducer  |  Integer  |  legislator_id  |  required  
    *Ministry |  String  |  ministry  |  required  
    Year  |  String  |  year  |  required  
    Category  |  String  |  category  |  required   |   Possible values  Ex: Ordinary Bill,Constitutional Amendment bill,Financial Bill, Money Bill,Ordinance Replacing bill  
    Session  |  Integer  |  session_id  |  required  
    Term  |  Integer  |  term_id  |  required  

## Debates  |  debates  
    Debate Id  |  Integer  |  debate_id  |  required   
    Title  |  Text  |  title  |  required    
    Content  |  Text  |  content  |   required   
    Type  |  String  |  type  |  required  |  Possible values  Ex: Adjournment Motion,Announcement by the chair,Assent to bills and so on (46 types)  
    Participants  |  Integer  |  legislator_id  |  required  
    Session  |  Integer  |  session_id  |  required  
    Term  |  Integer  |  term_id  |  required  
    Date  |  String  |  date  |  required  