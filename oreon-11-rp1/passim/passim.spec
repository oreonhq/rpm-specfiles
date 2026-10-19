%global source0_hash 400de22e7425930e50d4ae21005b39baf4a511b382378293aa255d20faf215c2
%global glib2_version 2.45.8
%global systemd_version 231
Summary:        Local caching server
Name:      passim
Version:   0.1.12
Release:        1%{?dist}
License:   LGPL-2.1-or-later
URL:       https://github.com/hughsie/%{name}
Source0:        https://github.com/hughsie/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Recommends: avahi
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes: %{name} < 0.1.1-3
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  glib2-devel
BuildRequires:  gnutls-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  libappstream-glib
BuildRequires:  libsoup3-devel
BuildRequires:  meson
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Passim is a daemon that allows software to share files on your local network.

%package libs
Summary: Local caching server library
Obsoletes: %{name} < 0.1.1-3
%description libs
libpassim is a library that allows software to share files on your local network
using the passimd daemon.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Files for development with %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
rm %{buildroot}/var/lib/passim/data/*
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%post

%systemd_post passim.service
%preun

%systemd_preun passim.service
%postun

%systemd_postun_with_restart passim.service
%files -f %{oreon_filedir}/main.list
%files -n passim-libs -f %{oreon_filedir}/passim-libs.list
%files -n passim-devel -f %{oreon_filedir}/passim-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1.10-1
- Prepare for Oreon 11 (RP1)
