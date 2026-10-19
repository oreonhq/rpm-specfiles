%global source0_hash a098c33924754ad43f981b740f6d576c70f9ed1006e12221b1845431ebce1239
%define gitdate 20070827
%define gitrev 8ff7213f39edc1b2b8b60d6b0cc5d5f14ca1928d
Name:           pixman
Version:        0.46.4
Release:        1%{?dist}
Summary:        Pixel manipulation library
License:        MIT
URL:            https://gitlab.freedesktop.org/pixman/pixman
Source0:        https://www.x.org/archive/individual/lib/%{name}-%{version}.tar.xz
Source1:        make-pixman-snapshot.sh
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
# /oreon:deps
%description
Pixman is a pixel manipulation library for X and Cairo.

%package devel
Summary: Pixel manipulation library development package
Requires: %{name}%{?isa} = %{version}-%{release}
Requires: pkgconfig
%description devel
Pixel manipulation library for X and Cairo development package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson --auto-features=auto \
  %nil
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%ldconfig_post
%ldconfig_postun
%files -f %{oreon_filedir}/main.list
%files -n pixman-devel -f %{oreon_filedir}/pixman-devel.list

%changelog

%autochangelog
