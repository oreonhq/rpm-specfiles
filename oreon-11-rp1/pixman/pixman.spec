%global source0_hash d075209d18728b1ca5d0bb864aa047a262a1fde206da8a677d6af75b2ee1ae98

%define gitdate 20070827
%define gitrev 8ff7213f39edc1b2b8b60d6b0cc5d5f14ca1928d

Name:           pixman
Version:        0.46.2
Release:        3%{?dist}
Summary:        Pixel manipulation library

# SPDX
License:        MIT
URL:            https://gitlab.freedesktop.org/pixman/pixman
#VCS:           git:git://git.freedesktop.org/git/pixman
# To make git snapshots:
# ./make-pixman-snapshot.sh %{\?gitrev}
# if no revision specified, makes a new one from HEAD.
Source0:        https://www.x.org/archive/individual/lib/pixman-0.46.2.tar.xz
Source1:        make-pixman-snapshot.sh

BuildRequires:  gcc
BuildRequires:  meson

%description
Pixman is a pixel manipulation library for X and Cairo.

%package devel
Summary: Pixel manipulation library development package
Requires: %{name}%{?isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
Pixel manipulation library for X and Cairo development package.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
%meson --auto-features=auto \
  %nil

%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_post
%ldconfig_postun

%files
%doc COPYING
%{_libdir}/libpixman-1*.so.*

%files devel
%dir %{_includedir}/pixman-1
%{_includedir}/pixman-1/pixman.h
%{_includedir}/pixman-1/pixman-version.h
%{_libdir}/libpixman-1*.so
%{_libdir}/pkgconfig/pixman-1.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.46.2-3
- Prepare for Oreon 11 (RP1)
