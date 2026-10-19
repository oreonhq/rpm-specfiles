%global source0_hash 631f5e704a1b7c8f953ca017a382ad945e75c2952c81813ff355e9ab8071b70e
Name:		libavtp
Version:	0.2.0
Release:        1%{?dist}
Summary:        An AVTP protocol implementation
License:	BSD-3-Clause
URL:		https://github.com/Avnu/libavtp
Source0:        https://github.com/Avnu/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libcmocka-devel
BuildRequires:  meson
# /oreon:deps
%description
An open source implementation of Audio Video Transport
Protocol (AVTP) specified in IEEE 1722-2016 spec.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n libavtp-devel -f %{oreon_filedir}/libavtp-devel.list

%changelog

%autochangelog

