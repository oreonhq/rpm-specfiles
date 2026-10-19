%global source0_hash cdd7984425fa92d37273eee4180b5f57b047eda6dd8fd623e58498f844b09b75
Name:           ocl-icd
Version:        2.3.5
Release:        1%{?dist}
Summary:        OpenCL Library (Installable Client Library) Bindings
License:        BSD-2-Clause
URL:            https://github.com/OCL-dev/%{name}/
Source0:        https://github.com/OCL-dev/ocl-icd//archive/refs/tags/v2.3.5/ocl-icd-2.3.5.tar.gz#/ocl-icd-2.3.5.tar.gz
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  opencl-headers
BuildRequires:  ruby
BuildRequires:  rubygems
BuildRequires:  xmlto
# /oreon:deps
%description
%{summary}.

%package devel
Summary:        OpenCL Library Development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       opencl-headers
%description devel
This package contains the development files for the OpenCL ICD bindings.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -vfi
%configure
%make_build
%install
%make_install
rm -vrf %{buildroot}%{_defaultdocdir}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n ocl-icd-devel -f %{oreon_filedir}/ocl-icd-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.4-1
- Prepare for Oreon 11 (RP1)
