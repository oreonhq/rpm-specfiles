%global source0_hash 249635f67fb94fabd46837283c40ba8dd5e7b774df2bac03d5026a3480766372

Name:       fonttosfnt
Version:    1.2.4
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
