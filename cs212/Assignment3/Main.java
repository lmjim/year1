import java.util.Random;
import java.lang.Double;
import java.util.ArrayList;


public class Main{
    public static void main(String[] args){
        int rects = 0;
        int boxes = 0;
        int circles = 0;
        int spheres = 0;
        
        ArrayList<Measurable> areas = new ArrayList<Measurable>();
        for (int counter=0; counter < 1000; counter++){
            double shape = nextDouble();
            if (shape <= 0.25){
                Rectangle rectangle = new Rectangle(nextDouble(), nextDouble());
                areas.add(rectangle);
                rects++;
            }
            else if (shape <= 0.50){
                Box box = new Box(nextDouble(), nextDouble(), nextDouble());
                areas.add(box);
                boxes++;
            }
            else if (shape <= 0.75){
                Circle circle = new Circle(nextDouble());
                areas.add(circle);
                circles++;
            }
            else{
                Sphere sphere = new Sphere(nextDouble());
                areas.add(sphere);
                spheres++;
            }
            
        }
        
        System.out.printf("%s%d%s%d%s%d%s%d%n", "Rects: ", rects, " Boxes: ", boxes, " Circles: ", circles, " Spheres: ", spheres);
        double sum = calculateSum(areas);
        System.out.println("Sum: " + sum);
        
    }
    
    
    private static double nextDouble(){
        Random random = new Random();
        double value = random.nextDouble() + Double.MIN_VALUE;
        return value;
    }
    
    
    private static double calculateSum(ArrayList<Measurable> areas){
        double sum = 0.0;
        for (int counter=0; counter < areas.size(); counter++){
            Measurable shape = areas.get(counter);
            sum += shape.getArea();
        }
        
        return sum;
    }
    
}