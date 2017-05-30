package prediction;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URLConnection;
import java.util.ArrayList;
import java.util.Collections;

public class makeData {

	static ArrayList<String> list = new ArrayList<String>();
	static ArrayList<Double> prices = new ArrayList<Double>();
	static ArrayList<String> dates = new ArrayList<String>();
	static ArrayList<String> pe = new ArrayList<String>();



	private static void read(){

		for (int i=0; i<1; i++){
			String ticker = list.get(i);

			String csvFile = "/Users/Emil/Desktop/Stocks/" + ticker + ".csv";
			BufferedReader br = null;
			String line = "";


			try {

				br = new BufferedReader(new FileReader(csvFile));
				while ((line = br.readLine()) != null) {

					// use comma as separator
					String[] data = line.split(",");
					//System.out.println(data[1]);
					prices.add(Double.parseDouble(data[1]));
					dates.add(data[0]);

				}

			} catch (FileNotFoundException e) {
				e.printStackTrace();
			} catch (IOException e) {
				e.printStackTrace();
			} finally {
				if (br != null) {
					try {
						br.close();
					} catch (IOException e) {
						e.printStackTrace();
					}
				}
			}

			//			ArrayList<String> derp = new ArrayList<String>();
			//			derp.add("1");
			//			derp.add("2");
			//			derp.add("3");
			//			System.out.println(derp);
			//			Collections.reverse(derp);
			//			System.out.println(derp);

			//			double sum=0;
			//			for (int a = 200; a<400; a++){
			//				sum+=prices.get(a);
			//			}
			//			System.out.println("sum " + sum);
			//			double average = sum/200;
			//			System.out.println("Average " + average);

			//			Collections.reverse(prices);
			//			Collections.reverse(dates);
			//			System.out.println(dates);
			ArrayList<String> newDates = new ArrayList<String>();
			ArrayList<Double> newPrices = new ArrayList<Double>();
			for (int x=dates.size()-1; x>=0; x--){
				newDates.add(dates.get(x));
			}
			for (int x=prices.size()-1; x>=0; x--){
				newPrices.add(prices.get(x));
			}
			System.out.println(newDates);
			System.out.println(newPrices);
			try{
				BufferedWriter bf = new BufferedWriter(new FileWriter("C:\\Users\\Emil\\Desktop\\Stocks\\Prices\\" + ticker));
				for (int price = 200; i<newPrices.size()-10; price++){

					double sum = 0;
					for (int a = price-200; a<price; a++){
						sum+=newPrices.get(a);
					}
					double average200 = sum / 200;
					
					sum = 0;
					for (int a = price-100; a<price; a++){
						sum+=newPrices.get(a);
					}
					double average100 = sum / 100;
					
					sum = 0;
					for (int a = price-50; a<price; a++){
						sum+=newPrices.get(a);
					}
					double average50 = sum / 50;
					


					double percent200 = newPrices.get(price) / average200;
					double percent100 = newPrices.get(price) / average100;
					double percent50 = newPrices.get(price) / average50;


					int peaked = 0;
					if (newPrices.get(price+10) > newPrices.get(price)){
						peaked = 1;
					}




					bf.write(newDates.get(price) + "," + /*newPrices.get(price) + "," + average200 + "," + average50 + 
							"," */+ percent200 + "," + percent100 + "," + percent50 + "," + peaked + "\n");
					bf.flush();
				}
			}
			catch(Exception e){

			}

		}
	}

	private static void init(){
		list.add("MSFT");
		list.add("GOOG");
		list.add("AMZN");
		list.add("AAPL");
		list.add("YHOO");
		list.add("XOM");	
	}

	private static void create() {

		for (int i=0; i<list.size(); i++){
			String ticker = list.get(i);

			String start_month = "Jan";
			String start_day = "01";
			String start_year = "2005";
			try { 
				String stringUrl = "";
				stringUrl = "https://www.google.com/finance/historical?q=NASDAQ:" + ticker + 
						"&startdate=" + start_month + "+" + start_day + "%2C+" + start_year + "&output=csv";
				URL url  = new URL(stringUrl);
				URLConnection uc = url.openConnection();
				InputStreamReader inStream = new InputStreamReader(uc.getInputStream());
				BufferedReader buff= new BufferedReader(inStream);

				String line = null;

				BufferedWriter bf = new BufferedWriter(new FileWriter("C:\\Users\\Emil\\Desktop\\Stocks\\" + ticker));
				while ((line = buff.readLine()) != null) {
					String[] price = line.split(",");
					bf.write(price[0] + "," + price[4]+"\n");
					bf.flush();
				}
			}
			catch (Exception e){
				e.printStackTrace();
			}
			System.out.println("done");




			//		FileWriter writer = null;
			//
			//		try {
			//
			//			writer = new FileWriter(fileName, false);
			//
			//			System.out.println("CSV file is created...");
			//
			//		} catch (IOException e) {
			//			e.printStackTrace();
			//		} finally {
			//			try {
			//				writer.flush();
			//				writer.close();
			//			} catch (IOException e) {
			//				e.printStackTrace();
			//			}
			//		}
		}
	}

	public static void main(String[] args) {
		init();
		//System.out.println(System.getProperty("user.home"));
		//String location = "C:\\Users\\Emil\\Desktop\\newCsvFile.csv";
		//create();
		read();
		//		for (int i=0; i<prices.size(); i++){
		//			System.out.println(prices.get(i));
		//		}

	}

}

