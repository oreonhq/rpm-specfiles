%global source0_hash 09164faec92ad38dcec248339f7fc83c7a74e484e0a4105ebce3a3a41b172364
%global glib2_version 2.80
%global libdnf_version 0.43.1
%global libdnf5_version 5.2.17.0
%bcond dnf5_default %[0%{?fedora} >= 44 || 0%{?rhel} >= 11]
%bcond dnf4 %[(0%{?rhel} && 0%{?rhel} < 11) || (0%{?fedora} && 0%{?fedora} < 44)]
Summary:        Package management service
Name:      PackageKit
Version:   1.4.0
Release:        1%{?dist}
License:   GPL-2.0-or-later AND LGPL-2.1-or-later AND FSFAP
URL:       http://www.freedesktop.org/software/PackageKit/
Source0:        http://www.freedesktop.org/software/PackageKit/releases/%{name}-%{version}.tar.xz
Patch1001:    package-inst+rem-sysupgrade-password-prompt.patch
Patch2001:    PackageKit-1.4.0-Fedora-Vendor.conf.patch
Patch3001:    PackageKit-1.4.0-RHEL-Vendor.conf.patch
%if %{with dnf4}
Requires: libdnf%{?_isa} >= %{libdnf_version}
%endif
Requires: %{name}-glib%{?_isa} = %{version}-%{release}
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: shared-mime-info
Requires: systemd
Obsoletes: PackageKit-udev-helper < %{version}-%{release}
Obsoletes: udev-packagekit < %{version}-%{release}
Obsoletes: PackageKit-gtk-module < %{version}-%{release}
Obsoletes: PackageKit-smart < %{version}-%{release}
Obsoletes: PackageKit-yum < 0.9.1
Obsoletes: PackageKit-yum-plugin < 0.9.1
Obsoletes: PackageKit-zif < 0.8.13-2
Obsoletes: PackageKit-debug-install < 0.9.1
Obsoletes: PackageKit-hawkey < 0.9.1
Obsoletes: PackageKit-backend-devel < 0.9.6
Obsoletes: PackageKit-device-rebind < 0.8.13-2
%if ! %{with dnf4}
Obsoletes: dnf4-plugin-notify-PackageKit < %{version}-%{release}
Obsoletes: libdnf5-plugin-notify-PackageKit < %{version}-%{release}
%endif
%if %{with dnf5_default}
Requires: libdnf5%{?_isa} >= %{libdnf5_version}
Requires: libdnf5-plugin-appstream%{?_isa}
Obsoletes: PackageKit-backend-dnf5 < %{version}-%{release}
Provides: PackageKit-backend-dnf5 = %{version}-%{release}
Provides: PackageKit-backend-dnf5%{?_isa} = %{version}-%{release}
Provides: PackageKit-dnf5 = %{version}-%{release}
Provides: PackageKit-dnf5%{?_isa} = %{version}-%{release}
%endif
# oreon:deps
BuildRequires:  docbook-utils
BuildRequires:  docbook5-schemas
BuildRequires:  docbook5-style-xsl
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libdnf5)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(ply-boot-client)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(sdbus-c++)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  python3-devel
BuildRequires:  systemd
BuildRequires:  vala
BuildRequires:  xmlto
# /oreon:deps
%description
PackageKit is a D-Bus abstraction layer that allows the session user
to manage packages in a secure way using a cross-distro,
cross-architecture API.

%if ! %{with dnf5_default}
%package backend-dnf5
Summary: DNF5 backend for PackageKit
%dnl Supplements: (libdnf5%{?_isa} and PackageKit%{?_isa})
Provides: %{name}-dnf5 = %{version}-%{release}
Provides: %{name}-dnf5%{?_isa} = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libdnf5%{?_isa} >= %{libdnf5_version}
Requires: libdnf5-plugin-appstream%{?_isa}
%description backend-dnf5
PackageKit is a D-Bus abstraction layer that allows the session user
to manage packages in a secure way using a cross-distro,
cross-architecture API.

This package provides the DNF5 backend for PackageKit.
%endif

%if %{with dnf4}
%package -n dnf4-plugin-notify-PackageKit
Summary: DNF4 plugin to notify PackageKit of DNF4 actions
Supplements: (dnf4 and PackageKit)
Conflicts: %{name} < 1.3.1-3
BuildArch: noarch
%description -n dnf4-plugin-notify-PackageKit
DNF4 plugin to notify PackageKit of DNF4 actions.

