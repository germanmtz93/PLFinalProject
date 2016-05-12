
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {

        ArrayList<car> cars = new ArrayList<>();

        String path = System.getProperty("user.dir") + "/";

        File file = new File(path + "cars.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));


        String line;
        while((line = br.readLine()) != null){
            String a = line.substring(1, line.length() -2);
            List<String> carList = Arrays.asList(a.split(","));
            for (int i = 0; i < carList.size();i++){
                carList.set(i,carList.get(i).trim());

            }
            carList.get(0);

            car c = new car(carList.get(0),carList.get(1),Integer.parseInt(carList.get(2)),Integer.parseInt(carList.get(3)),Integer.parseInt(carList.get(4)),Integer.parseInt(carList.get(5)));
            cars.add(c);
        }
        System.out.println("SELECT make, model, gasmileage, price FROM cars WHERE gasmileage > 30 AND price < 25000");
        cars.stream()
                .filter(c -> (c.getGasMileage() > 30) && (c.getPrice() < 25000))
                .forEach(c -> {
                    System.out.println(c.getMake() + " " + c.getModel() + " " + c.getGasMileage() + " " + c.getPrice());
                });

        System.out.println();

        System.out.println("SELECT make, model, gasmileage, price FROM cars WHERE gasmileage > 35 AND price > 40000 ORDER BY price");

        cars.stream()
                .sorted((c1,c2) -> Integer.toString(c1.getPrice()).compareTo(Integer.toString(c2.getPrice())))
                .filter(c -> (c.getGasMileage() > 35) && (c.getPrice() > 40000))
                .forEach(c -> {
                    System.out.println(c.getMake() + " " + c.getModel() + " " + c.getGasMileage() + " " + c.getPrice());
                });

        System.out.println();

        System.out.println("SELECT make, model, gasmileage, numseats, price, year FROM cars WHERE numseats >= 7 AND gasmileage >= 20 ORDER BY year DESC");

        cars.stream()
                .filter(c -> (c.getGasMileage() >= 20) && (c.getNumSeats() >=7))
                .sorted((c1,c2) -> Integer.toString(c2.getYear()).compareTo(Integer.toString(c1.getYear())))
                .forEach(c -> {
                    System.out.println(c.getMake() + " " + c.getModel() + " " + c.getGasMileage() + " " + c.getNumSeats() + " " + c.getPrice() + " " + c.getYear());
                });

    }
}