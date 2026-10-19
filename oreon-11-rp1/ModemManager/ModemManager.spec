%global source0_hash 691aa026aee458d4e92f95be3fc19989c0484bf51b3ba00673c28909ce5b6729
%bcond check 1
%global glib2_version %(pkg-config --modversion glib-2.0 2>/dev/null || echo bad)
%global qmi_version %(pkg-config --modversion qmi-glib 2>/dev/null || echo bad)
%global mbim_version %(pkg-config --modversion mbim-glib 2>/dev/null || echo bad)
%global qrtr_version %(pkg-config --modversion qrtr-glib 2>/dev/null || echo bad)
%global forgeurl https://gitlab.freedesktop.org/mobile-broadband/ModemManager
Name: ModemManager
Version: 1.24.2
Release:        1%{?dist}
Summary:        Mobile broadband modem management service
License: GPL-2.0-or-later
URL: %{forgeurl}
Source0:        https://gitlab.freedesktop.org/mobile-broadband/ModemManager/-/archive/1.24.2/ModemManager-1.24.2.tar.bz2
Requires: libmbim-utils
Requires: libqmi-utils
Requires: %{name}-glib%{?_isa} = %{version}-%{release}
Conflicts: glib2%{?_isa} < %{glib2_version}
Conflicts: libqmi%{?_isa} < %{qmi_version}
Conflicts: libmbim%{?_isa} < %{mbim_version}
Conflicts: libqrtr-glib%{?_isa} < %{qrtr_version}
Requires(post): systemd
Requires(postun): systemd
Requires(preun): systemd
Requires: polkit
Recommends: xxd
%if %{with check}
%endif
%global __provides_exclude ^libmm-plugin-
# oreon:deps
BuildRequires:  dbus-daemon
BuildRequires:  dbus-devel
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  libgudev1-devel
BuildRequires:  libmbim-devel
BuildRequires:  libqmi-devel
BuildRequires:  libqrtr-glib-devel
BuildRequires:  meson
BuildRequires:  polkit-devel
BuildRequires:  python3-dbus
BuildRequires:  python3-gobject
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  vala
# /oreon:deps
%description
The ModemManager service manages WWAN modems and provides a consistent API for
interacting with these devices to client applications.

%package devel
Summary: Libraries and headers for adding ModemManager support to applications
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
%description devel
This package contains various headers for accessing some ModemManager functionality
from applications.

%package glib
Summary: Libraries for adding ModemManager support to applications that use glib.
License: LGPL-2.1-or-later
Requires: glib2 >= %{glib2_version}
%description glib
This package contains the libraries that make it easier to use some ModemManager
functionality from applications that use glib.

%package glib-devel
Summary: Libraries and headers for adding ModemManager support to applications that use glib.
License: LGPL-2.1-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Requires: %{name}-glib%{?_isa} = %{version}-%{release}
Requires: glib2-devel >= %{glib2_version}
Requires: pkgconfig
%description glib-devel
This package contains various headers for accessing some ModemManager functionality
from glib applications.

%package vala
Summary: Vala bindings for ModemManager
License: LGPL-2.1-or-later
Requires: vala
Requires: %{name}-glib%{?_isa} = %{version}-%{release}
%description vala
Vala bindings for ModemManager

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson \
	-Ddist_version='"%{version}-%{release}"' \
	-Dudevdir=/usr/lib/udev \
	-Dsystemdsystemunitdir=%{_unitdir} \
	-Ddbus_policy_dir=%{_datadir}/dbus-1/system.d \
	-Dvapi=true \
	-Dgtk_doc=true \
	-Dpolkit=permissive \
	-Dbash_completion=false
%meson_build
%install
%meson_install
find %{buildroot}%{_datadir}/gtk-doc |xargs touch --reference meson.build
%find_lang %{name}
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
cp -a cli/mmcli-completion %{buildroot}%{_datadir}/bash-completion/completions/mmcli
%oreon_autofiles ModemManager-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles ModemManager-glib usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ModemManager-glib-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles ModemManager-vala usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%meson_test
%endif
%post

%systemd_post ModemManager.service
%preun

%systemd_preun ModemManager.service
%postun

%systemd_postun ModemManager.service
%files -f %{oreon_filedir}/main.list
%files -n ModemManager-devel -f %{oreon_filedir}/ModemManager-devel.list
%files -n ModemManager-glib -f %{oreon_filedir}/ModemManager-glib.list
%files -n ModemManager-glib-devel -f %{oreon_filedir}/ModemManager-glib-devel.list
%files -n ModemManager-vala -f %{oreon_filedir}/ModemManager-vala.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.24.2-1
- Prepare for Oreon 11 (RP1)
