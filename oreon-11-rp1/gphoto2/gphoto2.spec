%global source0_hash 4e379a0f12f72b49ee5ee2283ffd806b5d12d099939d75197a3f4bbc7f27a1a1
Name:           gphoto2
Version:        2.5.32
Release:        1%{?dist}
Summary:        Software for accessing digital cameras
License:        GPL-2.0-or-later
Url:            http://www.gphoto.org/
Source0:        http://downloads.sourceforge.net/gphoto/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libjpeg-devel
BuildRequires:  make
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libgphoto2)
BuildRequires:  popt-devel
BuildRequires:  readline-devel
# /oreon:deps
%description
The gPhoto2 project is a universal, free application and library
framework that lets you download images from several different
digital camera models, including the newer models with USB
connections. Note that
a) for some older camera models you must use the old "gphoto" package.
b) for USB mass storage models you must use the driver in the kernel

This package contains the command-line utility gphoto2.

Other (GUI) frontends are available separately.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
rm %{buildroot}%{_docdir}/%{name}/test-hook.sh
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
