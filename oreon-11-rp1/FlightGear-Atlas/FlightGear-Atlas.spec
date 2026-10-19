%global source0_hash cffde4b40d607b29204e19b9c67117bc6ce7e956dc98fe01344e2cb4e8a85437
%define snapshot .cvs20141002
Name:           FlightGear-Atlas
Summary:        Flightgear map tools
Version:        0.5.0
Release:        1%{?dist}
License:        GPL-2.0-or-later
Source0:        Atlas-%{version}.cvs20141002.tar.bz2
Source1:        Atlas-0.5.0-default-maps.tar.bz2
Patch0:         Atlas-0.5.0-fix-unused-but-set-variable-warning.patch
Patch1:         Atlas-0.5.0-fix-narrowing-conversion-from-int-to-char-error.patch
Patch2:         Atlas-0.5.0-fix-operator-should-have-been-declared-inside-namespace-error.patch
Patch3:         Atlas-0.5.0-fix-removal-of-deprecated-function-in-sgtime.patch
Patch4:         Atlas-0.5.0-add-material-from-corine-landcover-classes.patch
Patch5:         Atlas-0.5.0-remove-assert-about-matching-navaids.patch
Patch6:         Atlas-0.5.0-fix-sgpath-api-change.patch 
URL:            http://atlas.sourceforge.net
Requires:       FlightGear-data
Obsoletes:      fgfs-Atlas < 0.3.1-10
# oreon:deps
BuildRequires:  OpenSceneGraph-devel
BuildRequires:  SimGear-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  curl-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  intltool
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mesa-libEGL-devel
# /oreon:deps
%description
Atlas aims to produce and display high quality charts of the world for
users of FlightGear, an open source flight simulator. This is achieved
through two main parts: The map creator (simply called Map) and the
Atlas viewer

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n Atlas
find -type f -name '*.[hc]xx' -exec chmod a-x {} \;

%build

./autogen.sh
%configure CXXFLAGS="$RPM_OPT_FLAGS -fPIC" \
        --with-fgbase=%{_datadir}/flightgear \
        --datadir=%{_datadir}/flightgear \
        --enable-simgear-shared
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/flightgear
tar jxf %{SOURCE1} -C $RPM_BUILD_ROOT%{_datadir}/flightgear
install -d $RPM_BUILD_ROOT%{_datadir}/flightgear/Atlas/Palettes
install -d $RPM_BUILD_ROOT%{_datadir}/flightgear/Atlas/Fonts
install -m 0644 src/data/Fonts/*.txf \
        $RPM_BUILD_ROOT%{_datadir}/flightgear/Atlas/Fonts
install -m 0644 src/data/Palettes/*.ap \
        $RPM_BUILD_ROOT%{_datadir}/flightgear/Atlas/Palettes
install -m 0644 src/data/background.jpg \
        $RPM_BUILD_ROOT%{_datadir}/flightgear/Atlas
install -m 0644 src/data/airplane_image.png \
        $RPM_BUILD_ROOT%{_datadir}/flightgear/Atlas
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
