package defect;

public class RFCommunication implements Communicable {

    private final String name = "RF";

    @Override
    public void transmitData(String payload) {
        try {
            System.out.println(name + " comms: Transmitting telemetry -> " + payload);
            if (payload.length() > 10) {
                throw new Exception("Simulated comms error");
            }
        } catch (Exception e) {
            // Re-throw as a runtime exception or handle, but don't just print stack trace
            System.err.println("RF Comms Failure: " + e.getMessage());
        }
    }

    @Override
    public String toString() {
        return name;
    }
}