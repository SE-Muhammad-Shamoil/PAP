package defect;

/**
 * Propulsion groups launch + maneuver.
 * (FIXED: Removed unrelated getFuelLevel() method to adhere to ISP)
 */
public interface Propulsion extends Launchable, Maneuverable {
    // getFuelLevel() was removed.
}