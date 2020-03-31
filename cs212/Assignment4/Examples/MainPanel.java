import java.awt.Point;
import java.awt.Graphics;
import java.awt.event.MouseEvent;
import java.awt.event.MouseMotionAdapter;
import javax.swing.JPanel;

import java.util.ArrayList;

public class MainPanel extends JPanel {
	
	private final ArrayList<Point> points;
	private Point previousPoint;
		
	public MainPanel(){
		points = new ArrayList<Point>();
		previousPoint = new Point(0,0);
		
		addMouseMotionListener(
			new MouseMotionAdapter(){
				public void mouseDragged(MouseEvent event){
					points.add(event.getPoint());	
					repaint();
					
					System.out.println(points.size() + ": x = " + points.get(points.size() - 1).x + " y = " + points.get(points.size() - 1).y);
				}
			}
		);
	}
		
	public void paintComponent(Graphics g){
		super.paintComponent(g);
		
		// Drawing dots	
		for(Point point : points)
			g.fillOval(point.x, point.y, 3, 3);
		
		/*
		// Moving the block
		if(points.size() > 1){
			if(points.get(points.size() - 1).x < previousPoint.x + 20 && points.get(points.size() - 1).y < previousPoint.y + 20){
				g.fillRect(points.get(points.size() - 1).x, points.get(points.size() - 1).y, 20, 10);
				previousPoint = points.get(points.size() - 2);
			}else
				g.fillRect(previousPoint.x, previousPoint.y, 20, 10);
		}
		*/	
	}	
}