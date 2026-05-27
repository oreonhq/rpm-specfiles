%global source0_hash b47d3ac19d3549e54a05d0019a6c400674da716123858cfdb6d3bdd70a66c702

%define _root_libdir    /%{_lib}

Name:			libtirpc
Version:		1.3.7
Release:		2%{?dist}
Summary:		Transport Independent RPC Library
License:		SISSL AND BSD-3-Clause
URL:  			http://git.linux-nfs.org/?p=steved/libtirpc.git;a=summary
Source0:		http://downloads.sourceforge.net/libtirpc/libtirpc-%{version}.tar.bz2

BuildRequires:		automake, autoconf, libtool, pkgconfig
BuildRequires:		krb5-devel
BuildRequires:		gcc
BuildRequires: make

%description
This package contains SunLib's implementation of transport-independent
RPC (TI-RPC) documentation.  This library forms a piece of the base of 
Open Network Computing (ONC), and is derived directly from the 
Solaris 2.3 source.

TI-RPC is an enhanced version of TS-RPC that requires the UNIX System V 
Transport Layer Interface (TLI) or an equivalent X/Open Transport Interface 
(XTI).  TI-RPC is on-the-wire compatible with the TS-RPC, which is supported 
by almost 70 vendors on all major operating systems.  TS-RPC source code 
(RPCSRC 4.0) remains available from several internet sites.

%package devel
Summary:		Development files for the libtirpc library
Requires:		%{name}%{?_isa} = %{version}-%{release}
Requires:		pkgconfig

%description devel
This package includes header files and libraries necessary for
developing programs which use the tirpc library.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

# Remove .orig files
find . -name "*.orig" | xargs rm -f

%build
sh autogen.sh
autoreconf -fisv
%configure
make all

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/etc
mkdir -p %{buildroot}%{_root_libdir}
mkdir -p %{buildroot}%{_libdir}/pkgconfig
make install DESTDIR=%{buildroot} \
	libdir=%{_root_libdir} pkgconfigdir=%{_libdir}/pkgconfig
# Don't package .a or .la files
rm -f %{buildroot}%{_root_libdir}/*.{a,la}

# Creat the man diretory
mv %{buildroot}%{_mandir}/man3 %{buildroot}%{_mandir}/man3t


%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_root_libdir}/libtirpc.so.*
%config(noreplace)%{_sysconfdir}/netconfig
%config(noreplace)%{_sysconfdir}/bindresvport.blacklist

%files devel
%{!?_licensedir:%global license %%doc}
%license COPYING
%dir %{_includedir}/tirpc
%dir %{_includedir}/tirpc/rpc
%dir %{_includedir}/tirpc/rpcsvc
%{_root_libdir}/libtirpc.so
%{_libdir}/pkgconfig/libtirpc.pc
%{_includedir}/tirpc/netconfig.h
%{_includedir}/tirpc/rpc/auth.h
%{_includedir}/tirpc/rpc/auth_des.h
%{_includedir}/tirpc/rpc/auth_gss.h
%{_includedir}/tirpc/rpc/auth_unix.h
%{_includedir}/tirpc/rpc/des.h
%{_includedir}/tirpc/rpc/des_crypt.h
%{_includedir}/tirpc/rpc/rpcsec_gss.h
%{_includedir}/tirpc/rpc/clnt.h
%{_includedir}/tirpc/rpc/clnt_soc.h
%{_includedir}/tirpc/rpc/clnt_stat.h
%{_includedir}/tirpc/rpc/key_prot.h
%{_includedir}/tirpc/rpc/nettype.h
%{_includedir}/tirpc/rpc/pmap_clnt.h
%{_includedir}/tirpc/rpc/pmap_prot.h
%{_includedir}/tirpc/rpc/pmap_rmt.h
%{_includedir}/tirpc/rpc/raw.h
%{_includedir}/tirpc/rpc/rpc.h
%{_includedir}/tirpc/rpc/rpc_com.h
%{_includedir}/tirpc/rpc/rpc_msg.h
%{_includedir}/tirpc/rpc/rpcb_clnt.h
%{_includedir}/tirpc/rpc/rpcb_prot.h
%{_includedir}/tirpc/rpc/rpcb_prot.x
%{_includedir}/tirpc/rpc/rpcent.h
%{_includedir}/tirpc/rpc/svc.h
%{_includedir}/tirpc/rpc/svc_auth.h
%{_includedir}/tirpc/rpc/svc_auth_gss.h
%{_includedir}/tirpc/rpc/svc_dg.h
%{_includedir}/tirpc/rpc/svc_mt.h
%{_includedir}/tirpc/rpc/svc_soc.h
%{_includedir}/tirpc/rpc/types.h
%{_includedir}/tirpc/rpc/xdr.h
%{_includedir}/tirpc/rpcsvc/crypt.h
%{_includedir}/tirpc/rpcsvc/crypt.x
%{_mandir}/*/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.7-2
- Prepare for Oreon 11 (RP1)
