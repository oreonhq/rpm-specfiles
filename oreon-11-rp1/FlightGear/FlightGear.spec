%global source0_hash f5555dfd0d4cd576cf77990d35f1d915f7ebccd7d91cd162abc6db3187ead9c3

# added temporarily due to errors in libqt5core
%define _lto_cflags %{nil}

Name:           FlightGear
Summary:        The FlightGear Flight Simulator
Version:        2024.1.4
Release:        1%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Source0:        https://gitlab.com/flightgear/fgmeta/-/jobs/12799933767/artifacts/raw/fgbuild/flightgear-%{version}.tar.bz2
Patch:          0001-check-to-be-sure-that-n-is-not-being-set-as-format-t.patch
Patch:          0002-Use-system-iaxclient-instead-of-bundled-one.patch
Patch:          0003-make-fglauncher-a-static-library.patch
Patch:          0004-desktop-use-fgfs-wrapper.patch
Patch:          0005-make-fgqmlui-a-static-library.patch
Patch:          0006-fgviewer-fix-crash-on-exit.patch

URL:            http://www.flightgear.org/
BuildRequires:  openal-soft-devel, SimGear-devel >= %{version}
BuildRequires:  libpng-devel, freeglut-devel, libXi-devel, libXmu-devel
BuildRequires:  OpenSceneGraph-devel >= 3.2.0, boost-devel >= 1.44.0
BuildRequires:  fltk-fluid, fltk-devel, dbus-devel, sqlite-devel, glew-devel
BuildRequires:  cmake, desktop-file-utils, iaxclient-devel, libevent-devel
BuildRequires:  bzip2-devel, systemd-devel, qt5-qtbase-devel, libcurl-devel
BuildRequires:  qt5-qtdeclarative-devel, qt5-qtsvg-devel, qt5-linguist, xz-devel
BuildRequires:  FlightGear-data >= %{version}
Requires:       FlightGear-data >= %{version}, opengl-games-utils
Requires:	qt5-qtquickcontrols2
Requires:       hicolor-icon-theme

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

%files
%doc AUTHORS NEWS README Thanks docs-mini/*
%license COPYING
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/bash-completion/completions/*
%{_datadir}/zsh/site-functions/*
%{_datadir}/metainfo/*.metainfo.xml

%changelog
%autochangelog
