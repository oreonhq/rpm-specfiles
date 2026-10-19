%global source0_hash 21500bd68975312a7f0f3ce6019d9f75f42aacaa75ca7115ec720b5445406896
%define enable_print_profiles 0
%define enable_sane 0
Summary:        Color daemon
Name:      colord
Version:   1.4.8
Release:        1%{?dist}
License:   GPL-2.0-or-later AND LGPL-2.1-or-later
URL:       https://www.freedesktop.org/software/colord/
Source0:        https://www.freedesktop.org/software/colord/releases/%{name}-%{version}.tar.xz
%if 0%{?enable_sane}
%endif
Requires: color-filesystem
%{?systemd_requires}
Requires: colord-libs%{?_isa} = %{version}-%{release}
Obsoletes: colord < 0.1.27-3
Obsoletes: shared-color-profiles <= 0.1.6-2
Provides: shared-color-profiles
# oreon:deps
BuildRequires:  color-filesystem
BuildRequires:  docbook5-style-xsl
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  libxslt
BuildRequires:  meson
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(gusb)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  vala
# /oreon:deps
%description
colord is a low level system activated daemon that maps color devices
to color profiles in the system context.

%package libs
Summary: Color daemon library
%description libs
colord is a low level system activated daemon that maps color devices
to color profiles in the system context.

%package devel
Summary: Development package for %{name}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libs = %{version}-%{release}
Obsoletes: colorhug-client-devel <= 0.1.13
%description devel
Files for development with %{name}.

%package devel-docs
Summary: Developer documentation package for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description devel-docs
Documentation for development with %{name}.

%package extra-profiles
Summary: More color profiles for color management that are less commonly used
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
Obsoletes: shared-color-profiles-extra <= 0.1.6-2
Provides: shared-color-profiles-extra
%description extra-profiles
More color profiles for color management that are less commonly used.
This may be useful for CMYK soft-proofing or for extra device support.

%package tests
Summary: Data files for installed tests
%description tests
Data files for installed tests.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

ulimit -Sv 2000000
%meson \
    -Dtests=false \
    -Dvapi=true \
    -Dinstalled_tests=true \
    -Dprint_profiles=false \
%if 0%{?enable_sane}
    -Dsane=true \
%endif
    -Ddaemon_user=colord
%meson_build
%install
%meson_install
touch $RPM_BUILD_ROOT%{_localstatedir}/lib/colord/mapping.db
touch $RPM_BUILD_ROOT%{_localstatedir}/lib/colord/storage.db
%find_lang %{name}
%oreon_autofiles colord-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles colord-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles colord-devel-docs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles colord-extra-profiles usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles colord-tests usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post colord.service
%preun

%systemd_preun colord.service
%postun

%systemd_postun colord.service
%ldconfig_scriptlets libs
%files -f %{oreon_filedir}/main.list
%files -n colord-libs -f %{oreon_filedir}/colord-libs.list
%files -n colord-devel -f %{oreon_filedir}/colord-devel.list
%files -n colord-devel-docs -f %{oreon_filedir}/colord-devel-docs.list
%files -n colord-extra-profiles -f %{oreon_filedir}/colord-extra-profiles.list
%files -n colord-tests -f %{oreon_filedir}/colord-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.8-1
- Prepare for Oreon 11 (RP1)
