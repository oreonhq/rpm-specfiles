%global source0_hash 188e30db9eafb44eaa8579e1d7ae70ce7b14634c5bfae7612e3e185e446f39dc
%global	project_name	idxd-config
Name:		accel-config
Version:	4.1.8
Release:        1%{?dist}
Summary:        Configure accelerator subsystem devices
License:	GPL-2.0-only
URL:		https://github.com/intel/%{project_name}
Source0:        https://github.com/intel/idxd-config/archive/refs/tags/accel-config-v%{version}.tar.gz#/accel-config-v%{version}.tar.gz
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
ExclusiveArch:	%{ix86} x86_64
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libkmod)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  systemd
BuildRequires:  xmlto
# /oreon:deps
%description
Utility library for configuring the accelerator subsystem.

%package devel
Summary:	Development files for libaccfg
License:	LGPL-2.1-only
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package libs
Summary:	Configuration library for accelerator subsystem devices
License:	LGPL-2.1-only
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description libs
Libraries for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{project_name}-%{name}-v%{version}

%build

echo %{version} > version
./autogen.sh
%configure --disable-static --disable-silent-rules
%make_build
%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%oreon_autofiles accel-config-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles accel-config-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n accel-config-devel -f %{oreon_filedir}/accel-config-devel.list
%files -n accel-config-libs -f %{oreon_filedir}/accel-config-libs.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.1.8-13
- Import
