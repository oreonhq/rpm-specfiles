%global source0_hash ea42d84960773bd3ec7bb412df61cbfb617a42f69db09ed337eef91ff94a8a97
Name:           office-runner
Version:        1.0.2
Release:        1%{?dist}
Summary:        Office game for laptop owners
License:        GPL-3.0-only
URL:            http://www.hadess.net/2011/09/omg-i-haz-designed-bug-fix.html
Source0:        http://ftp.gnome.org/pub/GNOME/sources/office-runner/1.0/office-runner-%{version}.tar.xz
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gnome-settings-daemon-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  make
# /oreon:deps
%description
This program is dedicated to office workers who want not to suspend their laptop
when moving between rooms meeting. office-runner inhibits suspend for 10 minutes 
when closing the lid and record their time when moving between meeting rooms.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure
make %{?_smp_mflags}
%install
%make_install
desktop-file-install \
--dir=%{buildroot}%{_datadir}/applications \
%{buildroot}/%{_datadir}/applications/office-runner.desktop
%find_lang %{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 William Moreno Reyes <williamjmorenor@gmail.com> -->
<!--
EmailAddress: hadess@hadess.net
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">office-runner.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Close your laptop lid and start running</summary>
  <description>
    <p>
      Office runner let you close your laptop lid and go quickly to a meeting or
      other place without having to wait until the computer turns off and then wake up.
    </p>
  </description>
  <url type="homepage">http://www.hadess.net/2011/09/omg-i-haz-designed-bug-fix.html</url>
  <screenshots>
    <screenshot type="default">http://2.bp.blogspot.com/-aJ2QmlyCCQ8/TnNgJniDNaI/AAAAAAAAAa8/jUiYw74gbjk/s1600/office-runner.png</screenshot>
  </screenshots>
</application>
EOF
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
