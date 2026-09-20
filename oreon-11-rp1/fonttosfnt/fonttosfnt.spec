%global source0_hash 2e251e66e8753c08aa280b26fd4a10d0d88e7d9bba5c8aac3d3fb36705e5918e

Name:       fonttosfnt
Version:    1.2.5
Release:    %autorelease
Summary:    Tool to wrap bdf or pcf bitmap fonts in an sfnt wrapper

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  gcc make libtool
BuildRequires:  pkgconfig(fontenc)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Conflicts:  xorg-x11-font-utils < 7.5-51

%description
fonttosfnt wraps a set of bdf or pcf bitmap fonts in a sfnt (TrueType or
OpenType) wrapper.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/fonttosfnt
%{_mandir}/man1/fonttosfnt.1*

%changelog
%autochangelog
