package defect;

public class LaserCommunication implements Communicable {

    private final String name = "Laser";

    @Override
    public void transmitData(String payload) {
        System.out.println(name + " comms: Sending high-bandwidth laser packet -> " + payload);
    }

    @Override
    public String toString() {
        return name;
    }
}