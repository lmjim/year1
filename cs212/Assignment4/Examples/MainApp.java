import javax.swing.JFrame;
import java.awt.BorderLayout;

public class MainApp {

	public static void main(String[] args) {	
		MainFrame mainFrame = new MainFrame();
		
		mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		mainFrame.setSize(500, 200);
		mainFrame.setVisible(true);
	
		JFrame anotherMainFrame = new JFrame();
	
		MainPanel mainPanel = new MainPanel();
		anotherMainFrame.add(mainPanel, BorderLayout.CENTER);
	
		anotherMainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		anotherMainFrame.setSize(500, 200);
		anotherMainFrame.setVisible(true);	
	}
}