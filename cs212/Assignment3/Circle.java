public class Circle implements Measurable{
    double radius;
    
    public Circle(double radius){
        this.radius = radius;
    }
    
    @Override
    public double getArea(){
        return (Math.PI * radius * radius);
    }
    
}
