%global source0_hash 17a47329509dfef123b5e2023a93d3a6730516052e40b8f1f46019ec3074b26f

Name:           iapetal
Version:        1.4
Release:        26%{?dist}
Summary:        A 2D space rescue game

License:        GPL-3.0-or-later
URL:            http://iapetal.sourceforge.net
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        iapetal.desktop
BuildArch:      noarch
BuildRequires:  desktop-file-utils
Requires:       python3-pygame python3-gobject hicolor-icon-theme

%description
Fly your lander carefully to rescue the scientists in the habitat module
from the falling asteroids.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/iapetal
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata

install -m 755 iapetal.py $RPM_BUILD_ROOT%{_bindir}/iapetal
install -m 755 iapetal-launcher.py $RPM_BUILD_ROOT%{_bindir}/iapetal-launcher
install -m 644 *.ogg $RPM_BUILD_ROOT%{_datadir}/iapetal/
install -m 644 *.png $RPM_BUILD_ROOT%{_datadir}/iapetal/
install -m 644 iapetal.appdata.xml $RPM_BUILD_ROOT%{_datadir}/appdata/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 habitat.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps

desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}

%files
%doc COPYING TODO
%{_bindir}/*
%{_datadir}/iapetal
%{_datadir}/applications/iapetal.desktop
%{_datadir}/icons/hicolor/32x32/apps/habitat.png
%{_datadir}/appdata/iapetal.appdata.xml

%changelog
%autochangelog
