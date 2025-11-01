package defect;

public class ParachuteLanding implements Landable {

    private final String name = "Parachute";

    @Override
    public void land() { // Fixed signature to match Landable interface
        System.out.println(name + " landing: Deploying parachutes and descending safely.");
    }

    @Override
    public String toString() {
        return name; // Fixed syntax error
    }
}