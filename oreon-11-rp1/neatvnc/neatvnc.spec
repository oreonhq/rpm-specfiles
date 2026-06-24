%global source0_hash none

# -*-Mode: rpm-spec -*-

Name:     neatvnc
Version:  0.9.0
Release:  6%{?dist}
Summary:  Liberally licensed VNC server library
# main source is ISC
# include/sys/queue.h is BSD
License:  ISC AND BSD-2-Clause AND BSD-3-Clause

URL:      https://github.com/any1/neatvnc
Source:   %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Backport to fix i686 builds
# From: https://github.com/any1/neatvnc/commit/e0e0ce5c579cafc763992f1c1bb964eb95999fb7
Patch:    0001-server-Use-correct-type-for-length-in-compress.patch

BuildRequires: gcc
BuildRequires: git-core
BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(aml)
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(nettle)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(zlib)
BuildRequires: turbojpeg-devel

%description
This is a liberally licensed VNC server library that's intended to be
fast and neat. Note: This is a beta release, so the interface is not
yet stable.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains header files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git_am

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license COPYING
%{_libdir}/lib%{name}.so.0{,.*}

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog

