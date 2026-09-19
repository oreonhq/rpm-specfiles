%global source0_hash f0a4510d9fe5eae4c91b63ade9848992b2795108e76eff7f51dc3decf7df2cb1

# first two digits of version
%global release_version %%(echo %{version} | awk -F. '{print $1"."$2}')

Name:           gnome-nettool
Version:        3.8.1
Release:        34%{?dist}
Summary:        Network information tool for GNOME

# Automatically converted from old format: GPLv2+ and GFDL - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:            https://gitlab.gnome.org/GNOME/gnome-nettool
Source0:        https://download.gnome.org/sources/gnome-nettool/%{release_version}/gnome-nettool-%{version}.tar.xz

# Backported from upstream
# https://gitlab.gnome.org/GNOME/gnome-nettool/merge_requests/2
Patch0:         fix-scalable-icon.patch

BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libgtop2-devel
BuildRequires: make

Requires:       bind-utils
Requires:       coreutils
Requires:       iputils
Requires:       net-tools
Requires:       nmap
Requires:       traceroute
Requires:       whois

%description
GNOME Nettool is a front-end to various networking command-line
tools, like ping, netstat, ifconfig, whois, traceroute, finger.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure --disable-compile-warnings
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: https://bugzilla.gnome.org/show_bug.cgi?id=736831
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">gnome-nettool.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Perform advanced networking analysis</summary>
  <description>
    <p>
      Network Tools is a utility to perform advanced networking analysis
      operations.
      It features a range of networking tools that are typically done on
      the command line, but allows you to perform them with a graphical
      interface.
      With Network Tools, you can perform the following: ping, netstat,
      traceroute, port scans, lookup, finger and whois.
    </p>
  </description>
  <url type="homepage">http://projects.gnome.org/gnome-network/</url>
  <screenshots>
    <screenshot type="default">https://projects.gnome.org/gnome-network/screenshots/info_info.jpg</screenshot>
    <screenshot>https://projects.gnome.org/gnome-network/screenshots/info_netstat.jpg</screenshot>
    <screenshot>https://projects.gnome.org/gnome-network/screenshots/info_lookup.jpg</screenshot>
  </screenshots>
</application>
EOF

%find_lang gnome-nettool --with-gnome

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/gnome-nettool.desktop

%files -f gnome-nettool.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/gnome-nettool
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/gnome-nettool.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-nettool.gschema.xml
%{_datadir}/gnome-nettool/
%{_datadir}/icons/hicolor/*/apps/gnome-nettool.png
%{_datadir}/icons/hicolor/scalable/apps/gnome-nettool.svg

%changelog
%autochangelog
