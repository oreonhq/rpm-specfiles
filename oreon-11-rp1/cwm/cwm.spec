%global source0_hash b4f275143c8c716d7df1cfbb230f888c72aa861708e144d1749858f1cc6fcac0

Summary: Calm Window Manager by OpenBSD project
Name: cwm
Version: 7.4
Release: 7%{?dist}
# The entire source code is licensed under ISC license,
# except queue.h which is BSD
# Automatically converted from old format: ISC and BSD - review is highly recommended.
License: ISC AND LicenseRef-Callaway-BSD
Url: https://github.com/chneukirchen/cwm
Source0: http://chneukirchen.org/releases/%{name}-%{version}.tar.gz
Source1: %{name}.desktop
Source2: LICENSE
BuildRequires: gcc
BuildRequires: pkgconf
BuildRequires: byacc
BuildRequires: libX11-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama
BuildRequires: libXft-devel
BuildRequires: make

%description
cwm (calm window manager) is a window manager for X11 which contains many
features that concentrate on the efficiency and transparency of window
management, while maintaining the simplest and most pleasant aesthetic.

This package contains a Linux port of the official project, which changes the
source for the port portion but doesn't touches the original functionality
provided by the original OpenBSD's project.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
cp -a %{SOURCE2} .

%build
# The Makefile provides a default CFLAGS but RPM overrides it, without
# the -D_GNU_SOURCE
%{set_build_flags}
CFLAGS="$CFLAGS -D_GNU_SOURCE"
make %{?_smp_mflags}

%install
%{set_build_flags}
CFLAGS="$CFLAGS -D_GNU_SOURCE"
make PREFIX=%{_prefix} DESTDIR=%{buildroot} install
install -d %{buildroot}/%{_datadir}/xsessions
install -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/xsessions

%files
%doc README
%license LICENSE
%{_bindir}/*
%{_datadir}/xsessions/*
%{_mandir}/man1/*
%{_mandir}/man5/*

%changelog
%autochangelog
