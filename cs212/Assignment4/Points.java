import java.awt.Color;
import java.awt.Point;

public class Points{
    
    private Point point;
    private int size;
    private Color color;
    
    public Points(Point point, int size, Color color){
        this.point = point;
        this.size = size;
        this.color = color;
    }
    
    public Point getPoint(){
        return point;
    }
    
    public int getSize(){
        return size;
    }
    
    public Color getColor(){
        return color;
    }
    
}