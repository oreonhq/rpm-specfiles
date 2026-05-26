Name:       xhost
Version:    1.0.9
Release:    11%{?dist}
Summary:    Manage hosts or users allowed to connect to the X server

License:    MIT AND ICU
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

Patch01:    0001-Replace-inet_addr-inet_aton-with-a-call-to-inet_pton.patch
# oreon url source checksums begin
%global source0_sha256 ea86b531462035b19a2e5e01ef3d9a35cca7d984086645e2fc844d8f0e346645
%global source0_file xhost-1.0.9.tar.xz
# oreon url source checksums end

BuildRequires:  automake libtool
BuildRequires:  gcc make gettext
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-server-utils < 7.7-40

%description
xhost is used to manage the list of host names or user names
allowed to make connections to the X server.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/xhost-1.0.9.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ea86b531462035b19a2e5e01ef3d9a35cca7d984086645e2fc844d8f0e346645" || { echo "oreon: Source0 SHA256 mismatch for xhost-1.0.9.tar.xz" >&2; exit 1; })
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.9-11
- Prepare for Oreon 11 (RP1)
