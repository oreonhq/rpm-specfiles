%global source0_hash 47c8be99d7cb08b704d6065cff628b82417be44f386b9ae96c043cc6a51477fa
%global debug_package %{nil}
%global app_id org.gnome.Shell.Extensions.GSConnect
Name:           gnome-shell-extension-gsconnect
Version:        73
Release:        1%{?dist}
Summary:        KDE Connect implementation for GNOME Shell
License:        GPL-2.0-or-later
URL:            https://github.com/GSConnect/%{name}
Source0:        https://github.com/GSConnect/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        nautilus-gsconnect.metainfo.xml
Source2:        nemo-gsconnect.metainfo.xml
Patch0:         %{name}-42-firewalld.patch
Requires:       firewalld-filesystem
Requires:       gnome-shell
Requires:       openssh
Requires:       openssh-clients
Requires:       openssl
Requires:       /usr/bin/ffmpeg
Requires(post): firewalld-filesystem
Recommends:     evolution-data-server
Recommends:     (gsound or libcanberra-gtk3)
Suggests:       (nautilus-gsconnect = %{version}-%{release} if nautilus)
Suggests:       (nemo-gsconnect = %{version}-%{release} if nemo)
Suggests:       webextension-gsconnect = %{version}-%{release}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  firewalld-filesystem
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk4
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
# /oreon:deps
%description
The KDE Connect project allows devices to securely share content such as
notifications and files as well as interactive features such as SMS messaging
and remote input. The KDE Connect team maintains cross-desktop, Android and
Sailfish applications as well as an interface for KDE Plasma.

GSConnect is a complete implementation of KDE Connect especially for GNOME Shell
with Nautilus, Chrome and Firefox integration. It is does not rely on the KDE
Connect desktop application and will not work with it installed.

%package -n nautilus-gsconnect
Summary:        Nautilus extension for GSConnect
Requires:       gobject-introspection
Requires:       nautilus-extensions
Requires:       nautilus-python
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description -n nautilus-gsconnect
The nautilus-gsconnect package provides a Nautilus context menu for sending
files to devices that are online, paired and have the "Share and receive" plugin
enabled.

%package -n nemo-gsconnect
Summary:        Nemo extension for GSConnect
Requires:       gobject-introspection
Requires:       nemo-extensions
Requires:       nemo-python
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description -n nemo-gsconnect
The nemo-gsconnect package provides a Nemo context menu for sending files to
devices that are online, paired and have the "Share and receive" plugin enabled.

%package -n webextension-gsconnect
Summary:        Web browser integration for GSConnect
Requires:       mozilla-filesystem
Requires:       %{name} = %{version}-%{release}
%description -n webextension-gsconnect
The webextension-gsconnect package allows Google Chrome/Chromium, Firefox,
Vivaldi, Opera (and other Browser Extension, Chrome Extension or WebExtensions
capable browsers) to interact with GSConnect, using the Share plugin to open
links in device browsers and the Telephony plugin to share links with contacts
by SMS.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0

%build

%meson \
    -Dfirewalld=true \
    -Dinstalled_tests=false \
    -Dnemo=true
%meson_build
%install
%meson_install
install -Dpm 0644 %{SOURCE1} %{SOURCE2} -t $RPM_BUILD_ROOT%{_metainfodir}/
%find_lang %{app_id}
%oreon_autofiles nautilus-gsconnect usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles nemo-gsconnect usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles webextension-gsconnect usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate \
    $RPM_BUILD_ROOT%{_datadir}/applications/%{app_id}.desktop \
    $RPM_BUILD_ROOT%{_datadir}/applications/%{app_id}.Preferences.desktop
appstream-util validate-relax --nonet \
    $RPM_BUILD_ROOT%{_metainfodir}/nautilus-gsconnect.metainfo.xml \
    $RPM_BUILD_ROOT%{_metainfodir}/nemo-gsconnect.metainfo.xml \
    $RPM_BUILD_ROOT%{_metainfodir}/%{app_id}.metainfo.xml
%post

%firewalld_reload
%files -f %{oreon_filedir}/main.list
%files -n nautilus-gsconnect -f %{oreon_filedir}/nautilus-gsconnect.list
%files -n nemo-gsconnect -f %{oreon_filedir}/nemo-gsconnect.list
%files -n webextension-gsconnect -f %{oreon_filedir}/webextension-gsconnect.list

%changelog

%autochangelog
