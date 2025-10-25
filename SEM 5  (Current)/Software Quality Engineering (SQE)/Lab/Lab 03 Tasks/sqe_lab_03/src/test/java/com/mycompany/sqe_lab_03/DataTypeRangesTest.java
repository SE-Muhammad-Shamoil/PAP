package com.mycompany.sqe_lab_03;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class DataTypeRangesTest {

    @Test
    void testByteRange() {
        assertEquals(-128, DataTypeRanges.getByteMin());
        assertEquals(127, DataTypeRanges.getByteMax());}

    @Test
    void testShortRange() {
        assertEquals(-32768, DataTypeRanges.getShortMin());
        assertEquals(32767, DataTypeRanges.getShortMax());}

    @Test
    void testIntRange() {
        assertEquals(-2147483648, DataTypeRanges.getIntMin());
        assertEquals(2147483647, DataTypeRanges.getIntMax());}

    @Test
    void testLongRange() {
        assertEquals(-9223372036854775808L, DataTypeRanges.getLongMin());
        assertEquals(9223372036854775807L, DataTypeRanges.getLongMax());}

    @Test
    void testFloatRange() {
        assertEquals(Float.MIN_VALUE, DataTypeRanges.getFloatMin());
        assertEquals(Float.MAX_VALUE, DataTypeRanges.getFloatMax());}

    @Test
    void testDoubleRange() {
        assertEquals(Double.MIN_VALUE, DataTypeRanges.getDoubleMin());
        assertEquals(Double.MAX_VALUE, DataTypeRanges.getDoubleMax());}

    @Test
    void testCharRange() {
        assertEquals(0, DataTypeRanges.getCharMin());
        assertEquals(65535, DataTypeRanges.getCharMax());}
}

