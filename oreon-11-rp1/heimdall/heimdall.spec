%global source0_hash 7d01dd8bf9c2f93ea016ae8b059110c50cea49e78670e8a1333ebd5899cdaaa3
Name:           heimdall
Version:        2.2.2
Release:        1%{?dist}
Summary:        Flash firmware on to Samsung Galaxy S devices
License:        MIT
URL:            https://git.sr.ht/~grimler/Heimdall
Source0:        https://git.sr.ht/~grimler/Heimdall/archive/v%{version}.tar.gz
Source2:        %{name}.desktop
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libusb1-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
# /oreon:deps
%description
Heimdall is a cross-platform open-source utility to flash firmware
on to Samsung Galaxy S devices

%package frontend
Summary:        Qt4 based frontend for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description frontend
Heimdall is a cross-platform open-source utility to flash firmware
on to Samsung Galaxy S devices

This package provides Qt5 based frontend for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Heimdall-v%{version}

#remove unneeded files
rm -rf Win32
rm -rf OSX

%build

%{cmake}
%{cmake_build}
%install
%{cmake_install}
install -D -m 0755 %{_vpath_builddir}/bin/heimdall %{buildroot}%{_bindir}/heimdall
install -D -m 0755 %{_vpath_builddir}/bin/heimdall-frontend %{buildroot}%{_bindir}/heimdall-frontend
install -D -m 0644 heimdall/60-heimdall.rules %{buildroot}%{_udevrulesdir}/60-heimdall.rules
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE2}
mkdir -p %{buildroot}%{_datadir}/appdata
cat > %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!--
EmailAddress: contact@glassechidna.com.au
SentUpstream: 2014-09-18
-->
<application>
 <id type="desktop">heimdall.desktop</id>
 <metadata_license>CC0-1.0</metadata_license>
 <project_license>MIT</project_license>
 <name>Heimdall</name>
 <summary>Flash firmware onto Samsung mobile devices</summary>
 <description>
  <p>
   Heimdall is a cross-platform open-source tool suite used to flash
   firmware (aka ROMs) onto Samsung mobile devices.
  </p>
 </description>
 <screenshots>
  <screenshot type="default" width="1275" height="718">http://jorti.fedorapeople.org/appdata/heimdall.png</screenshot>
 </screenshots>
 <url type="homepage">http://glassechidna.com.au/heimdall/</url>
 <url type="donation">http://glassechidna.com.au/donate</url>
 <updatecontact>jorti@fedoraproject.org</updatecontact>
</application>
EOF
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n heimdall-frontend -f %{oreon_filedir}/heimdall-frontend.list

%changelog

%autochangelog
