%global source0_hash 2a648dcdf12da19e208255df4ebed3e7d2a02f905be4165f2443c984cf887375

Name:           gphoto2
Version:        2.5.28
Release:        5%{?dist}
Summary:        Software for accessing digital cameras
License:        GPL-2.0-or-later
Url:            http://www.gphoto.org/
Source0:        http://downloads.sourceforge.net/gphoto/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libgphoto2) >= %{version}
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig(libexif)
BuildRequires:  popt-devel
BuildRequires:  readline-devel

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

%autosetup

%build
%configure
%make_build

%install
%make_install
rm %{buildroot}%{_docdir}/%{name}/test-hook.sh
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc NEWS README TODO
%{_bindir}/gphoto2
%{_mandir}/man1/gphoto2.1*

%changelog
%autochangelog
