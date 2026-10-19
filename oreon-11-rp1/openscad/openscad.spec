%global source0_hash d938c297e7e5f65dbab1461cac472fc60dfeaa4999ea2c19b31a4184f2d70359
Name:           openscad
Version:        2021.01
%global upversion %{version}
Release:        1%{?dist}
Summary:        The Programmers Solid 3D CAD Modeller
License:        GPL-2.0-only WITH CGAL-linking-exception AND CC0-1.0
URL:            http://www.%{name}.org/
Source0:        http://files.%{name}.org/%{name}-%{version}.src.tar.gz
Patch0:         %{name}-polyclipping.patch
Patch1:         %{name}-cgal5.3.patch
%global github  https://github.com/openscad/openscad
Patch2:         %{name}-2021.01-fix-overloaded-join.patch
Patch3:         %{name}-2021.01-cgal-build-fix.patch
Patch4:         CVE-2022-0496.patch
Patch5:         CVE-2022-0497.patch
Patch6:         %{name}-2021.01-cgal6-cpp17.patch
Patch7:         %{name}-boost1.90.patch
ExcludeArch:    %{ix86}
Requires:       font(liberationmono)
Requires:       font(liberationsans)
Requires:       font(liberationserif)
Requires:       hicolor-icon-theme
Recommends:     %{name}-MCAD = %{version}-%{release}
%bcond_without 3mf
%if %{with 3mf}
%endif
# oreon:deps
BuildRequires:  CGAL-devel
BuildRequires:  ImageMagick
BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  double-conversion-devel
BuildRequires:  eigen3-devel
BuildRequires:  flex
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  glew-devel
BuildRequires:  glib2-devel
BuildRequires:  gmp-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  lib3mf-devel
BuildRequires:  libspnav-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  mesa-dri-drivers
BuildRequires:  mpfr-devel
BuildRequires:  mutter
BuildRequires:  opencsg-devel
BuildRequires:  pkgconfig(libzip)
BuildRequires:  polyclipping-devel
BuildRequires:  procps-ng
BuildRequires:  python3-devel
BuildRequires:  qscintilla-qt5-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtgamepad-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  xwfb-run
# /oreon:deps
%description
OpenSCAD is a software for creating solid 3D CAD objects.
Unlike most free software for creating 3D models (such as the famous
application Blender) it does not focus on the artistic aspects of 3D
modeling but instead on the CAD aspects. Thus it might be the application
you are looking for when you are planning to create 3D models of machine
parts but pretty sure is not what you are looking for when you are more
interested in creating computer-animated movies.

###############################################
%package        MCAD
Summary:        OpenSCAD Parametric CAD Library
License:        LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.1-only AND LGPL-3.0-or-later AND (GPL-3.0-only OR LGPL-2.1-only) AND (GPL-3.0-or-later OR LGPL-2.1-or-later) AND (CC-BY-SA-3.0 OR LGPL-2.0-or-later) AND CC-BY-3.0 AND BSD-2-Clause AND MIT AND LicenseRef-Fedora-Public-Domain
URL:            https://www.github.com/openscad/MCAD
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description    MCAD
This library contains components commonly used in designing and moching up
mechanical designs. It is currently unfinished and you can expect some API
changes, however many things are already working.

### LICENSES:

##  LGPL-2.0-or-later:
#   multiply.scad

##  LGPL-2.1-or-later:
#   2Dshapes.scad
#   3d_triangle.scad
#   gridbeam.scad
#   libtriangles.scad
#   shapes.scad
#   screw.scad
#   transformations.scad

##  LGPL-2.1-only:
#   fonts.scad
#   gears.scad
#   hardware.scad
#   involute_gears.scad
#   servos.scad
#   triangles.scad
#   unregular_shapes.scad
#   bitmap/letter_necklace.scad

##  LGPL-3.0-or-later:
#   teardrop.scad

##  GPL-3.0-only OR LGPL-2.1-only:
#   motors.scad
#   nuts_and_bolts.scad

##  GPL-3.0-or-later OR LGPL-2.1-or-later:
#   metric_fastners.scad
#   regular_shapes.scad

##  CC-BY-SA-3.0 OR LGPL-2.0-or-later:
#   bearing.scad
#   materials.scad
#   stepper.scad
#   units.scad
#   utilities.scad

##  CC-BY-3.0:
#   polyholes.scad
#   bitmap/alphabet_block.scad
#   bitmap/bitmap.scad
#   bitmap/height_map.scad
#   bitmap/name_tag.scad

##  BSD-2-Clause:
#   boxes.scad

##  MIT:
#   constants.scad
#   curves.scad
#   math.scad

##  LicenseRef-Fedora-Public-Domain:
#   lego_compatibility.scad
#   trochoids.scad

###############################################

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{upversion} -p1 -S git

# Unbundle polyclipping
rm src/ext/polyclipping -rf

# Remove unwanted things from MCAD, such as nonworking Python tests
pushd libraries/MCAD
for FILE in *.py; do
  rm -r $FILE
done
mv bitmap/README bitmap-README
popd

# Tests cmake check for MCAD by probing libraries/MCAD/__init__.py
# But we've just removed it
sed -i 's@MCAD/__init__.py@MCAD/gears.scad@' tests/CMakeLists.txt

%build

%{qmake_qt5} PREFIX=%{_prefix} VERSION=%{upversion} CONFIG-=debug
%make_build
cd tests
cmake -DPYTHON_EXECUTABLE:STRING=%{python3} .
%make_build
cd -
%install
make install INSTALL_ROOT=%{buildroot}
rm -rf %{buildroot}%{_datadir}/%{name}/fonts
%find_lang %{name}
for FILE in .gitignore lgpl-2.1.txt README.markdown TODO bitmap-README; do
  rm %{buildroot}%{_datadir}/%{name}/libraries/MCAD/$FILE
done
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
cd tests
xwfb-run -c mutter -- ctest %{?_smp_mflags} || : # let the tests fail, as they probably won't work in Koji
cd -
%files -f %{oreon_filedir}/main.list
%files -n openscad-MCAD -f %{oreon_filedir}/openscad-MCAD.list

%changelog

%autochangelog
