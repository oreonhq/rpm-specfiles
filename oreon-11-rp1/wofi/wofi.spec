%global source0_hash 6216dc14d93cdb6170f89c1ca3aaacdeaa44862fbc9be947d614be266a9c49f6
Name:		wofi
Summary:        A launcher/menu program for wlroots based wayland compositors
Version:	1.5.3
Release:        1%{?dist}
License:	GPL-3.0-only
URL:		https://hg.sr.ht/~scoopta/wofi
Source0:        https://hg.sr.ht/~scoopta/%{name}/archive/v%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(wayland-client)
# /oreon:deps
%description
Wofi is a launcher/menu program for wlroots based wayland compositors such as
sway.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Files for development with %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n wofi-devel -f %{oreon_filedir}/wofi-devel.list

%changelog

%autochangelog
