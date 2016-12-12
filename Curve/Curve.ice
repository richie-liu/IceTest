
#pragma once

module Demo
{

    sequence<string> Pillars;
    interface Curve
    {
        idempotent void sayCurve(int delay);
        float getDiscount(int date);
        idempotent Pillars getPillars();
        void shutdown();
    };

};
