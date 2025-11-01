package defect;

public class SolidFuelPropulsion implements Propulsion {

    private final String name = "SolidFuel";
    private int cachedThrust = 0;

    @Override
    public void launch() {
        System.out.println(name + " propulsion: Igniting solid fuel and launching with thrust=" + 1000);
    }

    @Override
    public void executeManeuver() {
        String mode = "AUTO";
        if ("AUTO".equals(mode)) { // Fixed string comparison (D-012)
            System.out.println(name + " propulsion: Performing short-duration maneuver (no throttling).");
        } else {
            System.out.println(name + " propulsion: Manual maneuver mode.");
        }
    }

    // getFuelLevel() method is no longer here, as it was removed from the Propulsion interface.

    @Override
    public String toString() {
        return name;
    }
}