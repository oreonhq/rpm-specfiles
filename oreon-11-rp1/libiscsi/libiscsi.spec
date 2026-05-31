%global source0_hash 212f6e1fd8e7ddb4b02208aafc6de600f6f330f40359babeefdd83b0c79d47a1

Name: libiscsi
Summary: iSCSI client library
Version: 1.20.3
Release: 4%{?dist}
License: LGPL-2.1-or-later
URL: https://github.com/sahlberg/%{name}
Source:        https://github.com/sahlberg/libiscsi/archive/%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: CUnit-devel
BuildRequires: gnutls-devel
BuildRequires: rdma-core-devel

%description
libiscsi is a library for attaching to iSCSI resources across
a network.


#######################################################################

# Conflict with iscsi-initiator-utils.

%global libiscsi_includedir %{_includedir}/iscsi
%global libiscsi_libdir %{_libdir}/iscsi

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n libiscsi-%{version}

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


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING LICENCE-LGPL-2.1.txt
%doc README.md TODO
%dir %{libiscsi_libdir}
%{libiscsi_libdir}/libiscsi.so.11*
%config /etc/ld.so.conf.d/*

%package utils
Summary: iSCSI Client Utilities
License: GPL-2.0-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
The libiscsi-utils package provides a set of assorted utilities to connect
to iSCSI servers without having to set up the Linux iSCSI initiator.

%files utils
%license LICENCE-GPL-2.txt
%{_bindir}/iscsi-ls
%{_bindir}/iscsi-inq
%{_bindir}/iscsi-readcapacity16
%{_bindir}/iscsi-swp
%{_bindir}/iscsi-perf
%{_bindir}/iscsi-test-cu
%{_bindir}/iscsi-pr
%{_bindir}/iscsi-discard
%{_bindir}/iscsi-md5sum
%{_bindir}/iscsi-rtpg
%{_mandir}/man1/iscsi-ls.1.gz
%{_mandir}/man1/iscsi-inq.1.gz
%{_mandir}/man1/iscsi-swp.1.gz
%{_mandir}/man1/iscsi-test-cu.1.gz
%{_mandir}/man1/iscsi-md5sum.1.gz

%package devel
Summary: iSCSI client development libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The libiscsi-devel package includes the header files for libiscsi.

%files devel
%dir %{libiscsi_includedir}
%{libiscsi_includedir}/iscsi.h
%{libiscsi_includedir}/scsi-lowlevel.h
%{libiscsi_libdir}/libiscsi.so
%{_libdir}/pkgconfig/libiscsi.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.20.3-4
- Prepare for Oreon 11 (RP1)
