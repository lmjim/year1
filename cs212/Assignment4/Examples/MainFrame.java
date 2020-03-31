import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JFrame;

public class MainFrame extends JFrame {
	private final JButton button1;
	private final JButton button2;
	private final JButton button3;
	private final JLabel label;
	
	public MainFrame() {
		setLayout(new FlowLayout());
		
		button1 = new JButton("Button 1");
		button1.addActionListener(new Button1Listener());
		add(button1);		

		button2 = new JButton("Button 2");
		button2.addActionListener(new Button2Listener());
		add(button2);

		button3 = new JButton("Button 3");
		button3.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				label.setText("Button 3 Clicked!");
			}			
		});
		add(button3);
		
		label = new JLabel("No button clicked!");
		add(label);
		
	}
	
	private class Button1Listener implements ActionListener {
		public void actionPerformed(ActionEvent e) {
			label.setText("Button 1 Clicked!");
		}		
	}
	
	private class Button2Listener implements ActionListener {
		public void actionPerformed(ActionEvent e) {
			label.setText("Button 2 Clicked!");
		}		
	}
}