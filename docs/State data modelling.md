## States  | states  
    State Id  | Integer  |  state_id  |  required  
    Name  | String  | name  |  required  

## Constituencies  | constituencies  
    Constituency Id  | Integer  |  constituency_id  |  required  
    Name  |  String  | name  |  required  
    State  |  Integer  |  state  | required  

## Sittings  |  sittings    
    Sitting Id  |  Integer  | sitting_id  |  required  
    Sitting Name  |  String  |  sitting_name  |  required  | ex: In odisha current sitting is 16th sitting     
    Starting Year  |  String  |  start_year  |  required  
    End Year  |  String  |  end_year  |  required  
    State  |  String  |  state_id  |  required  


## Sessions  |  sessions   
    Session Id  | Integer  | session_id  | required  
    Session Type  |  String   | type  |  required  | Possible values ex: Budget session / First ,Monsoon session / Second, Winter session / Third       
    Sitting  | Integer  |  sitting_id  |  required  
    Starting Date  |  String  | start_date  |  required  
    End Date  | String  | end_date  |  required  

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
    Sitting  |  Integer  |  sitting_id  |  required  
    House  |  String  |  house  |  required  |  Possible values  Ex: Upper / Vidhan Parishad, Lower / Vidhan Sabha  
    *Assests
## Questions  |  questions  
    Question Id  |  Integer  |  question_id  |  required  
    Title  |  Text  |  title  |  required  
    *Answer  |  Text  |  answer  |  required  
    Question Type  |  String  |  type  |  required  |  Possible Values  Ex: Starred, Unstarred 
    Asked By  |  Integer  | legislator_id  |  required  
    *Category(Ministry)  | String  |  category  |  required  
    Date  |  String  |  date  |  required  
    Subject  |  String  |  subject  |  required  
    Session  |  Integer  |  session_id  |  required  
    Sitting  |  Integer  |  sitting_id  |  required
    House  |  String  |  house  |  required  |  Possible values  Ex: Upper / Vidhan Parishad, Lower / Vidhan Sabha   
    * External Link  |  String  |  link  |  required  

## Bills  |  bills  
    Bill Id  |  Integer  |  bill_id  |  required  
    Title  |  Text   |  title  |  required  
    House  |  String  |  house  |  required  |  Possible values  Ex: Upper / Vidhan Parishad, Lower / Vidhan Sabha    
    Type  |  String  |  type  |  required  |   Possible values  Ex: Government ,Private Member  
    Status  |  String  |  status |  required  |  Possible Values  Ex: Assented,Passed,Pending,Withdrawn,Negatived,Lapsed  
    Introducer  |  Integer  |  legislator_id  |  required  
    *Ministry |  String  |  ministry  |  required  
    Year  |  String  |  year  |  required  
    Category  |  String  |  category  |  required   |   *Possible values  Ex: Ordinary Bill,Constitutional Amendment bill,Financial Bill, Money Bill,Ordinance Replacing bill 
    Session  |  Integer  |  session_id  |  required  
    Sitting  |  Integer  |  sitting_id  |  required  

