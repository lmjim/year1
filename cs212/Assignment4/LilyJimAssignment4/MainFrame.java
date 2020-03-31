import java.awt.FlowLayout;
import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.BoxLayout;
import javax.swing.Box;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class MainFrame extends JFrame {
	private final JButton colorBlack;
	private final JButton colorBlue;
	private final JButton colorRed;
    private final JButton colorGreen;
    
    private final JButton sizeSmall;
    private final JButton sizeMedium;
    private final JButton sizeLarge;
    private final JButton optionClear;
	
	public MainFrame() {
		setLayout(new BorderLayout());
        
        
        //Create Drawing Canvas in center with White Background:
        MainPanel mainPanel = new MainPanel();
        mainPanel.setBackground(Color.WHITE);
        add(mainPanel, BorderLayout.CENTER);
        
        
        
        //Create vertical button panel for color selection
        JPanel colorButtonPanel = new JPanel();
        colorButtonPanel.setLayout(new BoxLayout(colorButtonPanel, BoxLayout.PAGE_AXIS));
        
		//Create button for black
		colorBlack = new JButton("Black");
        colorBlack.setBackground(Color.LIGHT_GRAY);
        colorBlack.setForeground(Color.BLACK);
        colorBlack.setMaximumSize(new Dimension(100, 100));
        colorBlack.setPreferredSize(new Dimension(100, 100));
		colorBlack.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                mainPanel.setColor(Color.BLACK);
            }
        }
        );
		colorButtonPanel.add(colorBlack);
        
        //Create button for blue
		colorBlue = new JButton("Blue");
        colorBlue.setBackground(Color.LIGHT_GRAY);
        colorBlue.setForeground(Color.BLUE);
        colorBlue.setMaximumSize(new Dimension(100, 100));
        colorBlue.setPreferredSize(new Dimension(100, 100));
		colorBlue.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                mainPanel.setColor(Color.BLUE);
            }
        }
        );
        colorButtonPanel.add(Box.createRigidArea(new Dimension (0,5)));
		colorButtonPanel.add(colorBlue);
        
        //Create button for red
		colorRed = new JButton("Red");
        colorRed.setBackground(Color.LIGHT_GRAY);
        colorRed.setForeground(Color.RED);
        colorRed.setMaximumSize(new Dimension(100, 100));
        colorRed.setPreferredSize(new Dimension(100, 100));
		colorRed.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				mainPanel.setColor(Color.RED);
			}			
		}
        );
        colorButtonPanel.add(Box.createRigidArea(new Dimension (0,5)));
		colorButtonPanel.add(colorRed);
        
        //Create button for green
        colorGreen = new JButton("Green");
        colorGreen.setBackground(Color.LIGHT_GRAY);
        colorGreen.setForeground(new Color(0, 200, 0));
        colorGreen.setMaximumSize(new Dimension(100, 100));
        colorGreen.setPreferredSize(new Dimension(100, 100));
		colorGreen.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				mainPanel.setColor(new Color(0, 200, 0));
			}			
		}
        );
        colorButtonPanel.add(Box.createRigidArea(new Dimension (0,5)));
		colorButtonPanel.add(colorGreen);
        
        //Put color button panel on left
        add(colorButtonPanel, BorderLayout.WEST);
        
        
        
        //Create vertical button panel for size and clear
        JPanel sizeButtonPanel = new JPanel();
        sizeButtonPanel.setLayout(new BoxLayout(sizeButtonPanel, BoxLayout.PAGE_AXIS));
        
        //Create button for small
        sizeSmall = new JButton("Small");
        sizeSmall.setBackground(Color.LIGHT_GRAY);
        sizeSmall.setAlignmentX(sizeButtonPanel.RIGHT_ALIGNMENT);
        sizeSmall.setMaximumSize(new Dimension(100, 100));
        sizeSmall.setPreferredSize(new Dimension(100, 100));
        sizeSmall.setAlignmentX(sizeButtonPanel.RIGHT_ALIGNMENT);
        sizeSmall.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                mainPanel.setSize(5);
            }
        }
        );
        sizeButtonPanel.add(sizeSmall);
        
        //Create button for medium
        sizeMedium = new JButton("Medium");
        sizeMedium.setBackground(Color.LIGHT_GRAY);
        sizeMedium.setAlignmentX(sizeButtonPanel.RIGHT_ALIGNMENT);
        sizeMedium.setMaximumSize(new Dimension(100, 100));
        sizeMedium.setPreferredSize(new Dimension(100, 100));
        sizeMedium.setAlignmentX(sizeButtonPanel.RIGHT_ALIGNMENT);
        sizeMedium.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                mainPanel.setSize(10);
            }
        }
        );
        sizeButtonPanel.add(Box.createRigidArea(new Dimension (0,5)));
        sizeButtonPanel.add(sizeMedium);
        
        //Create button for large
        sizeLarge = new JButton("Large");
        sizeLarge.setBackground(Color.LIGHT_GRAY);
        sizeLarge.setAlignmentX(sizeButtonPanel.RIGHT_ALIGNMENT);
        sizeLarge.setMaximumSize(new Dimension(100, 100));
        sizeLarge.setPreferredSize(new Dimension(100, 100));
        sizeLarge.setAlignmentX(sizeButtonPanel.RIGHT_ALIGNMENT);
        sizeLarge.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                mainPanel.setSize(20);
            }
        }
        );
        sizeButtonPanel.add(Box.createRigidArea(new Dimension (0,5)));
        sizeButtonPanel.add(sizeLarge);
        
        //Create button to clear
        optionClear = new JButton("Clear");
        optionClear.setBackground(Color.LIGHT_GRAY);
        optionClear.setAlignmentX(sizeButtonPanel.RIGHT_ALIGNMENT);
        optionClear.setMaximumSize(new Dimension(100, 100));
        optionClear.setPreferredSize(new Dimension(100, 100));
        optionClear.setAlignmentX(sizeButtonPanel.RIGHT_ALIGNMENT);
        optionClear.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                mainPanel.clear();
            }
        }
        );
        sizeButtonPanel.add(Box.createRigidArea(new Dimension (0,5)));
        sizeButtonPanel.add(optionClear);

        //Put size and clear buttons on right
        add(sizeButtonPanel, BorderLayout.EAST);
        
	}
    
}