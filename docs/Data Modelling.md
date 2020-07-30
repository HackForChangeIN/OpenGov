------------------------------------------------------------------------------------------------------
OpenGov Modelling
------------------------------------------------------------------------------------------------------ 

## States  | states  
    State Id  | Integer  |  state_id  |  required  
    Name  | String  | name  |  required  

## Constituencies  | constituencies  
    Constituency Id  | Integer  |  constituency_id  |  required  
    Name  |  String  | name  |  required  
    State  |  Integer  |  state  | required  

## Terms  
    Term Id  |  Integer  | term_id  |  required  
    Starting Year  |  String  |  start_year  |  required  
    End Year  |  String  |  end_year  |  required  


## Sessions  |  sessions   
    Session Id  | Integer  | session_id  | required  
    Session Type  |  String   | type  |  required  | Possible values ex: Budget session,Monsoon session, Winter session  
    Term  | Integer  |  term  |  required  
    Starting Date  |  String  | start_date  |  required  
    End Date  | String  | end_date  |  required  

## Parties  |  parties  
    Party Id  |  Integer  |  party_id  |  required  
    Full Name  |  String  |  full_name  |  required  
    Acronym  |  String  |  acronym  |  required   
    Type  |  String  |  type  |  required  |  Possible Values  Ex: National Level, State level  
    Symbols  |  Image  |  symbol  |  required  
    Founded  |  String |  founded  |  required  
    Founder Name  |  String  |  founder_name  |  required  
    President Name  |  String  |  president_name  |  required  
    Website  |  String  |  website  |  required  
