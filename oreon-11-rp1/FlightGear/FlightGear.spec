%global source0_hash f5555dfd0d4cd576cf77990d35f1d915f7ebccd7d91cd162abc6db3187ead9c3
%define _lto_cflags %{nil}
Name:           FlightGear
Summary:        The FlightGear Flight Simulator
Version:        2024.1.7
Release:        1%{?dist}
License:        GPL-2.0-or-later
Source0:        https://gitlab.com/flightgear/fgmeta/-/jobs/12799933767/artifacts/raw/fgbuild/flightgear-%{version}.tar.bz2
Patch:          0001-check-to-be-sure-that-n-is-not-being-set-as-format-t.patch
Patch:          0002-Use-system-iaxclient-instead-of-bundled-one.patch
Patch:          0003-make-fglauncher-a-static-library.patch
Patch:          0004-desktop-use-fgfs-wrapper.patch
Patch:          0005-make-fgqmlui-a-static-library.patch
Patch:          0006-fgviewer-fix-crash-on-exit.patch
URL:            http://www.flightgear.org/
Requires:       FlightGear-data >= %{version}, opengl-games-utils
Requires:	qt5-qtquickcontrols2
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  FlightGear-data
BuildRequires:  OpenSceneGraph-devel
BuildRequires:  SimGear-devel
BuildRequires:  boost-devel
BuildRequires:  bzip2-devel
BuildRequires:  cmake
BuildRequires:  dbus-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fltk-devel
BuildRequires:  fltk-fluid
BuildRequires:  freeglut-devel
BuildRequires:  glew-devel
BuildRequires:  iaxclient-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  libcurl-devel
BuildRequires:  libevent-devel
BuildRequires:  libpng-devel
BuildRequires:  openal-soft-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  sqlite-devel
BuildRequires:  systemd-devel
BuildRequires:  xz-devel
# /oreon:deps
%description
The Flight Gear project is working to create a sophisticated flight
simulator framework for the development and pursuit of interesting
flight simulator ideas. We are developing a solid basic sim that can be
expanded and improved upon by anyone interested in contributing

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n flightgear-%{version}
rm -rf 3rdparty/iaxclient

# make rpmlint happy
find -name \*.h -o -name \*.cpp -o -name \*.cxx -o -name \*.hxx \
        -o -name \*.hpp |xargs chmod -x
for f in docs-mini/README.xmlparticles Thanks
do
        iconv -f iso-8859-1 -t utf-8 -o ${f}.utf8 ${f}
        mv -f ${f}.utf8 ${f}
done
sed -i 's/\r//' docs-mini/AptNavFAQ.FlightGear.html
# remove some unneeded files for the doc section
for ext in Cygwin IRIX Joystick Linux MSVC MSVC8 MacOS SimGear Unix \
        Win32-X autoconf mingw plib src xmlsyntax 
do
        rm -f docs-mini/README.${ext}
done

%build

export CXXFLAGS="-fPIC $RPM_OPT_FLAGS"
%cmake \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DCMAKE_BUILD_TYPE=Release \
    -DSYSTEM_SQLITE=ON \
    -DFG_DATA_DIR:PATH=%{_datadir}/flightgear \
    -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name}
%cmake_build
%install
%cmake_install
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/fgfs-wrapper
rm -rf $RPM_BUILD_ROOT/usr/appdir
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
