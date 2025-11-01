package defect;

public class PoweredLanding implements Landable {

    private final String name = "PoweredLanding";

    @Override
    public void land() { // Fixed signature to match Landable interface
        System.out.println(name + " landing: Performing retro-burn and precision touchdown.");
    }

    @Override
    public String toString() {
        return name;
    }
}