import java.awt.Point;
import java.awt.Graphics;
import java.awt.event.MouseEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseMotionAdapter;
import java.awt.Color;
import javax.swing.JPanel;
import java.util.ArrayList;

public class MainPanel extends JPanel {
	
	private ArrayList<Points> points;
    private int currentSize;
    private Color currentColor;
    
		
	public MainPanel(){
		points = new ArrayList<Points>();
        currentSize = 10;
        currentColor = Color.BLACK;
		
		addMouseMotionListener(
			new MouseMotionAdapter(){
				public void mouseDragged(MouseEvent event){
                    Points point = new Points(event.getPoint(), currentSize, currentColor);
					points.add(point);	
					repaint();
					
					System.out.println(points.size() + ": x = " + points.get(points.size() - 1).getPoint().x + " y = " + points.get(points.size() - 1).getPoint().y);
				}
			}
		);
        
        addMouseListener(
            new MouseAdapter(){
                public void mouseClicked(MouseEvent event){
                    Points point = new Points(event.getPoint(), currentSize, currentColor);
                    points.add(point);
                    repaint();

                    System.out.println(points.size() + ": x = " + points.get(points.size() - 1).getPoint().x + " y = " + points.get(points.size() - 1).getPoint().y);
                }
            }
        );
        
	}
    
    
    public void setSize(int size){
        currentSize = size;
    }
    
    
    public void setColor(Color color){
        currentColor = color;
    }
    
    
	public void paintComponent(Graphics g){
		super.paintComponent(g);
		
		for(Points point : points){
            g.setColor(point.getColor());
			g.fillOval(point.getPoint().x, point.getPoint().y, point.getSize(), point.getSize());
        }
	}
    
    
    public void clear(){
        points = new ArrayList<>();
        repaint();
    }
    
}