%global source0_hash 212f6e1fd8e7ddb4b02208aafc6de600f6f330f40359babeefdd83b0c79d47a1
Name: libiscsi
Summary:        iSCSI client library
Version: 1.20.3
Release:        4%{?dist}
License: LGPL-2.1-or-later
URL: https://github.com/sahlberg/%{name}
Source0:        https://github.com/sahlberg/libiscsi/archive/refs/tags/%{version}.tar.gz#/libiscsi-1.20.3.tar.gz
# oreon:deps
BuildRequires:  CUnit-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gnutls-devel
BuildRequires:  libtool
BuildRequires:  rdma-core-devel
# /oreon:deps
%description
libiscsi is a library for attaching to iSCSI resources across
a network.

#######################################################################

# Conflict with iscsi-initiator-utils.

%global libiscsi_includedir %{_includedir}/iscsi
%global libiscsi_libdir %{_libdir}/iscsi

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libiscsi-%{version}
%oreon_prep
%build

sh autogen.sh
%configure --libdir=%{libiscsi_libdir} --disable-werror --with-gnutls
make %{?_smp_mflags}
%install
make DESTDIR=$RPM_BUILD_ROOT install pkgconfigdir=%{_libdir}/pkgconfig %{?_smp_mflags}
mkdir -p $RPM_BUILD_ROOT/etc/ld.so.conf.d
echo %{libiscsi_libdir} > $RPM_BUILD_ROOT/etc/ld.so.conf.d/%{name}-%{_arch}.conf
rm $RPM_BUILD_ROOT/%{libiscsi_libdir}/libiscsi.a
rm $RPM_BUILD_ROOT/%{libiscsi_libdir}/libiscsi.la
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%package utils
Summary: iSCSI Client Utilities
License: GPL-2.0-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}
%description utils
The libiscsi-utils package provides a set of assorted utilities to connect
to iSCSI servers without having to set up the Linux iSCSI initiator.

%package devel
Summary: iSCSI client development libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The libiscsi-devel package includes the header files for libiscsi.

%files -f %{oreon_filedir}/main.list
%files -n libiscsi-utils -f %{oreon_filedir}/libiscsi-utils.list
%files -n libiscsi-devel -f %{oreon_filedir}/libiscsi-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.20.3-4
- Prepare for Oreon 11 (RP1)
