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
BuildRequires: desktop-file-utils
BuildRequires: intltool
BuildRequires: libappstream-glib
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-wheel
BuildRequires: rb_libtorrent-python3
BuildRequires: systemd-rpm-macros

## add Requires to make into Meta package
Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-gtk = %{version}-%{release}
Requires: %{name}-images = %{version}-%{release}
Requires: %{name}-console = %{version}-%{release}
Requires: %{name}-web = %{version}-%{release}
Requires: %{name}-daemon = %{version}-%{release}

%description
Deluge is a new BitTorrent client, created using Python and GTK+. It is
intended to bring a native, full-featured client to Linux GTK+ desktop
environments such as GNOME and XFCE. It supports features such as DHT
(Distributed Hash Tables), PEX (µTorrent-compatible Peer Exchange), and UPnP
(Universal Plug-n-Play) that allow one to more easily share BitTorrent data
even from behind a router with virtually zero configuration of port-forwarding.

%package common
Summary:    Files common to Deluge sub packages
# Automatically converted from old format: GPLv3 with exceptions - review is highly recommended.
License:    LicenseRef-Callaway-GPLv3-with-exceptions
Requires:   rb_libtorrent-python3
Requires:   python3-service-identity
Recommends: python3-GeoIP

%description common
Common files needed by the Deluge bittorrent client sub packages

%package gtk
Summary:    The gtk UI to Deluge
# Automatically converted from old format: GPLv3 with exceptions - review is highly recommended.
License:    LicenseRef-Callaway-GPLv3-with-exceptions
Requires:   %{name}-common = %{version}-%{release}
Requires:   %{name}-images = %{version}-%{release}
Requires:   %{name}-daemon = %{version}-%{release}
## Required for the proper ownership of icon dirs.
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
# Automatically converted from old format: GPLv3 with exceptions - review is highly recommended.
License:    LicenseRef-Callaway-GPLv3-with-exceptions
%description images
Data files used by the GTK and web user interface for Deluge bittorent client

%package console
Summary:    CLI to Deluge
# Automatically converted from old format: GPLv3 with exceptions - review is highly recommended.
License:    LicenseRef-Callaway-GPLv3-with-exceptions
Requires:   %{name}-common = %{version}-%{release}
Requires:   %{name}-daemon = %{version}-%{release}
%description console
Deluge bittorent client command line interface

%package web
Summary:    Web interface to Deluge
# Automatically converted from old format: GPLv3 with exceptions - review is highly recommended.
License:    LicenseRef-Callaway-GPLv3-with-exceptions
Requires:   python3-mako
Requires:   %{name}-common = %{version}-%{release}
Requires:   %{name}-images = %{version}-%{release}
Requires:   %{name}-daemon = %{version}-%{release}

%description web
Deluge bittorent client web interface

%package daemon
Summary:    The Deluge daemon
# Automatically converted from old format: GPLv3 with exceptions - review is highly recommended.
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

# http://dev.deluge-torrent.org/ticket/2034
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

## NOTE: The lang files should REEEAALLLY be in a standard place such as
##       /usr/share/locale or similar. It'd make things so much nicer for
##       the packaging. :O
## A bit of sed magic to mark the translation files with %%lang, taken from
## find-lang.sh (part of the rpm-build package) and tweaked somewhat. We
## cannot (unfortunately) call find-lang directly since it's not on a
## "$PREFIX/share/locale/"-ish directory tree.

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

## Now we move that list back to our sources, so that '%%files -f' can find it
## properly.
popd && mv %{buildroot}/%{name}.lang .

install -m0644 -D deluge.sysusers.conf %{buildroot}%{_sysusersdir}/deluge.conf

%files

%files common -f %{name}.lang
%doc CHANGELOG.md LICENSE README.md

%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info/
%dir %{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}/__pycache__
%{python3_sitelib}/%{name}/*.py*
%{python3_sitelib}/%{name}/plugins
%{python3_sitelib}/%{name}/core
%dir %{python3_sitelib}/%{name}/ui
%{python3_sitelib}/%{name}/ui/__pycache__
%{python3_sitelib}/%{name}/ui/*.py*
# includes %%name.pot too
%dir %{python3_sitelib}/%{name}/i18n
%dir %{python3_sitelib}/%{name}/i18n/*
%dir %{python3_sitelib}/%{name}/i18n/*/LC_MESSAGES
%{python3_sitelib}/%{name}/i18n/__pycache__/*
%{python3_sitelib}/%{name}/i18n/*.py

%files images
# only pixmaps dir is in data so I own it all
%{python3_sitelib}/%{name}/ui/data
# if someone decides to only install images
%dir %{python3_sitelib}/%{name}

%files gtk
%{_bindir}/%{name}
%{_bindir}/%{name}-gtk
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_datadir}/pixmaps/%{name}.*
%{_metainfodir}/%{name}.metainfo.xml
%{python3_sitelib}/%{name}/ui/gtk3
%{_mandir}/man?/%{name}-gtk*
%{_mandir}/man?/%{name}.1*

%files console
%{_bindir}/%{name}-console
%{python3_sitelib}/%{name}/ui/console
%{_mandir}/man?/%{name}-console*

%files web
%{_bindir}/%{name}-web
%{python3_sitelib}/%{name}/ui/web
%{_mandir}/man?/%{name}-web*
%{_unitdir}/%{name}-web.service

%files daemon
%{_bindir}/%{name}d
%{_unitdir}/%{name}-daemon.service
%attr(-,%{name}, %{name})%{_sharedstatedir}/%{name}/
%{_mandir}/man?/%{name}d*
%{_sysusersdir}/deluge.conf

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

%changelog
%autochangelog
