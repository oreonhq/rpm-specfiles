%global source0_hash 0d3712defa457f23cff6eb696797c4b38d9590ca9012cb01e39e4b5da63f1630
%global libpqos_ver 6.0.1
%global desc %{expand: \
This package provides basic support for Intel Resource Director Technology
including, Cache Monitoring Technology (CMT), Memory Bandwidth Monitoring
(MBM), Cache Allocation Technology (CAT), Code and Data Prioritization 
(CDP) and Memory Bandwidth Allocation (MBA).}
Name:		intel-cmt-cat
Version:	26.06
Release:        1%{?dist}
Summary:        Intel cache monitoring and allocation technology config tool
License:	BSD-3-Clause
URL: 		https://github.com/intel/intel-cmt-cat
Source0:        https://github.com/intel/intel-cmt-cat/archive/refs/tags/v%{version}.tar.gz#/intel-cmt-cat-%{version}.tar.gz
ExclusiveArch:	x86_64
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
%{desc}

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel %{desc}

Development files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%make_build
%install
%make_install BIN_DIR="%{buildroot}%{_bindir}" SBIN_DIR="%{buildroot}%{_sbindir}"
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n intel-cmt-cat-devel -f %{oreon_filedir}/intel-cmt-cat-devel.list

%changelog

%autochangelog
