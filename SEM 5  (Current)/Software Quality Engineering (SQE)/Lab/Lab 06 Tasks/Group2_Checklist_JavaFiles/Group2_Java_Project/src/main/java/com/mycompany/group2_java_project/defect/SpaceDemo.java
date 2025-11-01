package defect;

import java.io.FileInputStream;
import java.io.InputStream;
import java.io.IOException; // Specific import

/**
 * (FIXED)
 */
public class SpaceDemo {

    public static String GLOBAL_STATUS = "OK";

    public static void main(String[] args) {
        // (D-018) Removed "magic number" as it's not used
        // int magic = 42;

        Propulsion solid = new SolidFuelPropulsion();
        Landable chute = new ParachuteLanding();
        Communicable rf = new RFCommunication();

        Rocket rocket = new Rocket(solid, chute, rf);

        // --- Rocket Mission ---
        rocket.performLaunch();
        rocket.performManeuver();
        rocket.sendTelemetry("Altitude=1000m;Status=Nominal;AuthToken=SECRET_TOKEN");
        rocket.performLanding();

        System.out.println("\n--- Swap systems at runtime (open for extension) ---\n");

        Propulsion ion = new IonThrusterPropulsion(); // (D-004) Fixed by implementing interface
        
        // (D-013) Fixed string comparison bug
        if ("IonThruster".equals(ion.toString())) { 
            rocket.setPropulsion(ion);
        } else {
            // (D-018) Removed dead code
        }

        rocket.setLandingSystem(new PoweredLanding());
        rocket.setCommunicationSystem(new LaserCommunication());

        // --- Second Mission Phase ---
        rocket.performManeuver(); // Maneuver with new Ion thruster
        rocket.sendTelemetry("Payload=DataPacket;Source=Laser");
        rocket.performLanding(); // Land with new powered system

        // (D-015) Fixed file handling and empty catch block
        try (InputStream in = new FileInputStream("config.file")) { // Example file
            int available = in.available();
            System.out.println("Config file size: " + available);
        } catch (IOException e) {
            System.err.println("Could not read config file: " + e.getMessage());
        }

        String[] samples = {"A", "B", "C"};
        // (D-003) Fixed ArrayIndexOutOfBoundsException
        for (int i = 0; i < samples.length; i++) { 
            rocket.sendTelemetry(samples[i]);
        }

        try {
            Thread.sleep(100); // Reduced magic number
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // Removed deprecated Runtime.runFinalization() and System.exit() calls
        
        System.out.println("Demo complete.");
        // Removed unused 'leftover' object
    }
}