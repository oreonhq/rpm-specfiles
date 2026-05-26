Name:       xrdb
Version:    1.2.2
Release:    7%{?dist}
Summary:    X server resource database utility

License:    HPND-DEC AND MIT-open-group
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 31f5fcab231b38f255b00b066cf7ea3b496df712c9eb2d0d50c670b63e5033f4
%global source0_file xrdb-1.2.2.tar.xz
# oreon url source checksums end

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Recommends: cpp

Obsoletes:  xorg-x11-server-utils < 7.7-40

%description
xrdb is used to get or set the contents of the RESOURCE_MANAGER property on
the root window of screen 0, or the SCREEN_RESOURCES property on the
root window of any or all screens, or everything combined.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/xrdb-1.2.2.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "31f5fcab231b38f255b00b066cf7ea3b496df712c9eb2d0d50c670b63e5033f4" || { echo "oreon: Source0 SHA256 mismatch for xrdb-1.2.2.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup

%build
autoreconf -v --install
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.2-7
- Prepare for Oreon 11 (RP1)
