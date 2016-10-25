import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Iterator;

public class homework {
	public class cellvalues {
		int row, column, cell_value;
		public cellvalues(int row, int column, int cell_value){
			this.row = row;
			this.column = column;
			this.cell_value = cell_value;
		}
	}
	public class boardstate {
		int row, column;
		String board_state_cell_value;
		public boardstate(int row, int column, String board_state_cell_value){
			this.row = row;
			this.column = column;
			this.board_state_cell_value = board_state_cell_value;
		}
	}
	public static void main(String args[]){
		ArrayList<cellvalues> game_board_cell_values = new ArrayList<cellvalues>();
		ArrayList<boardstate> game_board_state = new ArrayList<boardstate>();
		int N = 0, depth, row_number = 0;
		String type_of_algorithm = "";
		String player = "", opponent = "";
		String file_name = "G:/Documents/USC/Artificial Intelligence/Homework/Homework 2/Input/input0.txt";
		FileReader file_reader;
		try {
			file_reader = new FileReader(file_name);
			BufferedReader buffered_reader = new BufferedReader(file_reader);
			String each_line = "";
			int line_number = -1;
			

			while((each_line = buffered_reader.readLine()) != null){
				line_number += 1;
				if(line_number == 0){
					N = Integer.parseInt(each_line);
				}else if(line_number == 1){
					type_of_algorithm = each_line;
				}else if(line_number == 2){
					String you_play = each_line;
					if(you_play == "X"){
						player = "X";
						opponent = "O";
					}else{
						player = "O";
						opponent = "X";
					}
				}else if(line_number == 3){
					depth = Integer.parseInt(each_line);
				}else if(line_number < 4 + N){
					row_number += 1;
					String[] str = each_line.split(" ");
					for(int i = 0; i < N; i++){
						int cell_value = Integer.parseInt(str[i]);
						int column_number = i;
						homework hw = new homework();
						cellvalues cv = hw.new cellvalues(row_number, column_number, cell_value);
						game_board_cell_values.add(cv);

					}
				}else{
					if(row_number == N){
						row_number = 0;
					}
					row_number += 1;
					String[] str = each_line.split("");
					for(int i = 0; i < N; i++){
						String board_state_cell_value = str[i];
						int column_number = i;
						homework hw = new homework();
						boardstate bs = hw.new boardstate(row_number, column_number, board_state_cell_value);
						game_board_state.add(bs);

					}
					//System.out.println(each_line);
				}
				
			}
			buffered_reader.close();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			System.out.println("File Not Found");
		}
		/*
		Iterator itr_cv = game_board_cell_values.iterator();
		while(itr_cv.hasNext()){
			cellvalues cv = (cellvalues)itr_cv.next();
			System.out.println("Row - "+ cv.row + " col - "+ cv.column + " Cell - " + cv.cell_value);
		}
		System.out.println("----");
		Iterator itr_bs = game_board_state.iterator();
		while(itr_bs.hasNext()){
			boardstate bs = (boardstate)itr_bs.next();
			System.out.println("Row - "+ bs.row + " col - "+ bs.column + " Cell - " + bs.board_state_cell_value);
		}
		*/
		
	}
}
