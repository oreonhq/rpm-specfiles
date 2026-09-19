SETTING UP ROUTINO FOR USE WITH MARBLE
======================================

IMPORTANT: If you are upgrading from a release of Routino prior to 2.7.1, you
           MUST run these steps (at least step 4) again. Existing .mem files
           from previous releases of Routino (prior to 2.7.1) cannot be used
           with version 3.0.

Since Marble 1.0.0 (kdeedu 4.6.0), Marble supports computing routes using
Routino. The following instructions describe how to set that up:

1. Download one or more OpenStreetMap extract(s) in OSM PBF or OSM XML format.
   XML Files are usually compressed as *.osm.bz2, those can be opened directly
   by Routino.
   See http://wiki.openstreetmap.org/wiki/Planet.osm#Mirrors for possible
   download sites. For countries in Europe and for some other countries,
   http://download.geofabrik.de/osm/ is a good choice.

   IMPORTANT:
   * Starting from version 2.5, Routino supports the new binary .osm.pbf format,
     as well as any compressed .gz, .bz2 or, since 2.7, .xz input. Therefore, no
     advance conversion (pbf2osm) nor decompression should be needed anymore.
   * The larger the chosen map extract, the longer it takes to download and
     process. The processing time is not negligible, e.g. austria.osm.bz2 takes
     several minutes to download and approximately 50 minutes to process on a
     Pentium 4. Think twice before using the entire (16 GiB) planet.osm.bz2!
   * Some servers (e.g. downloads.cloudmade.com) have terms of service and/or
     acceptable usage policies restricting the fields of use.
   * You can use more than one input file. Sometimes, more than just a
     country-wide extract is needed for optimal routing, e.g. the optimum route
     from Vienna (Austria) to Innsbruck (Austria) goes through Germany.

2. Marble expects the data to be in a ~/.local/share/marble/maps/earth/routino
   directory, so create that directory now:
   mkdir ~/.local/share/marble/maps/earth/routino

3. Process the input (.osm.pbf, .osm.bz2, etc.) files with the
   routino-planetsplitter tool, setting the destination directory to the one
   expected by Marble.
   WARNING: This step may take minutes, hours or even days depending on the size
            of the input data and the speed of your computer!
   routino-planetsplitter --dir=$HOME/.local/share/marble/maps/earth/routino \
     *.osm.pbf
   (The routino-planetsplitter will accept an entire list of input files.)

4. If you want to use Routino's routing exclusively: In the Marble preferences,
   in the route planning tab, edit the profiles to disable all the other routing
   programs (especially the online services), keep only Routino checked. If you
   keep them checked, Marble will also query the web services and you can
   compare the computed routes (but you may want to check the web services'
   terms of use, e.g. OpenRouteService requires explicit approval for any
   commercial use).

5. Now you are ready to test your installation:
   Use the route planning applet on the left, select 2 places in whatever map
   section you downloaded in step 1 (and processed in step 3) and a locomotion
   method and see the route being computed.

        Kevin Kofler
