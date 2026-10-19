%global source0_hash 04789029d4a62cb86c6403887a8c9b79ab3fb08f76fd0db0d312674f9efacf9c
%global libapivermajor 0
%global libapiversion %{libapivermajor}.1
Name:		kafs-client
Version:	0.4
Release:        1%{?dist}
Summary:        The basic tools for kAFS and mounter for the AFS dynamic root
License:	GPL-2.0-or-later
URL:		https://www.infradead.org/~dhowells/kafs/
Source0:        https://www.infradead.org/~dhowells/kafs/kafs-client-%{version}.tar.bz2
Requires: filesystem-afs
%global datadir %{_datarootdir}/kafs
Requires: keyutils >= 1.6
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
Requires: selinux-policy-base >= 3.7.19-5
# oreon:deps
BuildRequires:  gcc
BuildRequires:  keyutils-libs-devel
BuildRequires:  krb5-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  systemd-units
# /oreon:deps
%description
Provide basic AFS-compatible tools for kAFS and systemd scripts to mount the
dynamic root on /afs and preload the cell database.

%package libs
Summary: Library of routines for dealing with kAFS
Requires: %{name}%{?_isa} = %{version}-%{release}
%description libs
Provide a library of shareable routines for dealing with the kAFS
filesystem.  These provide things like configuration parsing and DNS lookups.

%package libs-devel
Summary: Library of routines for dealing with kAFS
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description libs-devel
Provide a library of shareable routines for dealing with the kAFS
filesystem.  These provide things like configuration parsing and DNS lookups.

#
# We generate a compatibility package that makes kafs look like OpenAFS, but it
# needs to be uninstalled be able to install OpenAFS or Auristor.
#
%package compat
Summary: AFS compatibility package
Requires: %{name}%{?_isa} = %{version}-%{release}
%description compat
Compatibility package providing standard AFS names for tools such as
aklog.  This package must be uninstalled for kAFS to coexist with
another AFS implementation (such as OpenAFS).

%global _hardened_build 1
%global docdir %{_docdir}/kafs-client

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%make_build \
	ETCDIR=%{_sysconfdir} \
	BINDIR=%{_bindir} \
	SBINDIR=%{_sbindir} \
	DATADIR=%{datadir} \
	INCLUDEDIR=%{_includedir} \
	LIBDIR=%{_libdir} \
	LIBEXECDIR=%{_libexecdir} \
	MANDIR=%{_mandir} \
	CFLAGS="-Wall -Werror $RPM_OPT_FLAGS $RPM_LD_FLAGS $ARCH_OPT_FLAGS"
%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_datarootdir}
%make_install \
	ETCDIR=%{_sysconfdir} \
	BINDIR=%{_bindir} \
	SBINDIR=%{_sbindir} \
	DATADIR=%{datadir} \
	INCLUDEDIR=%{_includedir} \
	LIBDIR=%{_libdir} \
	LIBEXECDIR=%{_libexecdir} \
	MANDIR=%{_mandir} \
	CFLAGS="-Wall -Werror $RPM_OPT_FLAGS $RPM_LD_FLAGS $ARCH_OPT_FLAGS"
ln -s aklog-kafs %{buildroot}/%{_bindir}/aklog
%ldconfig_scriptlets libs
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post afs.mount
%preun

%systemd_preun afs.mount
%postun

%systemd_postun_with_restart afs.mount
%files -f %{oreon_filedir}/main.list
%files -n kafs-client-libs -f %{oreon_filedir}/kafs-client-libs.list
%files -n kafs-client-libs-devel -f %{oreon_filedir}/kafs-client-libs-devel.list
%files -n kafs-client-compat -f %{oreon_filedir}/kafs-client-compat.list

%changelog

%autochangelog
