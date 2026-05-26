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
Source0:        https://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.xz
Source1:        make-pixman-snapshot.sh
# oreon url source checksums begin
%global source0_sha256 d075209d18728b1ca5d0bb864aa047a262a1fde206da8a677d6af75b2ee1ae98
%global source0_file pixman-0.46.2.tar.xz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/pixman-0.46.2.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d075209d18728b1ca5d0bb864aa047a262a1fde206da8a677d6af75b2ee1ae98" || { echo "oreon: Source0 SHA256 mismatch for pixman-0.46.2.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
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
