public class Sphere extends Circle{
    
    public Sphere(double radius){
        super(radius);
    }
    
    @Override
    public double getArea(){
        return (4.0 * Math.PI * radius * radius);
    }
    
}