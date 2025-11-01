package defect;

public class RelayCommunication implements Communicable {

    private final String name = "Relay";

    @Override
    public void transmitData(String payload) { // Fixed signature to match Communicable interface
        System.out.println(name + " comms: Relaying telemetry via satellite -> " + payload);
    }

    @Override
    public String toString() {
        return name;
    }
}