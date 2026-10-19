%global source1_hash fa8158a1fd188a125e089e22afb9a1df3aee1f14936ad6e24d40b1d876afff4d
%global source0_hash b9ba272b5ba42aaf1c694e6c29628ab816cc1a700a37bac08aacb52571606acd
Name:           deluge
Version:        2.2.0
Release:        7%{?dist}
Summary:        A GTK+ BitTorrent client with support for DHT, UPnP, and PEX
License:        LicenseRef-Callaway-GPLv3-with-exceptions
URL:            http://deluge-torrent.org/
Source0:        https://ftp.osuosl.org/pub/deluge/source/2.2/%{name}-%{version}.tar.xz
Source1:        https://ftp.osuosl.org/pub/deluge/source/2.2/%{name}-%{version}.tar.xz.sha256
Source2:        deluge-daemon.service
Source3:        deluge-web.service
BuildArch:     noarch
Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-gtk = %{version}-%{release}
Requires: %{name}-images = %{version}-%{release}
Requires: %{name}-console = %{version}-%{release}
Requires: %{name}-web = %{version}-%{release}
Requires: %{name}-daemon = %{version}-%{release}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  rb_libtorrent-python3
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Deluge is a new BitTorrent client, created using Python and GTK+. It is
intended to bring a native, full-featured client to Linux GTK+ desktop
environments such as GNOME and XFCE. It supports features such as DHT
(Distributed Hash Tables), PEX (µTorrent-compatible Peer Exchange), and UPnP
(Universal Plug-n-Play) that allow one to more easily share BitTorrent data
even from behind a router with virtually zero configuration of port-forwarding.

%package common
Summary:    Files common to Deluge sub packages
License:    LicenseRef-Callaway-GPLv3-with-exceptions
Requires:   rb_libtorrent-python3
Requires:   python3-service-identity
Recommends: python3-GeoIP
%description common
Common files needed by the Deluge bittorrent client sub packages

%package gtk
Summary:    The gtk UI to Deluge
License:    LicenseRef-Callaway-GPLv3-with-exceptions
Requires:   %{name}-common = %{version}-%{release}
Requires:   %{name}-images = %{version}-%{release}
Requires:   %{name}-daemon = %{version}-%{release}
Requires:   hicolor-icon-theme
Requires:   gtk3 >= 3.10
Requires:   python3-cairo
Requires:   python3-gobject
Requires:   libappindicator-gtk3
Requires:   librsvg2
Recommends: python3-dbus
Recommends: python3-pygame
%description gtk
Deluge bittorent client GTK graphical user interface

%package images
Summary:    Image files for deluge
License:    LicenseRef-Callaway-GPLv3-with-exceptions
%description images
Data files used by the GTK and web user interface for Deluge bittorent client

%package console
Summary:    CLI to Deluge
License:    LicenseRef-Callaway-GPLv3-with-exceptions
Requires:   %{name}-common = %{version}-%{release}
Requires:   %{name}-daemon = %{version}-%{release}
%description console
Deluge bittorent client command line interface

%package web
Summary:    Web interface to Deluge
License:    LicenseRef-Callaway-GPLv3-with-exceptions
Requires:   python3-mako
Requires:   %{name}-common = %{version}-%{release}
Requires:   %{name}-images = %{version}-%{release}
Requires:   %{name}-daemon = %{version}-%{release}
%description web
Deluge bittorent client web interface

%package daemon
Summary:    The Deluge daemon
License:    LicenseRef-Callaway-GPLv3-with-exceptions
Requires:   %{name}-common = %{version}-%{release}
%description daemon
Files for the Deluge daemon

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Create a sysusers.d config file
cat >deluge.sysusers.conf <<EOF
u deluge - 'deluge daemon account' %{_sharedstatedir}/%{name} -
EOF

%build

%py3_build
%install
%py3_install
mkdir -p %{buildroot}%{_unitdir}
install -m644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}-daemon.service
install -m644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}-web.service
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}
desktop-file-install  \
    --dir %{buildroot}%{_datadir}/applications    \
    --copy-name-to-generic-name            \
    --add-mime-type=application/x-bittorrent    \
    --delete-original                \
    --remove-category=Application            \
    %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
pushd %{buildroot}
    find -type f -o -type l \
        | sed '
            s:%{buildroot}%{python3_sitelib}::
            s:^\.::
            s:\(.*/deluge/i18n/\)\([^/_]\+\)\(.*\.mo$\):%lang(\2) \1\2\3:
            s:^\([^%].*\)::
            s:%lang(C) ::
            /^$/d' \
    > %{name}.lang
popd && mv %{buildroot}/%{name}.lang .
install -m0644 -D deluge.sysusers.conf %{buildroot}%{_sysusersdir}/deluge.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post daemon

%systemd_post deluge-daemon.service
%post web

%systemd_post deluge-web.service
%preun daemon

%systemd_preun deluge-daemon.service
%preun web

%systemd_preun deluge-web.service
%postun daemon

%systemd_postun_with_restart deluge-daemon.service
%postun web

%systemd_postun_with_restart deluge-web.service
%files -f %{oreon_filedir}/main.list
%files -n deluge-common -f %{oreon_filedir}/deluge-common.list
%files -n deluge-gtk -f %{oreon_filedir}/deluge-gtk.list
%files -n deluge-images -f %{oreon_filedir}/deluge-images.list
%files -n deluge-console -f %{oreon_filedir}/deluge-console.list
%files -n deluge-web -f %{oreon_filedir}/deluge-web.list
%files -n deluge-daemon -f %{oreon_filedir}/deluge-daemon.list

%changelog

%autochangelog
