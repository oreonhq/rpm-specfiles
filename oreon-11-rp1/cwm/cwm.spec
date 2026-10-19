%global source0_hash ec75056a5f57980d9f57076c4ae7d25a1e6903ea4e793c0a04b98e25edb0fc90
Summary:        Calm Window Manager by OpenBSD project
Name: cwm
Version: 7.9
Release:        1%{?dist}
License: ISC AND LicenseRef-Callaway-BSD
Url: https://github.com/chneukirchen/cwm
Source0:        http://chneukirchen.org/releases/%{name}-%{version}.tar.gz
Source1: %{name}.desktop
Source2: LICENSE
# oreon:deps
BuildRequires:  byacc
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  libXinerama
BuildRequires:  libXrandr-devel
BuildRequires:  make
BuildRequires:  pkgconf
# /oreon:deps
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

%{set_build_flags}
CFLAGS="$CFLAGS -D_GNU_SOURCE"
make %{?_smp_mflags}
%install
%{set_build_flags}
CFLAGS="$CFLAGS -D_GNU_SOURCE"
make PREFIX=%{_prefix} DESTDIR=%{buildroot} install
install -d %{buildroot}/%{_datadir}/xsessions
install -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/xsessions
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
