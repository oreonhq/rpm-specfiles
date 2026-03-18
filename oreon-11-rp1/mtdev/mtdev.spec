%global tarball mtdev
#global gitdate 20110105

Name:           mtdev
Version:        1.1.6
Release:        12%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
Summary:        Multitouch Protocol Translation Library

# SPDX
License:        MIT
URL:            http://bitmath.org/code/mtdev/

# upstream doesn't have tarballs

%if 0%{?gitdate}
Source0:        %{tarball}-%{gitdate}.tar.bz2
Source1:        make-git-snapshot.sh
Source2:        commitid
%else
Source0:        http://bitmath.org/code/%{name}/%{name}-%{version}.tar.bz2
%endif

BuildRequires:  autoconf automake libtool gcc make make make make

%description
%{name} is a stand-alone library which transforms all variants of kernel MT
events to the slotted type B protocol. The events put into mtdev may be from
any MT device, specifically type A without contact tracking, type A with
contact tracking, or type B with contact tracking.

%package devel
Summary:        Multitouch Protocol Translation Library Development Package
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Multitouch protocol translation library development package.

%prep
%setup -q -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build
autoreconf --force -v --install || exit 1
%configure --disable-static
%make_build

%install
rm -rf %{buildroot}
%make_install

# We intentionally don't ship *.la files
rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc COPYING README
%{_libdir}/libmtdev.so.*

%files devel
%{_includedir}/mtdev.h
%{_includedir}/mtdev-plumbing.h
%{_includedir}/mtdev-mapping.h
%{_libdir}/libmtdev.so
%{_libdir}/pkgconfig/mtdev.pc
%{_bindir}/mtdev-test

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.6-12
- Prepare for Oreon 11 (RP1)