%package -n libdnf5-plugin-notify-PackageKit
Summary: DNF5 plugin to notify PackageKit of DNF5 actions
Supplements: (libdnf5%{?_isa} and PackageKit%{?_isa})
Conflicts: %{name} < 1.3.1-2
%description -n libdnf5-plugin-notify-PackageKit
DNF5 plugin to notify PackageKit of DNF5 actions.
%endif

%package glib
Summary: GLib libraries for accessing PackageKit
Requires: dbus >= 1.1.1
Requires: glib2 >= %{glib2_version}
Obsoletes: PackageKit-libs < %{version}-%{release}
Provides: PackageKit-libs = %{version}-%{release}
%description glib
GLib libraries for accessing PackageKit.

%package cron
Summary: Cron job and related utilities for PackageKit
Requires: crontabs
Requires: %{name}%{?_isa} = %{version}-%{release}
%description cron
Crontab and utilities for running PackageKit as a cron job.

%package devel
Summary: Libraries and headers for PackageKit
Requires: %{name}-glib-devel%{?_isa} = %{version}-%{release}
Requires: %{name}-gtk3-module%{?_isa} = %{version}-%{release}
Requires: %{name}-gstreamer-plugin%{?_isa} = %{version}-%{release}
%description devel
Headers and libraries for PackageKit.

%package glib-devel
Summary: GLib Libraries and headers for PackageKit
Requires: %{name}-glib%{?_isa} = %{version}-%{release}
Requires: dbus-devel%{?_isa} >= 1.1.1
Requires: sqlite-devel%{?_isa}
Obsoletes: PackageKit-docs < %{version}-%{release}
Provides: PackageKit-docs = %{version}-%{release}
%description glib-devel
GLib headers and libraries for PackageKit.

%package gstreamer-plugin
Summary: Install GStreamer codecs using PackageKit
Requires: %{name}-glib%{?_isa} = %{version}-%{release}
Obsoletes: codeina < 0.10.1-10
Provides: codeina = 0.10.1-10
%description gstreamer-plugin
The PackageKit GStreamer plugin allows any Gstreamer application to install
codecs from configured repositories using PackageKit.

%package gtk3-module
Summary: Install fonts automatically using PackageKit
Requires: pango
Requires: %{name}-glib%{?_isa} = %{version}-%{release}
%description gtk3-module
The PackageKit GTK3+ module allows any Pango application to install
fonts from configured repositories using PackageKit.

%package command-not-found
Summary: Ask the user to install command line programs automatically
Requires: bash
Requires: %{name} = %{version}-%{release}
Requires: %{name}-glib%{?_isa} = %{version}-%{release}
%description command-not-found
A simple helper that offers to install new packages on the command line
using PackageKit.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -N

# Fun patching times :)
%autopatch -p1 -M 2000

%conf
%meson \
        -Dgtk_doc=true \
        -Dpython_backend=false \
        -Dpackaging_backend=%{?with_dnf4:dnf,}dnf5 \
        -Dlegacy_tools=true

%build

%meson_build
%install
%meson_install
mkdir -p %{buildroot}%{_localstatedir}/cache/PackageKit
%if %{with dnf4}
mkdir -p %{buildroot}%{_localstatedir}/cache/app-info/{icons,xmls}
%endif
pushd %{buildroot}%{_libexecdir} > /dev/null
ln -s pk-gstreamer-install gst-install-plugins-helper
popd > /dev/null
%find_lang %{name}
%oreon_autofiles PackageKit-glib usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles PackageKit-cron usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles PackageKit-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles PackageKit-glib-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles PackageKit-gstreamer-plugin usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles PackageKit-gtk3-module usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles PackageKit-command-not-found usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml || :
%post

systemctl disable packagekit-offline-update.service > /dev/null 2>&1 || :
%files -f %{oreon_filedir}/main.list
%files -n PackageKit-glib -f %{oreon_filedir}/PackageKit-glib.list
%files -n PackageKit-cron -f %{oreon_filedir}/PackageKit-cron.list
%files -n PackageKit-devel -f %{oreon_filedir}/PackageKit-devel.list
%files -n PackageKit-glib-devel -f %{oreon_filedir}/PackageKit-glib-devel.list
%files -n PackageKit-gstreamer-plugin -f %{oreon_filedir}/PackageKit-gstreamer-plugin.list
%files -n PackageKit-gtk3-module -f %{oreon_filedir}/PackageKit-gtk3-module.list
%files -n PackageKit-command-not-found -f %{oreon_filedir}/PackageKit-command-not-found.list

%changelog

%autochangelog
