------------------------------------------------------------------------------------------------------
OpenGov Modelling
------------------------------------------------------------------------------------------------------ 
## Central Legislatures | central_legislatures
    Name | String | name | required | Ex: Rajya Sabha, Lok Sabha, Vidhan Sabha
    Type | String | type | required | Ex: Upper, Lower

## State Legislatures | state_legislatures
    Name | String | name | required | Ex: Telangana Legislative Assembly, Telangana Legislative Council
    Type | String | type | required | Ex: Upper, Lower
    State | Integer | state_id | required 

## States  | states  
    Name  | String  | name  |  required  

## Parliamentary Constituencies  | parliamentary_constituencies
    Constituency Number  | Integer  |  constituency_number  |  required
    Name  |  String  | name  |  required  
    State  |  Integer  |  state_id  | required

## Assembly Constituencies  | assembly_constituencies
    Constituency Number  | Integer  |  constituency_number  |  required
    Name  |  String  | name  |  required  
    State  |  Integer  |  state_id  | required  

## Terms  |  terms
    Term Name  |  String  |  term_name  |  required  | ex: 17th term, 153rd, 
    Starting Year  |  String  |  start_year  |  required  
    End Year  |  String  |  end_year  |  required
    Central Legislatures  |  Integer | central_legislature_id | required 

## Sittings | sittings
    Sitting Name  |  String  |  sitting_name  |  required  | ex: 17th term, 153rd, 
    Starting Year  |  String  |  start_year  |  required  
    End Year  |  String  |  end_year  |  required 
    State Legislature | integer | state_legislature_id | required    

##  Parliamentary Sessions  |  parliamentary_sessions
    
    Session Type  |  String   | type  |  required  | Possible values ex: Budget session,Monsoon session, Winter session  
    Term  | Integer  |  term_id |  required  
    Starting Date  |  String  | start_date  |  required  
    End Date  | String  | end_date  |  required  
    Central Legislature  |  Integer | central_legislature_id | required 
    Total Working Days | Integer  | working_days | integer 

## Assembly Sessions | assembly_sessions
    Session Type  |  String   | type  |  required  | Possible values ex: Budget session / First ,Monsoon session / Second, Winter session / Third   
    Sitting  | Integer  |  sitting_id |  required  
    Starting Date  |  String  | start_date  |  required  
    End Date  | String  | end_date  |  required  
    State Legislature | integer | state_legislature_id | required 

##  Parties  |  parties  
    Party Name  |  String  |  party_name  |  required  
    Acronym  |  String  |  acronym  |  required   
    Type  |  String  |  type  |  required  |  Possible Values  Ex: National Level, State level, Regional   
    Symbols  |  Image  |  symbol  |  required  
    Founded  |  String |  founded  |  required  
    Founder Name  |  String  |  founder_name  |  required  
    President Name  |  String  |  president_name  |  required  
    Website  |  String  |  website  |  required  

## Candidate | candidate
    
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
    *Assests

## Candidature | candidature
    Candidate | Integer | candidate_id | required
    Party Name  |  Integer  |  party_id  |  required  
    State  |  Integer  |  state_id  |  required  
    Type | String | type | required | Possible Values Ex: MP,MLA,MLC 
    Parliamentary Constituency | Integer | parliamentary_constituency_id | Optional  
    Assembly Constituency | Integer | assembly_constituency_id | Optional 
    Term  |  Integer  |  term_id  |  Optional 
    Sitting | Integer | sitting_id | Optional 
    Central Legislatures | Integer | central_legislature_id | Optional 
    State Legislatures | Integer | state_legislature_id | Optional 
    
    

## Questions | questions  
    Title  |  Text  |  title  |  required  
    *Answer  |  Text  |  answer  |  Optional  
    Question Type  |  String  |  type  |  required  |  Possible Values  Ex: Starred, Unstarred 
    Asked By  |  Integer  | candidate_id  |  required  
    *Category(Ministry)  | String  |  category  |  required  
    Date  |  String  |  date  |  required  
    Subject  |  String  |  subject  |  required  
    Term  |  Integer  |  term_id  |  Optional 
    Sitting | Integer | sitting_id | Optional 
    Parliamentary Session  |  Integer  |  parliamentary_session_id  |  Optional   
    Assembly Session | Integer | assembly_session_id | Optional 
    Central Legislature | Integer | central_legislature_id | Optional 
    State Legislature | Integer | state_legislature_id | Optional 
    * External Link  |  String  |  link  |  Optional  

## Bills  |  bills  
    Title  |  Text   |  title  |  required  
    Type  |  String  |  type  |  required  |   Possible values  Ex: Government, Private Member  
    Status  |  String  |  status |  required  |  Possible Values  Ex: Assented, Passed, Pending, Withdrawn, Negatived,Lapsed  
    Introducer  |  Integer  |  candidate_id  |  required  
    *Ministry |  String  |  ministry  |  required  
    Year  |  String  |  year  |  required  
    Category  |  String  |  category  |  required   |   Possible values  Ex: Ordinary Bill, Constitutional Amendment bill,Financial Bill, Money Bill, Ordinance Replacing bill 
    Term  |  Integer  |  term_id  |  Optional 
    Sitting | Integer | sitting_id | Optional 
    Parliamentary Session  |  Integer  |  parliamentary_session_id  |  Optional   
    Assembly Session | Integer | assembly_session_id | Optional 
    Central Legislature | Integer | central_legislature_id | Optional 
    State Legislature | Integer | state_legislature_id | Optional
    * External Link  |  String  |  link  |  Optional 
      

## Debates  |  debates  
    Title  |  Text  |  title  |  required    
    Content  |  Text  |  content  |   required   
    Type  |  String  |  type  |  required  |  Possible values  Ex: Adjournment Motion, Announcement by the chair, Assent to bills and so on (46 types)  
    Participants  |  Integer  |  candidate_id  |  required  
    Central Legislature | Integer | central_legislature_id | Required 
    Session  |  Integer  |  session_id  |  required  
    Term  |  Integer  |  term_id  |  required  
    Date  |  String  |  date  |  required  
    * External Link  |  String  |  link  |  Optional 


## Attendance  | attendance  
    Attendance | String | attendance | required 
    Term  |  Integer  |  term_id  |  required 
    Session | Integer | session_id | required  
    Candidate | Integer | candidate_id | required  
    No.of days Signed | Integer | signed_days | required 
    No.of days Not Signed | Integer | not_signed_days | required
    