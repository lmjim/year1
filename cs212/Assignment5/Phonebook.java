public class Phonebook{
    private String name;
    private String number;
    
    public Phonebook(String name, String number){
        this.name = name;
        this.number = number;
    }
    
    public String getName(){
        return name;
    }
    
    public String getLastName(){
        String[] lastfirst = name.split(",");
        String lastName = lastfirst[0];
        return lastName;
    }
    
    public String getNumber(){
        return number;
    }
    
}