# OBS runs rpmbuild from SPECS, so include the bundled spec via SOURCES path.
# Keep qca-bundled.spec in this package directory and sync from ../qca/qca.spec.
%include %{_sourcedir}/qca-bundled.spec
