package com.mycompany.sqe_lab_03;

public class DataTypeRanges {

    public static void main(String[] args) {
        System.out.println("Byte range: " + Byte.MIN_VALUE + " to " + Byte.MAX_VALUE);
        System.out.println("Short range: " + Short.MIN_VALUE + " to " + Short.MAX_VALUE);
        System.out.println("Integer range: " + Integer.MIN_VALUE + " to " + Integer.MAX_VALUE);
        System.out.println("Long range: " + Long.MIN_VALUE + " to " + Long.MAX_VALUE);
        System.out.println("Float range: " + Float.MIN_VALUE + " to " + Float.MAX_VALUE);
        System.out.println("Double range: " + Double.MIN_VALUE + " to " + Double.MAX_VALUE);
        System.out.println("Character range: " + (int) Character.MIN_VALUE + " to " + (int) Character.MAX_VALUE);
        System.out.println("Boolean values: " + Boolean.FALSE + " and " + Boolean.TRUE);
    }

    // Helper methods for testing
    public static byte getByteMin() { return Byte.MIN_VALUE; }
    public static byte getByteMax() { return Byte.MAX_VALUE; }
    public static short getShortMin() { return Short.MIN_VALUE; }
    public static short getShortMax() { return Short.MAX_VALUE; }
    public static int getIntMin() { return Integer.MIN_VALUE; }
    public static int getIntMax() { return Integer.MAX_VALUE; }
    public static long getLongMin() { return Long.MIN_VALUE; }
    public static long getLongMax() { return Long.MAX_VALUE; }
    public static float getFloatMin() { return Float.MIN_VALUE; }
    public static float getFloatMax() { return Float.MAX_VALUE; }
    public static double getDoubleMin() { return Double.MIN_VALUE; }
    public static double getDoubleMax() { return Double.MAX_VALUE; }
    public static char getCharMin() { return Character.MIN_VALUE; }
    public static char getCharMax() { return Character.MAX_VALUE; }
}
