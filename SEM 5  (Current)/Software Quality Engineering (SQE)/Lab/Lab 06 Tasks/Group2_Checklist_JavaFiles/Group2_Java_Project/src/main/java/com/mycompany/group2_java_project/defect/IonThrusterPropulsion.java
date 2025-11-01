package defect;

public class IonThrusterPropulsion implements Propulsion {

    private final String name = "IonThruster";

    @Override
    public void launch() {
        System.out.println(name + " propulsion: Ion thrusters cannot provide launch thrust; aborting launch.");
    }

    @Override
    public void executeManeuver() {
        System.out.println(name + " propulsion: Executing low-thrust long-duration maneuver.");
    }

    // getFuelLevel() method is no longer here, as it was removed from the Propulsion interface.

    @Override
    public String toString() {
        return name;
    }
}