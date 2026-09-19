%global source0_hash dd838bae9d2b19ddd71fe6d30ed33abc7c85e19d223e79d35600db3fa44bf734

Name: xdriinfo
Version: 1.0.7
Release: %autorelease
Summary: X application to query configuration information of DRI drivers
License: MIT
URL: https://gitlab.freedesktop.org/xorg/app/xdriinfo
Source0: https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Source1: https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz.sig
Source2: https://gitlab.freedesktop.org/alanc.gpg

# This package was split from the mesa-demos Fedora package, which used to
# also build and install xdriinfo in its glx-utils until mesa-demos-9.0.0-3
Conflicts: glx-utils < 9.0.0-4

BuildRequires: gcc
BuildRequires: libglvnd-devel
BuildRequires: xorg-x11-util-macros
BuildRequires: make autoconf automake libtool
BuildRequires: gnupg2

%description
xdriinfo can be used to query configuration information of direct
rendering drivers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/xdriinfo
%{_mandir}/man1/xdriinfo.1*
%doc AUTHORS ChangeLog README.md

%changelog
%autochangelog
