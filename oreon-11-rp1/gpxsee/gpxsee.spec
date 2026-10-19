%global source0_hash 2456cbfa127b12bb971760175420aba6369d771f3a586558501d261964ccf333
%global appname GPXSee
Name:           gpxsee
Version:        16.15
Release:        1%{?dist}
Summary:        GPS log file viewer and analyzer
License:        GPL-3.0-only
URL:            https://www.gpxsee.org/
Source0:        https://github.com/tumic0/%{appname}/archive/%{version}/%{appname}-%{version}.tar.gz
Recommends:     qt5-qtpbfimageformat
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtlocation-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtserialport-devel
BuildRequires:  qt5-qtsvg-devel
# /oreon:deps
%description
GPS log file viewer and analyzer with support for
GPX, TCX, KML, FIT, IGC and NMEA files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{appname}-%{version}

%build

lrelease-qt5 %{name}.pro
%{qmake_qt5} PREFIX=/usr %{name}.pro
%make_build
%install
%make_install INSTALL_ROOT=%{buildroot}
%find_lang %{name} --with-qt
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
