Name:           ocl-icd
Version:        2.3.4
Release:        %autorelease
Summary:        OpenCL Library (Installable Client Library) Bindings
License:        BSD-2-Clause
URL:            https://github.com/OCL-dev/%{name}/

Source0:        https://github.com/OCL-dev/ocl-icd//archive/v2.3.4/ocl-icd-2.3.4.tar.gz
# oreon url source checksums begin
%global source0_sha256 1a302b71b7304cca5a36f69d017b1af2b762cc4c2dd1c0c0e2fc1933db25c9cc
%global source0_file ocl-icd-2.3.4.tar.gz
# oreon url source checksums end

BuildRequires:  asciidoc
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  opencl-headers
BuildRequires:  ruby rubygems
BuildRequires:  xmlto

%description
%{summary}.

%package devel
Summary:        OpenCL Library Development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       opencl-headers

%description devel
This package contains the development files for the OpenCL ICD bindings.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/ocl-icd-2.3.4.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1a302b71b7304cca5a36f69d017b1af2b762cc4c2dd1c0c0e2fc1933db25c9cc" || { echo "oreon: Source0 SHA256 mismatch for ocl-icd-2.3.4.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup

%build
autoreconf -vfi
%configure
%make_build

%install
%make_install
rm -vrf %{buildroot}%{_defaultdocdir}

%check
make check

%files
%license COPYING
%doc NEWS README
%{_libdir}/libOpenCL.so.1
%{_libdir}/libOpenCL.so.1.0.0
%{_mandir}/man7/libOpenCL.7*
%{_mandir}/man7/libOpenCL.so.7*

%files devel
%doc ocl_icd_loader_gen.map ocl_icd_bindings.c
%{_includedir}/ocl_icd.h
%{_bindir}/cllayerinfo
%{_libdir}/libOpenCL.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/OpenCL.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.4-1
- Prepare for Oreon 11 (RP1)
