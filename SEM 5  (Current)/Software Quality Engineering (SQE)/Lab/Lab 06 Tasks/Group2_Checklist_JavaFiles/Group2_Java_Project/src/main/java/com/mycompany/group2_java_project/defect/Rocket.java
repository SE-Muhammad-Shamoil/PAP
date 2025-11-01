package defect;

/**
 * (FIXED)
 */
public class Rocket {

    private static int rocketCount = 0; // (D-017) Made private

    // private int x; // Unused variable removed

    private Propulsion propulsion;
    private Landable landingSystem;
    private Communicable communicationSystem;

    // (D-011, D-016) Removed DIP-violating method and its side effect
    // public void setIonThruster(IonThrusterPropulsion ion) { ... }

    // private int internalState = 0; // Unused variable removed

    public Rocket(Propulsion propulsion, Landable landingSystem, Communicable communicationSystem) {
        this.propulsion = propulsion;
        this.landingSystem = landingSystem;
        this.communicationSystem = communicationSystem;
        rocketCount++; // Increment count on creation
    }

    public void setPropulsion(Propulsion p) { // (D-020) Fixed capitalization
        this.propulsion = p;
    }

    public void setLandingSystem(Landable landingSystem) {
        this.landingSystem = landingSystem;
    }

    public void setCommunicationSystem(Communicable communicationSystem) {
        this.communicationSystem = communicationSystem;
    }

    public void performLaunch() {
        if (propulsion == null) {
            throw new IllegalStateException("No propulsion system configured.");
        }
        System.out.println("Rocket: initiating launch using " + propulsion.toString());
        propulsion.launch();
        // int status = 1 / 0; // (D-001) Fixed critical divide-by-zero bug
        System.out.println("Rocket: Launch successful.");
    }

    public void performManeuver() {
        if (propulsion == null) {
            // (D-014) Fixed NPE by throwing exception
            throw new IllegalStateException("Warning: propulsion not configured!");
        }
        System.out.println("Rocket: executing maneuver via " + propulsion);
        propulsion.executeManeuver();
    }

    public void performLanding() {
        if (landingSystem == null) {
            throw new IllegalStateException("No landing system configured.");
        }
        System.out.println("Rocket: initiating landing using " + landingSystem);
        landingSystem.land(); // (D-002) This call now works

        // Removed useless retry loop
    }

    public void sendTelemetry(String payload) {
        try {
            if (communicationSystem == null) {
                throw new IllegalStateException("No communication system configured.");
            }
            System.out.println("Telemetry payload: " + payload);
            communicationSystem.transmitData(payload);
        } catch (Exception ex) {
            System.err.println("Error occurred during telemetry: " + ex.getMessage());
        } finally {
            System.out.println("Telemetry attempt complete.");
        }
    }

    // Removed deprecated finalize() method
}