%global source0_hash d83659a41f9f2aa051311cf8139aa5aebc998291f81222d06a3e82aea1defc1a
%global _hardened_build 1
Name:		libtnc
Version:	1.25
Release:        1%{?dist}
Summary:        Library implementation of the Trusted Network Connect (TNC) specification
License:	GPL-2.0-only
Source0:        http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
Patch0:		libtnc-1.25-bootstrap.patch
Patch1:		libtnc-1.25-syserror.patch
Patch2:		libtnc-1.25-symbolfix.patch
URL:		http://libtnc.sourceforge.net/
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  zlib-devel
# /oreon:deps
%description
This library provides functions for loading and interfacing with loadable IMC
Integrity Measurement Collector (IMC) and Integrity Measurement Verifier (IMV)
modules as required by the Trusted Network Computing (TNC) IF-IMC and IF-IMV 
interfaces as described in: https://www.trustedcomputinggroup.org/specs/TNC

%package devel
Summary:	Development headers and libraries for libtnc
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
Header and library files used for developing with (or linking to) libtnc.

%package -n perl-Interface-TNC
Version:	1.0
Summary:	Perl module for TNC interfaces
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
%description -n perl-Interface-TNC
Perl module for TNC interfaces

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

pushd Interface-TNC
tar xf Interface-TNC-1.0.tar.gz
popd

%patch -P0 -p1 -b .bootstrap
%patch -P1 -p1 -b .syserror
%patch -P2 -p1 -b .symbolfix

%build

%global build_type_safety_c 0
%set_build_flags
CC="$CC -std=gnu89"
CFLAGS="%{optflags} -fPIC -DPIC"
%configure --with-pic
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
pushd Interface-TNC/Interface-TNC-1.0
%{__perl} Makefile.PL INSTALLDIRS=vendor
make CC="$CC" %{?_smp_mflags}
popd
%install
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/%{_libdir}/*.la
rm -rf %{buildroot}/%{_libdir}/*.a
pushd Interface-TNC/Interface-TNC-1.0
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';'
popd
%oreon_autofiles perl-Interface-TNC usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libtnc-devel -f %{oreon_filedir}/libtnc-devel.list
%files -n perl-Interface-TNC -f %{oreon_filedir}/perl-Interface-TNC.list

%changelog

%autochangelog
