# SPDX-License-Identifier: MIT

%global githubname qatzip
%global libqatzip_soversion 3

Name:           qatzip
Version:        1.3.2
Release:        1%{?dist}
Summary:        Intel QuickAssist Technology (QAT) QATzip Library
License:        BSD-3-Clause
URL:            https://github.com/intel/%{githubname}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc >= 4.8.5
BuildRequires:  zlib-devel >= 1.2.7
BuildRequires:  qatlib-devel >= 23.08.0
BuildRequires:  autoconf autoconf-archive automake libtool make lz4-devel numactl-devel
# The purpose of the package is to support hardware that only exists on x86_64 platforms
# https://bugzilla.redhat.com/show_bug.cgi?id=1987280
ExclusiveArch:  x86_64

%description
QATzip is a user space library which builds on top of the Intel
QuickAssist Technology user space library, to provide extended
accelerated compression and decompression services by offloading the
actual compression and decompression request(s) to the Intel Chipset
Series. QATzip produces data using the standard gzip* format
(RFC1952) with extended headers. The data can be decompressed with a
compliant gzip* implementation. QATzip is designed to take full
advantage of the performance provided by Intel QuickAssist
Technology.

%package        libs
Summary:        Libraries for the qatzip package

%description    libs
This package contains libraries for applications to use
the QATzip APIs.

%package        devel
Summary:        Development components for the libqatzip package
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
This package contains headers and libraries required to build
applications that use the QATzip APIs.

%prep
%autosetup -n %{githubname}-%{version}

%build
%set_build_flags

autoreconf -vif
./configure \
    --bindir=%{_bindir} \
    --libdir=%{_libdir} \
    --includedir=%{_includedir} \
    --mandir=%{_mandir} \
    --prefix=%{_prefix} \
    --enable-symbol

%make_build

%install
%make_install
rm %{buildroot}/%{_libdir}/libqatzip.a
rm %{buildroot}/%{_libdir}/libqatzip.la
rm -vf %{buildroot}%{_mandir}/*.pdf

# Check section is not available for these functional and performance tests require special hardware.

%files
%license LICENSE*
%{_mandir}/man1/qzip.1*
%{_mandir}/man1/qatzip-test.1*
%{_bindir}/qzip
%{_bindir}/qatzip-test

%files libs
%license LICENSE*
%{_libdir}/libqatzip.so.%{libqatzip_soversion}*

%files devel
%doc docs/QATzip-man.pdf
%{_includedir}/qatzip.h
%{_libdir}/libqatzip.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.2-1
- Prepare for Oreon 11 (RP1)
