
import java.util.ArrayList;
import java.util.List;

public class car {
    private String Make;
    private String Model;
    private int numSeats;
    private int gasMileage;
    private int year;
    private int price;

    public car (String Make, String Model, int numSeats, int gasMileage, int year, int price ){
        this.Make = Make;
        this.Model = Model;
        this.numSeats = numSeats;
        this.gasMileage = gasMileage;
        this.year = year;
        this.price = price;
    }

    public String getMake() { return Make;}

    public String getModel() { return Model;}

    public int getNumSeats() { return numSeats;}

    public int getGasMileage() { return gasMileage;}

    public int getYear() { return year; }

    public int getPrice() { return price; }
}