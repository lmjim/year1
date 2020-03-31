public class Box extends Rectangle{
    double height;
    
    public Box(double length, double width, double height){
        super(length, width);
        this.height = height;
    }
    
    @Override
    public double getArea(){
        return ((2.0 * length * width) + (2.0 * length * height) + (2.0 * width * height));
    }
    
}