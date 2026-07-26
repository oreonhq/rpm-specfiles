%global source0_hash cffde4b40d607b29204e19b9c67117bc6ce7e956dc98fe01344e2cb4e8a85437

%define snapshot .cvs20141002

Name:           FlightGear-Atlas
Summary:        Flightgear map tools
Version:        0.5.0
Release:        0.97%{snapshot}%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Source0:        Atlas-%{version}%{snapshot}.tar.bz2
Source1:        Atlas-0.5.0-default-maps.tar.bz2
Patch0:         Atlas-0.5.0-fix-unused-but-set-variable-warning.patch
Patch1:         Atlas-0.5.0-fix-narrowing-conversion-from-int-to-char-error.patch
Patch2:         Atlas-0.5.0-fix-operator-should-have-been-declared-inside-namespace-error.patch
Patch3:         Atlas-0.5.0-fix-removal-of-deprecated-function-in-sgtime.patch
Patch4:         Atlas-0.5.0-add-material-from-corine-landcover-classes.patch
Patch5:         Atlas-0.5.0-remove-assert-about-matching-navaids.patch
Patch6:         Atlas-0.5.0-fix-sgpath-api-change.patch 
URL:            http://atlas.sourceforge.net
BuildRequires:  gcc-c++
BuildRequires:  freeglut-devel, curl-devel, libpng-devel, glew-devel, boost-devel
BuildRequires:  SimGear-devel >= 2.6.0, OpenSceneGraph-devel, mesa-libEGL-devel
BuildRequires:  automake autoconf intltool libtool
BuildRequires: make
Requires:       FlightGear-data
Obsoletes:      fgfs-Atlas < 0.3.1-10

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

# the palette file must be installed
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

%files
%doc AUTHORS COPYING NEWS README
%{_bindir}/*
%{_datadir}/flightgear/Atlas

%changelog
%autochangelog
