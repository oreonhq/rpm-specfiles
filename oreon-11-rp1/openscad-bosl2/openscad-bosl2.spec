%global source0_hash a7274d7c2cd58e7e8d8b68ec6fc5142ca2964006160828d68efbc1a3032355f3

%global forgeurl https://github.com/BelfrySCAD/BOSL2
%global version 2.0.730

%forgemeta

Name:    openscad-bosl2
Version: %forgeversion
Release: %{autorelease}
Summary: BOSL2 library for OpenSCAD

License: BSD-2-Clause
URL:     %{forgeurl}
Source:  %{forgesource}

BuildArch:     noarch

# For running the tests
BuildRequires: openscad
BuildRequires: sed

Requires: openscad

%description
A library for OpenSCAD, filled with useful tools, shapes, masks, math and
manipulators, designed to make OpenSCAD easier to use.

BOSL2 is beta code. The code is still being reorganized.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build
#no build, only scad scripts

%install
install -dD -m755 %{buildroot}%{_datadir}/openscad/libraries/BOSL2

for FILE in *.scad; do
  install -p "$FILE" -m644 "%{buildroot}%{_datadir}/openscad/libraries/BOSL2/$FILE"
done

%check
# Missing dependency openscad-test
# ./scripts/run_tests.sh

%files
%license LICENSE
%doc README.md
%doc CONTRIBUTING.md
%doc tutorials
%doc examples
%{_datadir}/openscad/libraries/BOSL2

%changelog
%autochangelog
