Summary:    X property display utility
Name:       xprop
Version:    1.2.8
Release:    %autorelease
License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 d689e2adb7ef7b439f6469b51cda8a7daefc83243854c2a3b8f84d0f029d67ee
%global source0_file xprop-1.2.8.tar.xz
# oreon url source checksums end

BuildRequires:  gcc make
BuildRequires:  gettext-devel
BuildRequires:  libtool

BuildRequires:  pkgconfig(x11)

Obsoletes: xorg-x11-utils < 7.5-39

%description
The xprop utility is for displaying window and font properties in an X server.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/xprop-1.2.8.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d689e2adb7ef7b439f6469b51cda8a7daefc83243854c2a3b8f84d0f029d67ee" || { echo "oreon: Source0 SHA256 mismatch for xprop-1.2.8.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%doc README.md
%license COPYING
%{_bindir}/xprop
%{_mandir}/man1/xprop.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.8-1
- Prepare for Oreon 11 (RP1)
