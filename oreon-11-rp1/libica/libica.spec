# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 edc755494797331427c5f7900c7eecd8b5ecd3e69b7502313bf764f490b8e87a
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global with_fips 1

Summary: Library for accessing ICA hardware crypto on IBM z Systems
Name: libica
Version: 4.4.1
Release: 3%{?dist}
License: CPL-1.0
URL: https://github.com/opencryptoki/
Source0: https://github.com/opencryptoki/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# annotate assembler source
# https://bugzilla.redhat.com/show_bug.cgi?id=1630582
# https://github.com/opencryptoki/libica/pull/24
Patch0: %{name}-4.0.0-annotate.patch
# post GA fixes
#Patch1: %%{name}-%%{version}-fixes.patch
BuildRequires: gcc
BuildRequires: openssl-devel
BuildRequires: openssl
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: autoconf-archive
BuildRequires: perl(FindBin)
BuildRequires: perl(lib)
BuildRequires: make
ExclusiveArch: s390 s390x

%description
A library of functions and utilities for accessing ICA hardware crypto on
IBM z Systems.


%package devel
Summary: Development tools for programs to access ICA hardware crypto on IBM z Systems
Requires: %{name} = %{version}-%{release}
Requires: openssl-devel

%description devel
The libica-devel package contains the header files and static
libraries necessary for developing programs accessing ICA hardware crypto on
IBM z Systems.


%prep
%oreon_verify_sources
%autosetup -p1

sh ./bootstrap.sh


%build
# FIPS openssl config is not needed on RHEL/Fedora
# https://bugzilla.redhat.com/show_bug.cgi?id=2084097
CPPFLAGS=-DNO_FIPS_CONFIG_LOAD
export CPPFLAGS
%configure --disable-static \
%if %{with_fips}
    --enable-fips
%else
    --disable-fips
%endif
%make_build


%install
%make_install
rm %{buildroot}%{_libdir}/libica*.la
rm %{buildroot}%{_pkgdocdir}/{INSTALL,README.md}


%check
# mock doesn't provide the device, so check here
# https://github.com/rpm-software-management/mock/issues/33
if [ -c /dev/hwrng -o -c /dev/prandom ]; then
    make check
fi

%if %{with_fips}
%define __spec_install_post \
    %{?__debug_package:%{__debug_install_post}} \
    %{__arch_install_post} \
    %{__os_install_post} \
    make fipsinstall DESTDIR=%{buildroot}
    %{nil}
%endif

%files
%doc AUTHORS LICENSE ChangeLog
%{_bindir}/icainfo
%{_bindir}/icainfo-cex
%{_bindir}/icastats
%if %{with_fips}
%if 0%{?fedora} >= 36 || 0%{?rhel} >= 9 || 0%{?oreon}
# openssl 3.0 is available since Fedora 36 and RHEL 9
%exclude %{_sysconfdir}/libica/openssl3-fips.cnf
%endif
%{_libdir}/.libica.*.hmac
%{_libdir}/.libica-cex.*.hmac
%endif
%{_libdir}/libica.so.*
%{_libdir}/libica-cex.so.*
%{_mandir}/man1/icainfo.1*
%{_mandir}/man1/icainfo-cex.1*
%{_mandir}/man1/icastats.1*

%files devel
%{_includedir}/*
%{_libdir}/libica.so
%{_libdir}/libica-cex.so


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.4.1-3
- Import
