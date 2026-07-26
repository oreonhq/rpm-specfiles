%global source0_hash c6210377103171a6e163b71eeb3e49a4659f326c1b7afdd311197444de39d1ce

%global appname GPXSee

Name:           gpxsee
Version:        16.0
Release:        1%{?dist}
Summary:        GPS log file viewer and analyzer

License:        GPL-3.0-only
URL:            https://www.gpxsee.org/

Source0:        https://github.com/tumic0/%{appname}/archive/%{version}/%{appname}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtlocation-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtserialport-devel
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  make

Recommends:     qt5-qtpbfimageformat

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

# localization
%find_lang %{name} --with-qt

%check
# appdata
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

# desktop file
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%license licence.txt
%doc README.md
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/CRS/
%{_datadir}/%{name}/maps/
%{_datadir}/%{name}/style/
%{_datadir}/%{name}/symbols/
%dir %{_datadir}/%{name}/translations
%{_datadir}/icons/*/*/*/%{name}.*
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml

%changelog
%autochangelog
