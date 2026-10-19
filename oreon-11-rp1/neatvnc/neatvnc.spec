%global source0_hash 06bd3aefb58d66aef14e42143e8f75c84e3b54fc800acb2d2a2de0f507359d50
Name:     neatvnc
Version:  1.0.2
Release:        1%{?dist}
Summary:        Liberally licensed VNC server library
License:  ISC AND BSD-2-Clause AND BSD-3-Clause
URL:      https://github.com/any1/neatvnc
Source0:        https://github.com/any1/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  pkgconfig(aml)
BuildRequires:  pkgconfig(aml1)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  turbojpeg-devel
# /oreon:deps
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
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n neatvnc-devel -f %{oreon_filedir}/neatvnc-devel.list

%changelog

%autochangelog

