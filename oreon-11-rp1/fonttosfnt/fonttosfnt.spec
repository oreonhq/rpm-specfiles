%global source0_hash 2e251e66e8753c08aa280b26fd4a10d0d88e7d9bba5c8aac3d3fb36705e5918e
Name:       fonttosfnt
Version:    1.2.5
Release:        1%{?dist}
Summary:        Tool to wrap bdf or pcf bitmap fonts in an sfnt wrapper
License:    MIT
URL:        https://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Conflicts:  xorg-x11-font-utils < 7.5-51
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(fontenc)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros)
# /oreon:deps
%description
fonttosfnt wraps a set of bdf or pcf bitmap fonts in a sfnt (TrueType or
OpenType) wrapper.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-silent-rules
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
